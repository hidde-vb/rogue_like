from dataclasses import dataclass

import tcod.console
import tcod.event


@dataclass
class GameState:
    player_x: int = 0
    player_y: int = 0

    def on_draw(self, console: tcod.console.Console) -> None:
        console.print(self.player_x, self.player_y, "@")

    def on_event(self, event: tcod.event.Event) -> None:
        match event:
            case tcod.event.Quit():
                raise SystemExit
            case tcod.event.KeyDown(sym=tcod.event.KeySym.UP):
                self.player_y -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT):
                self.player_x += 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN):
                self.player_y += 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT):
                self.player_x -= 1
