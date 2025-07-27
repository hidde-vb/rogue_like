from random import Random

from tcod.ecs import Registry

from game.components import Gold, Graphic, Position
from game.tags import isActor, isItem, isPlayer


def new_world() -> Registry:
    """Create a new game world."""
    world = Registry()
    rng = world[None].components[Random] = Random()

    player = world[object()]
    player.components[Position] = Position(5, 5)
    player.components[Graphic] = Graphic(ch=ord("@"))
    player.components[Gold] = 0
    player.tags |= {isPlayer, isActor}

    for _ in range(10):
        x = rng.randint(0, 20)
        y = rng.randint(0, 20)
        gold = world[object()]
        gold.components[Position] = Position(x, y)
        gold.components[Graphic] = Graphic(ch=ord("$"), fg=(255, 255, 0))
        gold.components[Gold] = rng.randint(1, 10)
        gold.tags.add(isItem)

    return world
