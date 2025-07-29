import attrs

from game.tile_types import Tile, wall

type TileMap = list[list[Tile]]


@attrs.define()
class WorldMap:
    """A world map for the game."""

    width: int
    height: int
    tiles: TileMap = attrs.field(init=False)

    def __attrs_post_init__(self):
        """Initialize the world map with default tiles."""
        self.tiles = [[wall for _ in range(self.width)] for _ in range(self.height)]

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height
