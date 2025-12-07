"""
Modern Music Player (Audio Only) using:
- customtkinter for a modern-looking UI
- pygame.mixer for audio playback
- mutagen (optional) to detect mp3 duration

Features:
- Open a folder and build a playlist automatically
- Play / Pause / Resume
- Next / Previous song
- Stop
- Volume slider
- Timeline slider with seeking
- Loop current song checkbox
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pygame

# Try to import mutagen for MP3 duration detection.
# If not installed, MP3 will still play, but duration may show as --:--.
try:
    from mutagen.mp3 import MP3
except ImportError:
    MP3 = None

# ------------------- GLOBAL STATE VARIABLES -------------------

# List of full file paths for all songs in the current playlist
playlist = []

# Index of the currently playing song inside `playlist`
# -1 means "no song selected yet"
current_index = -1

# True if music is currently paused, False otherwise
paused = False

# True while user is dragging the position slider (so we don't update it automatically)
is_dragging_slider = False

# Fallback max range for slider if we cannot detect real duration
# (300 seconds = 5 minutes)
ESTIMATED_MAX_SECONDS = 300

# This tracks where in the song we started playing last time (in seconds).
# Example:
#   - start song from beginning: seek_base_seconds = 0
#   - seek to 60 sec: seek_base_seconds = 60
# Then pygame.mixer.music.get_pos() gives "time since last play()".
seek_base_seconds = 0

# Total duration of the current song in seconds (0 = unknown duration)
current_total_seconds = 0

# Tk / CTk widget references (will be set up in build_ui())
loop_current = None        # BooleanVar for "Loop current song" checkbox
root = None                # Main CTk window

playlist_box = None        # Listbox showing all songs
song_label = None          # Label showing current song name
progress_label = None      # Label showing "mm:ss / mm:ss"
volume_slider = None       # Slider to adjust volume
position_slider = None     # Slider to show / control current song time


# ------------------- DURATION HELPERS -------------------

def get_song_length_seconds(path: str) -> int:
    """
    Return song length in seconds for the given file path.

    We try two methods:
    1. mutagen for mp3 files (more accurate).
    2. pygame.mixer.Sound for other formats (and as a fallback).

    If both fail, return 0 (unknown length).
    """
    # 1. Try mutagen for MP3 files (if installed)
    if MP3 is not None and path.lower().endswith(".mp3"):
        try:
            audio = MP3(path)
            return int(audio.info.length)  # length is in seconds (float)
        except Exception:
            # If anything goes wrong, just ignore and try pygame.
            pass

    # 2. Fallback: use pygame Sound object, which supports several formats
    try:
        sound = pygame.mixer.Sound(path)
        return int(sound.get_length())  # length in seconds (float)
    except Exception:
        # Give up and return 0 if duration can't be determined
        return 0


# ------------------- CORE PLAYER LOGIC -------------------

def load_folder():
    """
    Ask user to choose a folder, load all supported audio files,
    and build the playlist from that folder.
    """
    global playlist, current_index

    # Open a folder selection dialog
    folder = filedialog.askdirectory(title="Select Music Folder")
    if not folder:
        # User cancelled
        return

    # Reset playlist and clear listbox
    playlist = []
    playlist_box.delete(0, tk.END)

    # Loop through all files in selected folder
    for file in os.listdir(folder):
        # Only accept certain audio types
        if file.lower().endswith((".mp3", ".wav", ".ogg")):
            full_path = os.path.join(folder, file)
            playlist.append(full_path)
            # Show only the filename (not the full path) in the listbox
            playlist_box.insert(tk.END, file)

    if not playlist:
        # Folder has no audio files
        messagebox.showinfo("No music", "No .mp3 / .wav / .ogg files found.")
        return

    # Auto-select the first song in the playlist
    current_index = 0
    playlist_box.selection_clear(0, tk.END)
    playlist_box.selection_set(0)
    playlist_box.activate(0)

    # Start playing the first song
    play_song(current_index)


def play_song(index: int):
    """
    Load and play the song at the given playlist index.
    Also updates UI: song name, total duration, slider range, etc.
    """
    global current_index, paused, seek_base_seconds, current_total_seconds

    # Safety check: index must be within playlist range
    if index < 0 or index >= len(playlist):
        return

    file_path = playlist[index]
    try:
        # Load and play the audio file using pygame.mixer.music
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        paused = False
        current_index = index

        # Since we start from the beginning, base time is 0
        seek_base_seconds = 0

        # Show the current filename in the UI
        filename = os.path.basename(file_path)
        song_label.configure(text=f"▶ {filename}")

        # Detect the actual length of this song (in seconds)
        current_total_seconds = get_song_length_seconds(file_path)

        if current_total_seconds > 0:
            # We know the real duration, so we set slider max accordingly
            position_slider.configure(from_=0, to=current_total_seconds)

            total_m = current_total_seconds // 60
            total_s = current_total_seconds % 60
            # Initial display: starting from 00:00
            progress_label.configure(text=f"00:00 / {total_m:02d}:{total_s:02d}")
        else:
            # If we don't know length, use fallback estimated range
            position_slider.configure(from_=0, to=ESTIMATED_MAX_SECONDS)
            progress_label.configure(text="00:00 / --:--")

        # Reset slider thumb to time=0
        position_slider.set(0)

    except Exception as e:
        # Common errors: unsupported format, file not found, etc.
        messagebox.showerror("Error", f"Could not play file:\n{e}")


def play_selected():
    """
    Play the song currently selected in the listbox.
    If none is selected:
      - if no song played yet, play the first,
      - else, replay the current song.
    """
    if not playlist:
        return

    selection = playlist_box.curselection()
    if not selection:
        if current_index == -1:
            # No song has been started; play the first
            play_song(0)
        else:
            # Replay the current song
            play_song(current_index)
        return

    index = selection[0]
    play_song(index)


def play_next():
    """
    Play the next song in the playlist.
    Wraps around to the first song at the end.
    """
    if not playlist:
        return

    next_index = (current_index + 1) % len(playlist)

    # Update the selection in the listbox
    playlist_box.selection_clear(0, tk.END)
    playlist_box.selection_set(next_index)
    playlist_box.activate(next_index)

    play_song(next_index)


def play_prev():
    """
    Play the previous song in the playlist.
    Wraps around to the last song when going backwards from the first.
    """
    if not playlist:
        return

    prev_index = (current_index - 1) % len(playlist)

    # Update the selection in the listbox
    playlist_box.selection_clear(0, tk.END)
    playlist_box.selection_set(prev_index)
    playlist_box.activate(prev_index)

    play_song(prev_index)


def toggle_pause():
    """
    Toggle between pause and resume.
    Also updates the song label icon ▶ / ⏸.
    """
    global paused

    # If nothing is loaded, ignore
    if not playlist or current_index == -1:
        return

    if paused:
        # Resume playback
        pygame.mixer.music.unpause()
        paused = False
        song_label.configure(
            text=f"▶ {os.path.basename(playlist[current_index])}"
        )
    else:
        # Pause playback
        pygame.mixer.music.pause()
        paused = True
        song_label.configure(
            text=f"⏸ {os.path.basename(playlist[current_index])}"
        )


def stop_song():
    """
    Stop playback completely, reset timer and slider to zero.
    """
    global paused, seek_base_seconds, current_total_seconds

    pygame.mixer.music.stop()
    paused = False

    # Reset time tracking
    seek_base_seconds = 0
    current_total_seconds = 0

    progress_label.configure(text="00:00 / --:--")
    position_slider.set(0)


def set_volume(value):
    """
    Set pygame mixer volume.
    `value` is a string or float between 0 and 100 from the slider.
    """
    vol = float(value) / 100.0
    pygame.mixer.music.set_volume(vol)


# ------------------- POSITION SLIDER (SEEK) -------------------

def on_slider_press(event):
    """
    Called when user clicks on the position slider.
    We set is_dragging_slider=True so the update loop does not override the slider.
    """
    global is_dragging_slider
    is_dragging_slider = True


def on_slider_release(event):
    """
    Called when user releases the position slider.
    We set is_dragging_slider=False and then seek to the new position.
    """
    global is_dragging_slider
    is_dragging_slider = False

    # Get the slider's current value (seconds) and seek
    seek_to(position_slider.get())


def seek_to(position_seconds: float):
    """
    Try to jump to a specific time in the current song (in seconds).
    Also updates seek_base_seconds so the timer remains consistent.

    Note: pygame.mixer.music.play(start=...) does not support all formats
    perfectly; for some audio types it may be approximate or unsupported.
    """
    global paused, seek_base_seconds

    # If no song is loaded, do nothing
    if current_index == -1:
        return

    # If we know the total length, clamp the target position within range
    if current_total_seconds > 0:
        position_seconds = max(0, min(position_seconds, current_total_seconds))

    try:
        # Remember where we started after this seek
        seek_base_seconds = int(position_seconds)

        # Start playing from this position. This also resets get_pos() back to 0,
        # which is why we add seek_base_seconds in the update loop.
        pygame.mixer.music.play(start=float(position_seconds))
        paused = False

    except Exception:
        messagebox.showinfo(
            "Seek not supported",
            "Seeking may not work for this audio format."
        )


# ------------------- UI UPDATE LOOP -------------------

def update_status_loop():
    """
    Periodically called function (every 500 ms) that:
    - updates the current time label
    - moves the slider if user is not dragging it
    - moves to next/looped song when one finishes
    """
    global seek_base_seconds

    if pygame.mixer.music.get_busy():
        # get_pos() returns milliseconds since last play()/unpause()
        ms = pygame.mixer.music.get_pos()
        if ms >= 0:
            # Relative seconds since last start
            rel_seconds = ms // 1000

            # Absolute position inside song:
            # base offset (from seeks) + relative time from current play()
            seconds = seek_base_seconds + rel_seconds

            # If we know total duration, clamp so it doesn't overflow
            if current_total_seconds > 0 and seconds > current_total_seconds:
                seconds = current_total_seconds

            # Convert current position to mm:ss
            m = seconds // 60
            s = seconds % 60

            if current_total_seconds > 0:
                # If total length known, show mm:ss / MM:SS
                tm = current_total_seconds // 60
                ts = current_total_seconds % 60
                progress_label.configure(
                    text=f"{m:02d}:{s:02d} / {tm:02d}:{ts:02d}"
                )
            else:
                # Otherwise show mm:ss / --:--
                progress_label.configure(
                    text=f"{m:02d}:{s:02d} / --:--"
                )

            # Update slider position if user is NOT dragging it
            if not is_dragging_slider:
                try:
                    position_slider.set(seconds)
                except tk.TclError:
                    # Can happen if widget is destroyed while updating
                    pass

    else:
        # If mixer is not busy (no song playing) and we didn't stop it manually,
        # that usually means song finished.
        if not paused and current_index != -1:
            if loop_current.get():
                # Replay the same song
                play_song(current_index)
            else:
                # Auto-advance to next song
                play_next()

    # Schedule this function to be called again after 500 milliseconds
    root.after(500, update_status_loop)


# ------------------- BUILD MODERN UI (CUSTOMTKINTER) -------------------

def build_ui():
    """
    Build the whole CustomTkinter UI: frames, labels, sliders, buttons, etc.
    Also sets global references to the created widgets.
    """
    global root, loop_current
    global playlist_box, song_label, progress_label
    global volume_slider, position_slider

    # Set appearance and color theme for CustomTkinter
    ctk.set_appearance_mode("dark")       # "dark" or "light"
    ctk.set_default_color_theme("blue")   # "blue", "green", "dark-blue"

    # Main window
    root = ctk.CTk()
    root.title("🎵 Modern Music Player (Audio Only)")
    root.geometry("900x480")

    # Tkinter BooleanVar to control "Loop current song" checkbox
    loop_current = ctk.BooleanVar(value=False)

    # ---------- Top bar (title + open folder button) ----------
    top_frame = ctk.CTkFrame(root)
    top_frame.pack(fill="x", padx=10, pady=(10, 5))

    title_label = ctk.CTkLabel(
        top_frame,
        text="Modern Music Player",
        font=("Segoe UI", 18, "bold")
    )
    title_label.pack(side="left")

    folder_button = ctk.CTkButton(
        top_frame,
        text="Open Folder",
        fg_color="#ff9800",     # orange color
        hover_color="#ffa733",
        command=load_folder
    )
    folder_button.pack(side="right")

    # ---------- Middle area: left "cover" box, right playlist ----------
    middle_frame = ctk.CTkFrame(root)
    middle_frame.pack(fill="both", expand=True, padx=10, pady=5)

    # Fake album-art area (just a big music note for now)
    cover_frame = ctk.CTkFrame(middle_frame, width=300, height=260)
    cover_frame.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)
    # Prevent frame from shrinking to fit its children
    cover_frame.pack_propagate(False)

    cover_label = ctk.CTkLabel(
        cover_frame,
        text="♪",                 # big music note
        font=("Segoe UI", 48, "bold"),
        justify="center"
    )
    cover_label.pack(expand=True)

    # Playlist frame (on the right)
    playlist_frame = ctk.CTkFrame(middle_frame, width=300)
    playlist_frame.pack(side="right", fill="y", pady=10)
    playlist_frame.pack_propagate(False)

    # Regular Tk Listbox inside CTk frame for song list
    playlist_box_widget = tk.Listbox(
        playlist_frame,
        bg="#181818",
        fg="#FFFFFF",
        selectbackground="#1DB954",  # green highlight
        selectforeground="#000000",
        activestyle="none",
        highlightthickness=0,
        relief="flat",
        font=("Segoe UI", 11)
    )
    playlist_box_widget.pack(side="left", fill="both", expand=True)

    # Scrollbar for playlist
    scroll = ctk.CTkScrollbar(
        playlist_frame,
        command=playlist_box_widget.yview
    )
    scroll.pack(side="right", fill="y")
    playlist_box_widget.config(yscrollcommand=scroll.set)

    # ---------- Info labels (song name + progress) ----------
    info_frame = ctk.CTkFrame(root)
    info_frame.pack(fill="x", padx=10, pady=(5, 0))

    song_label_widget = ctk.CTkLabel(
        info_frame,
        text="No song loaded",
        font=("Segoe UI", 12)
    )
    song_label_widget.pack(anchor="w")

    progress_label_widget = ctk.CTkLabel(
        info_frame,
        text="00:00 / --:--",
        font=("Segoe UI", 11)
    )
    progress_label_widget.pack(anchor="w")

    # ---------- Position slider (timeline) ----------
    slider_frame = ctk.CTkFrame(root)
    slider_frame.pack(fill="x", padx=10, pady=5)

    position_slider_widget = ctk.CTkSlider(
        slider_frame,
        from_=0,
        to=ESTIMATED_MAX_SECONDS
    )
    position_slider_widget.pack(fill="x")

    # Bind mouse events for seeking
    position_slider_widget.bind("<Button-1>", on_slider_press)
    position_slider_widget.bind("<ButtonRelease-1>", on_slider_release)

    # ---------- Playback controls (Prev / Play / Pause / Next / Stop) ----------
    controls_frame = ctk.CTkFrame(root)
    controls_frame.pack(pady=10)

    prev_btn = ctk.CTkButton(
        controls_frame,
        text="⏮ Prev",
        width=80,
        command=play_prev
    )
    prev_btn.grid(row=0, column=0, padx=5)

    play_btn = ctk.CTkButton(
        controls_frame,
        text="▶ Play",
        width=80,
        fg_color="#1DB954",      # Spotify green
        hover_color="#1ed760",
        command=play_selected
    )
    play_btn.grid(row=0, column=1, padx=5)

    pause_btn = ctk.CTkButton(
        controls_frame,
        text="⏯ Pause/Resume",
        width=120,
        fg_color="#3b82f6",      # blue
        hover_color="#60a5fa",
        command=toggle_pause
    )
    pause_btn.grid(row=0, column=2, padx=5)

    next_btn = ctk.CTkButton(
        controls_frame,
        text="⏭ Next",
        width=80,
        command=play_next
    )
    next_btn.grid(row=0, column=3, padx=5)

    stop_btn = ctk.CTkButton(
        controls_frame,
        text="⏹ Stop",
        width=80,
        fg_color="#f97316",      # orange
        hover_color="#fb923c",
        command=stop_song
    )
    stop_btn.grid(row=0, column=4, padx=5)

    # ---------- Loop current song checkbox ----------
    loop_check = ctk.CTkCheckBox(
        root,
        text="Loop current song",
        variable=loop_current
    )
    loop_check.pack()

    # ---------- Volume slider ----------
    vol_frame = ctk.CTkFrame(root)
    vol_frame.pack(fill="x", padx=10, pady=(5, 10))

    vol_label = ctk.CTkLabel(vol_frame, text="Volume")
    vol_label.pack(side="left")

    volume_slider_widget = ctk.CTkSlider(
        vol_frame,
        from_=0,
        to=100,
        command=set_volume
    )
    volume_slider_widget.set(70)  # default 70% volume
    volume_slider_widget.pack(side="left", fill="x", expand=True, padx=(10, 0))

    # Expose created widgets as global variables for use in other functions
    global playlist_box, song_label, progress_label, volume_slider, position_slider
    playlist_box = playlist_box_widget
    song_label = song_label_widget
    progress_label = progress_label_widget
    volume_slider = volume_slider_widget
    position_slider = position_slider_widget

    return root


# ------------------- MAIN ENTRY POINT -------------------

if __name__ == "__main__":
    # Initialize pygame mixer for audio playback
    pygame.mixer.init()

    # Build the UI and get the root window
    root = build_ui()

    # Start the periodic status update loop
    update_status_loop()

    # Run the Tkinter event loop (blocks until window is closed)
    root.mainloop()
