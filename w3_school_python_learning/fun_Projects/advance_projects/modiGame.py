
import pygame
import sys
import os

# ----------------- AUDIO INIT (helps on macOS too) -----------------
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()

# ----------------- BASE DIR FOR ALL ASSETS -----------------
# This makes all paths relative to *this file's* folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def asset_path(filename: str) -> str:
    """Return absolute path for a file that lives next to this script."""
    return os.path.join(BASE_DIR, filename)

# ----------------- CONFIG: change file names only here -----------------
# Just names, not full paths
PLAYER_IMAGE_PATH = "modi_walking.png"        # main character
ENEMY_IMAGE_PATH = "rahul_gandhi.png"        # enemy
VICTORY_IMAGE_PATH = "hero_win.png"   # big image on victory

BACKGROUND_MUSIC_PATH = "bg_song.mp3" # overall background music (looped)
DEATH_SOUND_PATH = "khatam.mp3"         # when enemy touches player
VICTORY_SOUND_PATH = "win.mp3"        # when player reaches flag
JUMP_SOUND_PATH = "jump.mp3"      # sound when player jumps  <-- NEW

# ----------------- BASIC SETUP -----------------
WIDTH, HEIGHT = 900, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Platformer with Images & Music")

CLOCK = pygame.time.Clock()
FPS = 60

# Colors
SKY_BLUE = (135, 206, 235)
GREEN    = (46, 204, 113)
RED      = (231, 76, 60)
WHITE    = (255, 255, 255)
BROWN    = (139, 69, 19)
YELLOW   = (241, 196, 15)
BLACK    = (0, 0, 0)

font = pygame.font.SysFont("arial", 24)

# ----------------- SAFE ASSET LOADING -----------------
def load_image(rel_path, size=None):
    """Load an image using path relative to this file."""
    full = asset_path(rel_path)
    if not os.path.exists(full):
        print(f"[WARN] Image not found: {full}")
        return None
    try:
        img = pygame.image.load(full).convert_alpha()
        if size:
            img = pygame.transform.smoothscale(img, size)
        return img
    except Exception as e:
        print(f"[WARN] Failed to load image {full}: {e}")
        return None

def load_sound(rel_path):
    """Load a sound effect using path relative to this file."""
    full = asset_path(rel_path)
    if not os.path.exists(full):
        print(f"[WARN] Sound not found: {full}")
        return None
    try:
        return pygame.mixer.Sound(full)
    except Exception as e:
        print(f"[WARN] Failed to load sound {full}: {e}")
        return None

# ----------------- LOAD ASSETS -----------------
player_sprite      = load_image(PLAYER_IMAGE_PATH, (40, 50))
enemy_sprite       = load_image(ENEMY_IMAGE_PATH, (40, 40))
victory_image_raw  = load_image(VICTORY_IMAGE_PATH)

death_sound        = load_sound(DEATH_SOUND_PATH)
victory_sound      = load_sound(VICTORY_SOUND_PATH)
jump_sound         = load_sound(JUMP_SOUND_PATH)   # <-- NEW

# Background music: turn relative name into absolute once
if BACKGROUND_MUSIC_PATH:
    full_bg = asset_path(BACKGROUND_MUSIC_PATH)
    if os.path.exists(full_bg):
        BACKGROUND_MUSIC_PATH = full_bg
    else:
        print(f"[WARN] Background music not found: {full_bg}")
        BACKGROUND_MUSIC_PATH = None

# ----------------- PLAYER & ENEMY STATE -----------------
player = {
    "x": 50,
    "y": HEIGHT - 100,
    "vx": 0,
    "vy": 0,
    "w": 40,
    "h": 50,
    "on_ground": False,
}

MOVE_SPEED      = 5
JUMP_POWER      = -14
GRAVITY         = 0.7
MAX_FALL_SPEED  = 15

enemy = {
    "x": 350,
    "y": HEIGHT - 80,
    "w": 40,
    "h": 40,
    "vx": 2,
    "min_x": 300,
    "max_x": 650,
}

platforms = [
    pygame.Rect(0, HEIGHT - 40, WIDTH, 40),        # ground
    pygame.Rect(150, HEIGHT - 120, 120, 20),
    pygame.Rect(330, HEIGHT - 190, 120, 20),
    pygame.Rect(520, HEIGHT - 260, 120, 20),
    pygame.Rect(700, HEIGHT - 330, 130, 20),
]

goal = pygame.Rect(WIDTH - 80, HEIGHT - 160, 40, 120)

# ----------------- GAME STATE -----------------
STATE_PLAYING = "playing"
STATE_DEAD    = "dead"
STATE_WIN     = "win"

game_state = STATE_PLAYING
death_sound_played    = False
victory_sound_played  = False

# ----------------- HELPERS -----------------
def reset_player_and_enemy():
    """Reset positions and state, restart background music."""
    global game_state, death_sound_played, victory_sound_played

    player["x"] = 50
    player["y"] = HEIGHT - 100
    player["vx"] = 0
    player["vy"] = 0
    player["on_ground"] = False

    enemy["x"] = 350
    enemy["y"] = HEIGHT - 80
    enemy["vx"] = 2

    game_state = STATE_PLAYING
    death_sound_played   = False
    victory_sound_played = False

    if BACKGROUND_MUSIC_PATH:
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(BACKGROUND_MUSIC_PATH)
            pygame.mixer.music.play(-1)  # loop forever
        except Exception as e:
            print(f"[WARN] Could not play bg music {BACKGROUND_MUSIC_PATH}: {e}")

def get_player_rect():
    return pygame.Rect(player["x"], player["y"], player["w"], player["h"])

def get_enemy_rect():
    return pygame.Rect(enemy["x"], enemy["y"], enemy["w"], enemy["h"])

# ----------------- INPUT & PHYSICS -----------------
def handle_input():
    keys = pygame.key.get_pressed()

    player["vx"] = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player["vx"] = -MOVE_SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player["vx"] = MOVE_SPEED

    # Jump only if on ground
    if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and player["on_ground"]:
        player["vy"] = JUMP_POWER
        player["on_ground"] = False
        # Play jump sound
        if jump_sound:
            jump_sound.play()

def move_enemy():
    enemy["x"] += enemy["vx"]
    if enemy["x"] < enemy["min_x"]:
        enemy["x"] = enemy["min_x"]
        enemy["vx"] *= -1
    if enemy["x"] + enemy["w"] > enemy["max_x"]:
        enemy["x"] = enemy["max_x"] - enemy["w"]
        enemy["vx"] *= -1

def apply_physics():
    player["vy"] += GRAVITY
    if player["vy"] > MAX_FALL_SPEED:
        player["vy"] = MAX_FALL_SPEED

    player["on_ground"] = False

    # Horizontal
    player["x"] += player["vx"]
    rect = get_player_rect()
    for plat in platforms:
        if rect.colliderect(plat):
            if player["vx"] > 0:
                player["x"] = plat.left - player["w"]
            elif player["vx"] < 0:
                player["x"] = plat.right
            rect = get_player_rect()

    # Vertical
    player["y"] += player["vy"]
    rect = get_player_rect()
    for plat in platforms:
        if rect.colliderect(plat):
            if player["vy"] > 0:
                player["y"] = plat.top - player["h"]
                player["vy"] = 0
                player["on_ground"] = True
            elif player["vy"] < 0:
                player["y"] = plat.bottom
                player["vy"] = 0
            rect = get_player_rect()

    if player["y"] > HEIGHT + 200:
        trigger_death()

# ----------------- GAME STATE CHANGES -----------------
def trigger_death():
    global game_state, death_sound_played
    if game_state != STATE_PLAYING:
        return
    game_state = STATE_DEAD

    if BACKGROUND_MUSIC_PATH:
        pygame.mixer.music.stop()
    if death_sound and not death_sound_played:
        death_sound_played = True
        death_sound.play()

def trigger_victory():
    global game_state, victory_sound_played
    if game_state != STATE_PLAYING:
        return
    game_state = STATE_WIN

    if BACKGROUND_MUSIC_PATH:
        pygame.mixer.music.stop()
    if victory_sound and not victory_sound_played:
        victory_sound_played = True
        victory_sound.play()

# ----------------- DRAWING -----------------
def draw():
    SCREEN.fill(SKY_BLUE)

    for plat in platforms:
        pygame.draw.rect(SCREEN, BROWN, plat)

    pygame.draw.rect(SCREEN, YELLOW, goal)
    pygame.draw.polygon(
        SCREEN,
        RED,
        [
            (goal.right, goal.top),
            (goal.right + 30, goal.top + 15),
            (goal.right, goal.top + 30),
        ],
    )

    enemy_rect = get_enemy_rect()
    if enemy_sprite:
        SCREEN.blit(enemy_sprite, (enemy["x"], enemy["y"]))
    else:
        pygame.draw.rect(SCREEN, GREEN, enemy_rect)

    player_rect = get_player_rect()
    if player_sprite:
        SCREEN.blit(player_sprite, (player["x"], player["y"]))
    else:
        pygame.draw.rect(SCREEN, RED, player_rect)

    info_text = "←/→ or A/D to move, Space/↑ to jump, R to restart"
    text_surf = font.render(info_text, True, BLACK)
    SCREEN.blit(text_surf, (20, 10))

    if game_state == STATE_DEAD:
        msg = "You died! Press R to restart."
        msg_surf = font.render(msg, True, WHITE)
        SCREEN.blit(
            msg_surf,
            (WIDTH // 2 - msg_surf.get_width() // 2,
             HEIGHT // 2 - msg_surf.get_height() // 2),
        )

    if game_state == STATE_WIN:
        msg = "You reached the flag! Press R to play again."
        msg_surf = font.render(msg, True, WHITE)
        SCREEN.blit(
            msg_surf,
            (WIDTH // 2 - msg_surf.get_width() // 2,
             40),
        )
        if victory_image_raw:
            scale_factor = (HEIGHT // 2) / victory_image_raw.get_height()
            new_w = int(victory_image_raw.get_width() * scale_factor)
            new_h = int(victory_image_raw.get_height() * scale_factor)
            victory_image = pygame.transform.smoothscale(
                victory_image_raw, (new_w, new_h)
            )
            x = WIDTH // 2 - new_w // 2
            y = HEIGHT // 2 - new_h // 2 + 40
            SCREEN.blit(victory_image, (x, y))

    pygame.display.flip()

# ----------------- MAIN LOOP -----------------
def main():
    global game_state

    while True:
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            reset_player_and_enemy()

        if game_state == STATE_PLAYING:
            handle_input()
            move_enemy()
            apply_physics()
            if get_player_rect().colliderect(get_enemy_rect()):
                trigger_death()
            if get_player_rect().colliderect(goal):
                trigger_victory()

        draw()

# ----------------- ENTRY POINT -----------------
if __name__ == "__main__":
    reset_player_and_enemy()
    main()
