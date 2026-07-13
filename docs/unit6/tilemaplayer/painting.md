# 6.4.3 Painting Tiles

## Classification

**Type:** Engineering Technique

**Category:** TileMapLayer

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Our TileSet now contains reusable tiles.

The next step is constructing the world.

How do we place those tiles into our level?

Rather than creating new sprites...

...we paint references to the tiles already stored in the TileSet.

This allows large environments to be built quickly while remaining easy to edit.

---

# Why This Matters

Painting is one of the primary workflows when building 2D worlds.

Examples include:

- ground
- walls
- platforms
- decorations
- backgrounds

Because every tile comes from the TileSet...

the level remains consistent and easy to modify.

Changing a tile in the TileSet automatically updates every location using that tile.

---

# Starter Workflow

Open the:

```text
TileMapLayer
```

Select a tile from the TileSet palette.

Then simply click inside the viewport.

```text
Select Tile

↓

Click Grid

↓

Tile Appears
```

Continue painting until the desired section of the world has been created.

---

Godot also provides several useful painting tools.

Examples include:

- Paint Brush
- Rectangle Tool
- Fill Tool
- Line Tool
- Eraser
- Tile Picker

These tools allow large sections of a level to be created much more quickly than placing tiles one at a time.

---

# Dissecting the Workflow

Notice that painting does **not** copy artwork.

Instead...

each grid location stores a reference.

```text
Grid Cell

↓

Tile ID
```

The TileSet provides the artwork.

The TileMapLayer simply records:

> **Which tile belongs here?**

Painting becomes another form of editing a representation.

---

# Design Principle

## Build worlds from reusable pieces.

Good level design rarely involves creating unique artwork for every location.

Instead...

reuse small, carefully designed tiles to construct much larger environments.

This allows levels to grow without increasing complexity.

---

# Practical Observation

Most level designers constantly switch between tools.

For example:

```text
Brush

↓

Rectangle

↓

Fill

↓

Eraser

↓

Tile Picker
```

Learning these workflows dramatically speeds up level construction.

Many beginning programmers spend far more time placing tiles than necessary simply because they are unaware of the available editing tools.

---

# Common Misconceptions

### "Painting creates new tiles."

No.

Painting places references to tiles that already exist inside the TileSet.

---

### "Every tile is independent."

Not necessarily.

Many locations reference exactly the same tile.

Editing the TileSet can therefore affect many places throughout the level.

---

### "The TileMapLayer stores artwork."

No.

It stores the arrangement of tile references.

The artwork remains inside the TileSet.

---

### "Painting is the only way to build TileMaps."

Not at all.

Later in this course we'll generate TileMaps automatically from code and even from procedural images.

Painting is one workflow.

It is not the only workflow.

---

# Reflection

Imagine building each of the following.

- a cave
- a castle
- a forest
- a village

Which painting tools would probably make the task easier?

When might you choose:

- Brush?
- Rectangle?
- Fill?
- Eraser?

Can you explain why?

---

# Looking Ahead

Painting individual tiles works well for small sections of a level.

Eventually, however...

painting every edge manually becomes tedious.

The next challenge is allowing neighboring tiles to automatically connect together.

We'll explore one of the most powerful TileMap features:

> **Terrain Sets and Auto-Tiling**