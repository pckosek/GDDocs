# 6.6.4 Parallax

## Classification

**Type:** Engineering Technique

**Category:** World Presentation

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Our platformer now has:

- movement
- animation
- TileMaps
- a Camera2D

The world works.

But it still feels flat.

Everything moves at exactly the same speed.

The player struggles to judge depth and distance.

How can a completely two-dimensional game create the illusion of a much larger world?

One of the oldest and most effective techniques is **Parallax**.

---

# Why This Matters

Parallax creates the illusion that different parts of the world exist at different depths.

Objects that appear farther away move more slowly.

Objects that appear closer move more quickly.

Examples include:

- distant mountains
- clouds
- forests
- foreground trees
- cave walls

Although every object exists on a flat screen...

...the player experiences a much richer world.

---

# Mental Model

Imagine looking out the window of a moving car.

Nearby trees rush past.

Distant mountains barely seem to move.

```text
Near Objects

↓

Move Quickly

-----------------------

Far Objects

↓

Move Slowly
```

The world itself has not changed.

Only your perspective has.

Parallax recreates this visual effect.

---

# Starter Implementation

Godot provides dedicated nodes for parallax.

A common scene might look like:

```text
Parallax2D

└── Sprite2D
```

or

```text
Parallax2D

└── TileMapLayer
```

Adjust the motion scale for the layer.

For example:

```text
Background

↓

0.2
```

```text
Foreground

↓

1.2
```

As the camera moves...

each layer scrolls at a different speed.

---

# Dissecting the Effect

Notice what changes.

The player moves normally.

The camera follows normally.

Only the background layers respond differently.

```text
Player

↓

Camera

↓

Parallax Layers

↓

Different Movement Speeds
```

The illusion of depth emerges naturally.

Nothing about the gameplay changes.

Only the presentation changes.

---

# Design Principle

## Use movement to communicate depth.

Parallax does not create real three-dimensional space.

It creates the **perception** of depth.

Carefully chosen movement speeds help the player experience a larger, more believable world.

Presentation shapes perception.

---

# Practical Observation

Not every layer should move equally.

A common arrangement might be:

| Layer | Relative Speed |
|--------|----------------|
| Sky | Very Slow |
| Mountains | Slow |
| Background Trees | Medium |
| Gameplay World | Normal |
| Foreground Plants | Slightly Faster |

Notice that the gameplay layer remains the reference point.

Everything else supports the illusion.

---

# Common Misconceptions

### "Parallax changes gameplay."

No.

Parallax changes only the presentation.

The player still moves through exactly the same world.

---

### "Every layer should move."

Not necessarily.

Some layers remain completely static.

Others move only slightly.

The appropriate movement depends on the intended visual effect.

---

### "Parallax creates 3D graphics."

No.

The world remains entirely two-dimensional.

Parallax simply creates a convincing illusion of depth.

---

### "More parallax is always better."

Not always.

Excessive movement can distract the player and make gameplay more difficult to read.

Subtle effects are often the most effective.

---

# Reflection

Imagine creating each of the following.

| Layer | Relative Speed |
|--------|----------------|
| Sky | |
| Clouds | |
| Mountains | |
| Trees | |
| Foreground Grass | |

Now ask yourself:

Which layers should appear closest to the player?

Which should feel distant?

How would you communicate that using movement?

---

# Looking Back

Earlier we learned that the Camera2D presents the world.

Parallax extends that idea.

The camera no longer presents every part of the world equally.

Different layers move differently.

The player experiences a world that feels much larger and deeper than the flat screen actually allows.

Good presentation often depends on carefully shaping perception rather than changing gameplay.

---

# Looking Ahead

The camera follows the player.

Parallax creates depth.

Sometimes, however...

the camera itself should respond to important gameplay events.

How can we communicate:

- impacts
- explosions
- damage
- dramatic moments

through the movement of the camera itself?

We'll explore one of the most expressive presentation techniques in game development:

> **Camera Feedback**