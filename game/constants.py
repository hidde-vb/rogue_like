from __future__ import annotations

from typing import Final

from tcod.event import KeySym

DIRECTION_KEYS: Final = {
    # Arrow keys
    KeySym.LEFT: (-1, 0),
    KeySym.RIGHT: (1, 0),
    KeySym.UP: (0, -1),
    KeySym.DOWN: (0, 1),
    # Arrow key diagonals
    KeySym.HOME: (-1, -1),
    KeySym.END: (-1, 1),
    KeySym.PAGEUP: (1, -1),
    KeySym.PAGEDOWN: (1, 1),
    # Keypad
    KeySym.KP_4: (-1, 0),
    KeySym.KP_6: (1, 0),
    KeySym.KP_8: (0, -1),
    KeySym.KP_2: (0, 1),
    KeySym.KP_7: (-1, -1),
    KeySym.KP_1: (-1, 1),
    KeySym.KP_9: (1, -1),
    KeySym.KP_3: (1, 1),
}

# Dawnbringer 16 colors
COLORS: Final = {
    "black": (20, 12, 28),
    "dark_gray": (78, 74, 78),
    "gray": (133, 149, 161),
    "light_gray": (117, 113, 97),
    "brown": (133, 76, 48),
    "dark_blue": (48, 52, 109),
    "light_blue": (89, 125, 206),
    "cyan": (109, 194, 202),
    "dark_red": (68, 36, 52),
    "light_red": (208, 70, 72),
    "orange": (210, 125, 44),
    "yellow": (218, 212, 94),
    "dark_green": (52, 101, 36),
    "light_green": (109, 170, 44),
    "peach": (210, 170, 153),
    "white": (222, 238, 214),
}
