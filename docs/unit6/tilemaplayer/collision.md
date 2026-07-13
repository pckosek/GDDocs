# 6.4.5 Collision Tiles

## Classification

**Type:** Engineering Technique

**Category:** TileMapLayer

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Suppose we paint a beautiful platform.

The player walks toward it...

...and falls straight through.

The artwork is correct.

The TileMapLayer is correct.

So what went wrong?

The answer is simple.

The tile has no collision.

To the engine...

it is only a picture.

If we want tiles to become solid parts of the world...

we must define their collision shapes.

---

# Why This Matters

Collision tiles transform artwork into gameplay.

Without collision:

- platforms cannot be stood upon
- walls do not block movement
- floors cannot support the player

The TileSet controls not only what the player sees...

...but also how the player interacts with the world.

This is where appearance and gameplay begin working together.

---

# Starter Workflow

Open the:

```text
TileSet Editor
```

Select one tile.

Open the:

```text
Physics
```

section.

Create a new:

```text
Physics Layer
```

Then draw a collision shape inside the tile.

```text
Tile

↓

Collision Polygon

↓

Solid Platform
```

Repeat for any tiles that should block movement.

---

# Configure Physics Layers

Each physics layer inside the TileSet represents a different kind of collision.

For a simple platformer, one layer is often enough.

For example:

```text
Physics Layer 0

↓

World Collision
```

Every ground tile belongs to this layer.

Your player's CharacterBody2D should then be configured so that its **Collision Mask** detects this same physics layer.

Both sides of the interaction must agree.

```text
Tile

↓

Physics Layer 0

-------------------

Player

↓

Collision Mask

↓

Physics Layer 0
```

If these layers do not match...

the player will pass straight through the tiles.

---

# Dissecting the Workflow

Notice something important.

The artwork never changes.

```text
Grass Tile
```

remains

```text
Grass Tile
```

What changes is the information attached to it.

```text
Appearance

+

Collision Shape

+

Physics Layer

↓

Gameplay Tile
```

The TileSet now represents both:

- what the player sees
- how the player interacts

---

# Design Principle

## Appearance alone does not create gameplay.

A beautiful platform that cannot be stood upon is only decoration.

Gameplay emerges when visual representation is combined with interaction.

Tiles become part of the world when they describe both appearance **and** behavior.

---

# Practical Observation

Students often fix movement bugs by rewriting code.

Sometimes the movement code is perfectly correct.

The real problem is that the TileSet was never configured with:

- collision shapes
- physics layers

When debugging movement...

always inspect both:

- the player
- the world

Gameplay depends on both systems working together.

---

# Common Misconceptions

### "Painting a tile makes it solid."

No.

Painting only places the tile.

Collision must be defined inside the TileSet.

---

### "Every tile needs collision."

Not at all.

Many tiles are decorative.

Examples include:

- clouds
- background scenery
- distant mountains
- decorative plants

Only gameplay surfaces require collision.

---

### "The player collides with the artwork."

Not exactly.

The player collides with the collision shapes attached to the tiles.

The artwork is simply a visual representation.

---

### "Collision Layers and Physics Layers are the same thing."

They work together, but they are configured in different places.

- **The TileSet** defines which **Physics Layer** each collision shape belongs to.
- **The CharacterBody2D** uses its **Collision Mask** to decide which physics layers it should collide with.

Both must be configured correctly for collisions to occur.

---

# Reflection

Imagine the following tiles.

Which should probably have collision?

| Tile | Collision? |
|------|------------|
| Ground | |
| Brick Wall | |
| Cloud Decoration | |
| Tree Background | |
| Spike Platform | |
| Wooden Bridge | |

Now ask yourself:

Which objects exist purely for appearance...

...and which become part of the gameplay?

---

# Looking Back

Earlier we learned that TileMapLayers efficiently represent large worlds.

Now we've discovered that those worlds contain more than artwork.

Each tile may also describe:

- collision
- physics
- interaction

The same TileSet now supports both the visual world and the gameplay world.

---

# Looking Ahead

Our TileMap now has:

- artwork
- terrain rules
- collision

The next challenge is organizing increasingly complex worlds.

How can we separate:

- background
- gameplay
- foreground
- decoration

without creating confusion?

We'll explore one of the most useful organizational tools in 2D level design:

> **TileMap Layers**