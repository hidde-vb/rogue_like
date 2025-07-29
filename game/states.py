import attrs
import tcod.console
import tcod.event

import g
from game.components import Gold, Graphic, Position
from game.constants import DIRECTION_KEYS
from game.tags import IsItem, IsPlayer
from game.world_map import WorldMap


@attrs.define()
class InGame:
    """Primary in-game state."""

    def on_draw(self, console: tcod.console.Console) -> None:
        """Draw the game state to the console."""

        # Draw the world map
        world_map = g.world[None].components.get(WorldMap)
        if world_map:
            for y in range(world_map.height):
                for x in range(world_map.width):
                    tile = world_map.tiles[y][x]
                    if tile is not None:
                        console.rgb[["ch", "fg", "bg"]][y, x] = (
                            tile.dark.ch,
                            tile.dark.fg,
                            tile.dark.bg,
                        )

        for entity in g.world.Q.all_of(components=[Position, Graphic]):
            pos = entity.components[Position]
            if not (0 <= pos.x < console.width and 0 <= pos.y < console.height):
                continue
            graphic = entity.components[Graphic]
            console.rgb[["ch", "fg"]][pos.y, pos.x] = graphic.ch, graphic.fg

        if text := g.world[None].components.get(("Text", str)):
            console.print(x=0, y=console.height - 1, text=text)

    def on_event(self, event: tcod.event.Event) -> None:
        """Handle events for the in-game state."""

        (player,) = g.world.Q.all_of(tags=[IsPlayer])
        match event:
            case tcod.event.Quit():
                raise SystemExit
            case tcod.event.KeyDown(sym=sym) if sym in DIRECTION_KEYS:
                pos = player.components[Position] + DIRECTION_KEYS[sym]
                tile = g.world[None].components.get(WorldMap).tiles[pos.y][pos.x]

                if tile and tile.walkable:
                    player.components[Position] = pos

                # Auto pickup gold
                for gold in g.world.Q.all_of(
                    components=[Gold], tags=[player.components[Position], IsItem]
                ):
                    player.components[Gold] += gold.components[Gold]
                    text = f"Picked up {gold.components[Gold]}g, total: {player.components[Gold]}g"
                    g.world[None].components[("Text", str)] = text
                    gold.clear()
