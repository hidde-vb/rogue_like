from __future__ import annotations

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

import g
import game.states
import game.world_tools


def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png",
        columns=32,
        rows=8,
        charmap=tcod.tileset.CHARMAP_TCOD,
    )

    console = tcod.console.Console(screen_width, screen_height)
    state = game.states.InGame()
    g.world = game.world_tools.new_world()

    with tcod.context.new(
        console=console, tileset=tileset, title="rogue_like", vsync=True
    ) as g.context:
        while True:
            console.clear()
            state.on_draw(console)
            g.context.present(console)

            for event in tcod.event.wait():
                state.on_event(event)


if __name__ == "__main__":
    main()
