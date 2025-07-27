import tcod.context
import tcod.ecs

context: tcod.context.Context
"""The window managed by tcod."""

world: tcod.ecs.Registry
"""The active ECS registry and current session."""
