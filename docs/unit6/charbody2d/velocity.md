# 6.1.2 Velocity

## Classification

**Type:** Engineering Technique

**Category:** 2D Character Movement

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Suppose the player presses the right arrow.

How should the character move?

One possibility would be to directly change the player's position.

```gdscript
position.x += 5
```

This certainly moves the character.

However...

it ignores collisions, gravity, and many of the tools provided by `CharacterBody2D`.

Instead, CharacterBody2D expects us to describe movement using **velocity**.

Velocity tells the engine:

> **How should this character move during the next frame?**

---

# Why This Matters

Almost every movement system in a platformer begins by updating the character's velocity.

Examples include:

- walking
- jumping
- falling
- knockback
- moving platforms
- enemy movement

Rather than directly changing position...

...we describe how the character intends to move.

The engine then performs the movement safely.

---

# Starter Implementation

Every `CharacterBody2D` already contains a velocity property.

```gdscript
extends CharacterBody2D

func _physics_process(delta):

    velocity.x = 200

    move_and_slide()
```

When this code runs...

the player continuously moves to the right.

Notice that we never modify:

```gdscript
position
```

directly.

Movement happens through velocity.

---

Gravity works the same way.

```gdscript
velocity.y += 980 * delta
```

The character does not instantly move downward.

Instead...

its downward velocity gradually increases.

Later,

```gdscript
move_and_slide()
```

uses that velocity to update the player's position.

---

# Dissecting the Code

Notice the sequence.

```text
Player Input

↓

Update Velocity

↓

move_and_slide()

↓

New Position
```

The position changes automatically.

Velocity describes the motion.

The movement function performs it.

Separating these responsibilities makes character movement much easier to manage.

---

# Design Principle

## Describe movement, not position.

CharacterBody2D is designed around velocity.

Rather than repeatedly changing position yourself...

...describe how the character should move.

Then allow the engine to resolve movement and collisions.

This produces cleaner, more predictable code.

---

# Comparison

There are several ways to move an object.

| Approach | Appropriate? |
|-----------|--------------|
| `position += ...` | Simple objects without collisions |
| `velocity + move_and_slide()` | CharacterBody2D movement |
| Physics Forces | RigidBody2D |

Choosing the correct approach depends on the kind of object you are creating.

---

# Practical Observation

Beginning programmers often think:

> I want my player to be *here*.

Character controllers usually think differently.

They ask:

> I want my player to move *this fast* in *this direction*.

The engine determines where the player finally ends up after accounting for collisions and the environment.

---

# Common Misconceptions

### "Velocity is the player's position."

No.

Position describes **where** the player is.

Velocity describes **how the player is moving**.

---

### "Changing velocity immediately moves the player."

Not by itself.

Velocity only describes movement.

A movement function such as:

```gdscript
move_and_slide()
```

uses that velocity to update the player's position.

---

### "Velocity only affects horizontal movement."

No.

Velocity has both horizontal and vertical components.

```gdscript
velocity.x
velocity.y
```

Each may be updated independently.

---

### "Position should never be changed directly."

Not exactly.

Some objects can safely change position directly.

CharacterBody2D is specifically designed to move using velocity together with its movement functions.

---

# Reflection

Suppose the player:

- walks
- jumps
- falls
- lands

Which component of the velocity changes most?

| Action | X Velocity | Y Velocity |
|---------|------------|------------|
| Walk Right | | |
| Jump | | |
| Fall | | |
| Land | | |

Now ask yourself:

Why is it useful to separate horizontal and vertical movement?

---

# Looking Ahead

Velocity describes how the character wants to move.

The next challenge is choosing **how** the engine should apply that movement.

CharacterBody2D provides two important movement functions.

The first—and most commonly used for platformers—is:

> **`move_and_slide()`**