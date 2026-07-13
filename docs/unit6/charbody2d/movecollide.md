# 6.1.5 `move_and_collide()`

## Classification

**Type:** Engineering Technique

**Category:** 2D Character Movement

**Difficulty:** Intermediate

**Estimated Time:** 15–20 minutes

---

# Design Problem

In the previous lesson we used:

```gdscript
move_and_slide()
```

to move our player.

Godot also provides another movement function.

```gdscript
move_and_collide()
```

Both functions move a `CharacterBody2D`.

So...

why are there two?

The difference is not **whether** the character moves.

The difference is **how much of the movement behavior Godot performs automatically.**

---

# Why This Matters

Most platformer characters should use:

```gdscript
move_and_slide()
```

because it automatically handles many common situations such as:

- sliding along walls
- walking across floors
- responding naturally to slopes

Sometimes, however, we want complete control over what happens after a collision.

In those situations:

```gdscript
move_and_collide()
```

becomes useful.

---

# Starter Implementation

A minimal example looks like this.

```gdscript
func _physics_process(delta):

    velocity.x = 200

    var collision = move_and_collide(
        velocity * delta
    )
```

Unlike:

```gdscript
move_and_slide()
```

this function returns information about the collision.

Your code decides what should happen next.

---

# Dissecting the Code

Think about the difference.

With:

```gdscript
move_and_slide()
```

the engine performs:

```text
Move

↓

Collide

↓

Slide

↓

Continue
```

Much of the behavior is automatic.

---

With:

```gdscript
move_and_collide()
```

the engine performs:

```text
Move

↓

Collision?

↓

Tell Your Script
```

Now **your code** decides how to respond.

Perhaps:

- stop moving
- bounce
- explode
- reverse direction
- trigger an event

The movement function gives you more responsibility.

---

# Design Principle

## Choose the level of control you need.

If your movement follows common platformer behavior...

...`move_and_slide()` usually provides the simplest solution.

If collisions require custom responses...

...`move_and_collide()` gives your script greater control.

Neither function is universally better.

They solve different problems.

---

# Comparison

| Function | Best Used For |
|-----------|---------------|
| `move_and_slide()` | Characters that walk, run, jump, and slide naturally |
| `move_and_collide()` | Objects requiring custom collision responses |

Most platformers primarily use:

```gdscript
move_and_slide()
```

Objects such as projectiles or special moving hazards may benefit from:

```gdscript
move_and_collide()
```

---

# Practical Observation

In this course...

your player will almost always use:

```gdscript
move_and_slide()
```

because it provides the movement behavior expected of a platformer.

Later projects may introduce situations where:

```gdscript
move_and_collide()
```

is a better engineering choice.

Understanding both functions helps you choose the appropriate tool for each object.

---

# Common Misconceptions

### "`move_and_collide()` is an improved version of `move_and_slide()`."

No.

They solve different problems.

One provides more automatic behavior.

The other provides more manual control.

---

### "Players should always use `move_and_collide()`."

Usually not.

Most platformer characters are easier to implement using:

```gdscript
move_and_slide()
```

---

### "`move_and_collide()` automatically slides."

No.

Unlike `move_and_slide()`, your script is responsible for deciding what happens after the collision.

---

### "The two functions are interchangeable."

Not exactly.

Although both move the character...

...they are designed for different styles of movement.

---

# Reflection

Imagine creating each of the following.

Which movement function seems more appropriate?

| Object | Suggested Function |
|----------|--------------------|
| Player Character | |
| Enemy Patrol | |
| Bullet | |
| Rolling Boulder | |
| Moving Platform | |

Now ask yourself:

Which objects benefit from automatic movement...

...and which benefit from complete control?

---

# Looking Ahead

Our player can now:

- move
- collide
- slide
- respond naturally to the environment

The next challenge is making movement feel satisfying.

How can we build mechanics such as:

- jumping
- coyote time
- jump buffering

that make a platformer feel responsive and enjoyable to play?