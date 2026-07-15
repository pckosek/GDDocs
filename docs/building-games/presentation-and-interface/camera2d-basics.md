# 6.6.1 Camera2D

## Classification

**Type:** Engineering Technique

**Category:** World Presentation

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine building a platformer level that stretches hundreds of tiles.

When the game begins...

...the player can only see a small part of that world.

As the player moves...

what should happen?

Should the character walk off the edge of the screen?

Should the entire level always remain visible?

Neither usually creates a satisfying experience.

Instead...

the camera becomes the player's window into the world.

Godot provides **Camera2D** to control that window.

---

# Why This Matters

Camera2D determines **what the player sees**.

It does not change the world.

It changes the player's view of the world.

Most 2D games use a camera to:

- follow the player
- limit the visible area
- frame important gameplay
- guide the player's attention

Without a camera...

large levels become difficult to navigate and understand.

---

# Starter Implementation

A common player scene looks like this.

```text
Player (CharacterBody2D)

├── CollisionShape2D
├── AnimatedSprite2D
└── Camera2D
```

Select the Camera2D node.

Enable:

```text
Enabled
```

When the game begins...

the camera becomes active.

If the Camera2D is a child of the player...

it naturally follows the player's movement.

---

# Dissecting the Node

Notice what moves.

```text
Player

↓

Camera

↓

View
```

The camera is not moving the player.

The player is moving normally.

The camera simply changes which part of the world is visible.

The world itself never changes.

Only the player's viewpoint changes.

---

# Design Principle

## Separate the world from the view.

The level exists independently of the camera.

The camera decides which part of that level the player currently sees.

This separation allows one world to be presented in many different ways.

---

# Practical Observation

A Camera2D usually belongs to the player.

As the player moves...

the camera follows automatically.

This creates a simple and reliable relationship.

```text
Player

↓

Camera

↓

Screen
```

Other gameplay systems continue using world coordinates.

Only the presentation changes.

---

# Common Misconceptions

### "The camera moves the player."

No.

The player moves independently.

The camera follows the player.

---

### "The world moves."

Not really.

The world remains fixed.

The camera changes the visible portion of the world.

---

### "Every scene needs a Camera2D."

Not necessarily.

Small games may fit entirely within one screen.

Camera2D becomes valuable whenever the world is larger than the visible window.

---

### "Only one Camera2D can exist."

Many games contain several cameras.

Only one is usually active at a time.

Different cameras may be used for gameplay, menus, cutscenes, or special effects.

---

# Reflection

Imagine the following games.

Would they benefit from a Camera2D?

| Game | Camera? |
|------|----------|
| One-Screen Puzzle Game | |
| Platformer | |
| Large Top-Down Adventure | |
| Endless Runner | |
| Side-Scrolling Shooter | |

Now ask yourself:

Why shouldn't the player always see the entire world?

---

# Looking Back

Earlier we built:

- movement
- animation
- TileMaps
- gameplay objects

Now we've discovered another important idea.

The player does not experience the entire world at once.

They experience the portion presented by the camera.

The camera becomes another gameplay system.

Not because it changes the world...

...but because it changes how the player experiences it.

---

# Looking Ahead

A Camera2D can follow the player automatically.

Sometimes, however...

following the player exactly is not the best experience.

How should the camera behave?

Should it:

- stay centred?
- look ahead?
- move smoothly?

The next lesson explores one of the most important design questions in 2D games:

> **Following the Player**