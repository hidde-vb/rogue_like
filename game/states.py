import attrs
import tcod.console
import tcod.event

import g
from game.components import Gold, Graphic, Position
from game.constants import DIRECTION_KEYS
from game.tags import isPlayer


@attrs.define()
class InGame:
    """Primary in-game state."""

    def on_draw(self, console: tcod.console.Console) -> None:
        """Draw the game state to the console."""

        for entity in g.world.Q.all_of(components=[Position, Graphic]):
            pos = entity.components[Position]
            if not (0 <= pos.x < console.width and 0 <= pos.y < console.height):
                continue
            graphic = entity.components[Graphic]
            console.rgb[["ch", "fg"]][pos.x, pos.y] = graphic.ch, graphic.fg

        if text := g.world[None].components.get(("Text", str)):
            console.print(x=0, y=console.height - 1, text=text)

    def on_event(self, event: tcod.event.Event) -> None:
        """Handle events in the game state."""

        (player,) = g.world.Q.all_of(tags=[isPlayer])
        match event:
            case tcod.event.Quit():
                raise SystemExit
            case tcod.event.KeyDown(sym=sym) if sym in DIRECTION_KEYS:
                print(player)
                player.components[Position] += DIRECTION_KEYS[sym]

                # pick up gold
                for gold in g.world.Q.all_of(
                    components=[Gold], tags=[player.components[Position]]
                ):
                    player.components[Gold] += gold.components[Gold]
                    text = f"Picked up {gold.components[Gold]}g, total {player.components[Gold]}g"
                    g.world[None].components[("Text", str)] = text
                    gold.clear()
