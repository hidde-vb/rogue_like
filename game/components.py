from typing import Final, Self

import attrs
import tcod.ecs.callbacks
from tcod.ecs import Entity


@attrs.define(frozen=True)
class Position:
    """The position of an entity."""

    x: int
    y: int

    def __add__(self, direction: tuple[int, int]) -> Self:
        """Add a direction to the current position."""
        return self.__class__(self.x + direction[0], self.y + direction[1])


@tcod.ecs.callbacks.register_component_changed(component=Position)
def on_position_changed(
    entity: Entity, old: Position | None, new: Position | None
) -> None:
    """Mirror position components as a tag."""
    if old == new:
        return
    if old is not None:
        entity.tags.discard(old)
    if new is not None:
        entity.tags.add(new)


@attrs.define(frozen=True)
class Graphic:
    """The icon and color of an entity."""

    ch: int = ord("!")
    fg: tuple[int, int, int] = (255, 255, 255)


Gold: Final = ("Gold", int)
"""Amount of gold carried by an entity."""
