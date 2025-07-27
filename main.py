from __future__ import annotations

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset
import g
from game.game_state import GameState


def main() -> None:
    screen_width = 80
    screen_height = 50

    console = tcod.console.Console(screen_width, screen_height, order="F")
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png",
        columns=32,
        rows=8,
        charmap=tcod.tileset.CHARMAP_TCOD,
    )

    state = GameState()

    with tcod.context.new(
        console=console, tileset=tileset, title="rogue_like", vsync=True
    ) as g.context:
        while True:
            console.clear()
            state.on_draw(console)
            g.context.present(console)

            for event in tcod.event.wait():
                print(event)
                state.on_event(event)


if __name__ == "__main__":
    main()
