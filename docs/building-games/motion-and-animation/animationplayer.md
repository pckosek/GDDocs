# 6.3.3 AnimationPlayer

## Classification

**Type:** Engineering Technique

**Category:** Visual Representation

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

AnimatedSprite2D makes it easy to play sequences of images.

That works well for characters drawn using sprite sheets.

But what if we want to animate something else?

For example:

- a door opening
- a collectible spinning
- a platform moving
- a camera zooming
- a light fading
- a sprite scaling
- a UI panel appearing

These are not changes to the artwork.

They are changes to an object's **properties**.

Godot provides **AnimationPlayer** for this purpose.

---

# Why This Matters

AnimationPlayer allows us to animate almost any property in a scene.

Examples include:

- position
- rotation
- scale
- color
- transparency
- shader values
- visibility

Instead of writing code to change those values every frame...

...we describe the animation once.

Godot plays it automatically.

---

# Starter Implementation

Suppose we have a door.

```text
Door

├── Sprite2D
├── CollisionShape2D
└── AnimationPlayer
```

Create an animation named:

```text
Open
```

Animate the door's rotation.

Later, from code:

```gdscript
$AnimationPlayer.play("Open")
```

The door rotates automatically.

No movement code is required.

---

# Dissecting the Node

Notice the difference.

AnimatedSprite2D changes:

```text
Which image is displayed.
```

AnimationPlayer changes:

```text
How properties change over time.
```

For example:

```text
Rotation

0°

↓

90°
```

Or:

```text
Scale

1.0

↓

1.5
```

The node is not limited to artwork.

It animates properties throughout the scene.

---

# Design Principle

## Animate behavior, not just images.

Animation is not limited to sprite frames.

Many gameplay objects become more expressive when their properties change smoothly over time.

AnimationPlayer allows those changes to be designed visually rather than programmed manually.

---

# Comparison

| Node | Primary Responsibility |
|------|------------------------|
| Sprite2D | Display one image |
| AnimatedSprite2D | Display changing sprite frames |
| AnimationPlayer | Animate properties over time |

Notice that these nodes solve different visual problems.

Many games use all three together.

---

# Practical Observation

AnimationPlayer often becomes the preferred tool when:

- multiple properties change together
- precise timing matters
- artists and designers need to edit animations visually
- animations affect more than just sprites

For example, opening a treasure chest might animate:

- rotation
- sound
- particles
- collision
- sprite visibility

All within one animation timeline.

---

# Common Misconceptions

### "AnimationPlayer replaces AnimatedSprite2D."

No.

They solve different problems.

AnimatedSprite2D changes artwork.

AnimationPlayer changes properties.

---

### "AnimationPlayer only works with sprites."

Not at all.

It can animate almost any property belonging to almost any node.

---

### "Every animation should use AnimationPlayer."

Not necessarily.

Simple frame-based character animation is often easier with AnimatedSprite2D.

AnimationPlayer becomes valuable when multiple properties need to change together.

---

### "AnimationPlayer contains gameplay."

Usually not.

The animation represents gameplay visually.

Your scripts still determine **when** animations should begin.

---

# Reflection

Suppose you are creating:

- a moving platform
- a treasure chest
- a fading light
- a boss introduction
- a menu transition

Would AnimatedSprite2D or AnimationPlayer be the better choice?

Why?

Can you identify which property is actually changing?

---

# Looking Ahead

So far we've chosen animations directly.

```gdscript
play("walk")

play("jump")

play("idle")
```

As games become larger...

...this quickly becomes difficult to manage.

The next challenge is allowing animations to respond automatically to gameplay.

Instead of asking:

> **Which animation should I play?**

we'll begin asking:

> **What state is the object currently in?**