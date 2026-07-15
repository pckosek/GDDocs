# 6.4.2 Creating a TileSet

## Classification

**Type:** Engineering Technique

**Category:** TileMapLayer

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Our TileMapLayer is ready.

Unfortunately...

...it has nothing to place.

Before we can paint a world, we need a collection of reusable tiles.

That collection is called a **TileSet**.

A TileSet stores every tile that can appear in a TileMapLayer.

Without one...

...the TileMapLayer has nothing to build with.

---

# Why This Matters

A TileSet acts like a library of building blocks.

Instead of repeatedly importing the same artwork...

...we import it once.

Then we define:

- individual tiles
- collision shapes
- terrain rules
- navigation information

Every TileMapLayer using that TileSet can reuse those definitions.

This keeps projects organized and consistent.

---

# Starter Workflow

Create a new:

```text
TileMapLayer
```

Select the **Tile Set** property.

Choose:

```text
New TileSet
```

Next:

1. Open the TileSet editor.
2. Add your tile texture.
3. Define the tile grid.
4. Create the individual tiles.

Once complete...

the TileMapLayer now has tiles available for painting.

---

# Dissecting the Workflow

Notice the relationship.

```text
Texture

↓

TileSet

↓

TileMapLayer

↓

World
```

Each step has a different responsibility.

The texture contains artwork.

The TileSet defines reusable tiles.

The TileMapLayer arranges those tiles into a level.

Separating these stages makes the system flexible and reusable.

---

# Design Principle

## Define once.

Reuse everywhere.

A TileSet centralizes information about every tile.

Rather than configuring each tile every time it appears...

...we define it once.

Every instance automatically shares those properties.

---

# Practical Observation

A TileSet stores much more than graphics.

Each tile may contain:

- collision shapes
- terrain information
- navigation polygons
- physics layers
- custom data

The TileSet becomes the authoritative description of every tile in your project.

The TileMapLayer simply references those definitions.

---

# Common Misconceptions

### "A TileSet is the level."

No.

The TileSet describes the available tiles.

The TileMapLayer decides where those tiles appear.

---

### "The texture is the TileSet."

Not exactly.

The texture provides artwork.

The TileSet organizes that artwork into usable tiles.

---

### "Every TileMapLayer needs its own TileSet."

Usually not.

Many TileMapLayers share the same TileSet.

This keeps worlds consistent and much easier to maintain.

---

### "The TileSet only stores graphics."

No.

It stores gameplay information as well.

Collision, terrain behavior, navigation, and other properties all belong inside the TileSet.

---

# Reflection

Imagine changing one tile inside your TileSet.

How many places in the world might update automatically?

Why is this preferable to editing every tile individually?

Now ask yourself:

Which information belongs in the TileSet...

...and which belongs in the TileMapLayer?

---

# Looking Ahead

Our TileSet now contains reusable tiles.

The next step is building a world.

How can we efficiently place those tiles to construct:

- platforms
- walls
- terrain
- decorations

We'll begin by exploring the tools used to paint TileMapLayers.