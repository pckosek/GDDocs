# 6.3.2 AnimatedSprite2D

## Classification

**Type:** Engineering Technique

**Category:** Visual Representation

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

A single sprite can display one image.

That works well for:

- coins
- signs
- decorations
- static objects

Characters, however, rarely remain still.

A player:

- walks
- jumps
- falls
- attacks

Showing the same image continuously makes movement feel unnatural.

Instead, we display a sequence of images.

This creates the illusion of motion.

Godot provides **AnimatedSprite2D** for exactly this purpose.

---

# Why This Matters

AnimatedSprite2D allows one object to display different animations over time.

Common examples include:

- idle
- walk
- jump
- fall
- attack
- hurt
- death

Rather than manually replacing images every frame...

...the node manages the animation automatically.

This keeps gameplay code much simpler.

---

# Starter Implementation

A typical player scene might look like this.

```text
Player (CharacterBody2D)

├── CollisionShape2D
├── AnimatedSprite2D
└── Camera2D
```

Create a new **SpriteFrames** resource.

Add animations such as:

```text
Idle

Walk

Jump

Fall
```

Then, from code:

```gdscript
$AnimatedSprite2D.play("walk")
```

The node begins cycling through the frames of the **walk** animation.

---

# Dissecting the Node

Notice that:

```gdscript
play("walk")
```

does **not** move the player.

It changes only the visual representation.

Gameplay and animation remain separate systems.

The player moves because of:

```gdscript
velocity

move_and_slide()
```

The sprite changes because of:

```gdscript
play()
```

Each system has one responsibility.

---

# Design Principle

## Animation should communicate gameplay.

Animations exist to help the player understand what the character is doing.

The artwork should reflect gameplay.

It should not replace gameplay.

The animation is a consequence of the character's state.

---

# Practical Observation

AnimatedSprite2D works particularly well for frame-by-frame artwork.

Examples include:

- pixel art
- hand-drawn sprites
- character animation
- enemies
- collectibles

As projects become larger...

each gameplay state often receives its own animation.

This makes the game feel much more responsive and readable.

---

# Common Misconceptions

### "AnimatedSprite2D moves the player."

No.

It changes only the images being displayed.

Movement still comes from CharacterBody2D.

---

### "Animations contain gameplay."

Usually not.

Animations represent gameplay visually.

The gameplay logic should remain inside the controlling scripts.

---

### "Every object needs animation."

No.

Many objects are perfectly represented by a single Sprite2D.

Animation is useful when the appearance changes over time.

---

### "Calling `play()` starts gameplay."

No.

Calling:

```gdscript
play("jump")
```

changes only the animation.

Your gameplay code still controls jumping, collisions, and movement.

---

# Reflection

Suppose your player can:

- stand still
- walk
- jump
- fall
- attack

Which of these should probably have their own animation?

Now ask yourself:

If the artwork changed completely...

would the gameplay still function?

Why?

---

# Looking Ahead

Right now we choose animations manually.

```gdscript
play("walk")
```

Eventually...

the game should choose animations automatically.

Instead of asking:

> Which animation should I play?

we'll begin asking:

> **What is the player's current state?**

The animation can then respond automatically to the gameplay.