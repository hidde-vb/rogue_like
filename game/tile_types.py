import attrs

from game.components import Graphic
from game.constants import COLORS


@attrs.define(frozen=True)
class Tile:
    """A tile in the game world."""

    walkable: bool
    transparent: bool
    # Only dark right now, no FOV is implemented.
    dark: Graphic


floor = Tile(
    walkable=True,
    transparent=True,
    dark=Graphic(ch=ord("."), fg=COLORS["dark_gray"], bg=COLORS["black"]),
)

wall = Tile(
    walkable=False,
    transparent=False,
    dark=Graphic(ch=ord("#"), fg=COLORS["gray"], bg=COLORS["dark_gray"]),
)
