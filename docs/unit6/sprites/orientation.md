# 6.3.5 Sprite Orientation

## Classification

**Type:** Engineering Technique

**Category:** Visual Representation

**Difficulty:** Beginner

**Estimated Time:** 15–20 minutes

---

# Design Problem

Our player can now:

- walk
- jump
- animate

There is one problem.

The player always faces the same direction.

If the player runs left...

...the sprite still looks right.

Should we create two complete sets of artwork?

One facing left.

One facing right.

Usually...

we don't need to.

Instead, we can change the sprite's **orientation**.

---

# Why This Matters

Many 2D games use the same artwork for both directions.

Instead of storing:

- walk_left
- walk_right

they often store only:

- walk

The engine mirrors the sprite whenever the character changes direction.

This greatly reduces the amount of artwork required while keeping animations synchronized.

---

# Starter Implementation

Suppose the player moves horizontally.

```gdscript
if velocity.x > 0:
    $AnimatedSprite2D.flip_h = false

elif velocity.x < 0:
    $AnimatedSprite2D.flip_h = true
```

When the player walks right...

the sprite faces right.

When the player walks left...

the sprite is mirrored.

The animation itself never changes.

Only its orientation changes.

---

# Dissecting the Code

Notice that we are **not** changing the animation.

```text
Walk Animation

↓

Facing Right

-------------------

Walk Animation

↓

Facing Left
```

The animation remains exactly the same.

The sprite simply displays it from the opposite direction.

This keeps the gameplay and animation logic much simpler.

---

# Mental Model

Think about holding a photograph.

Turning it around does not create a new photograph.

It changes only the way you are looking at it.

Sprite orientation works similarly.

```text
Animation

↓

Orientation

↓

Visual Result
```

The underlying artwork remains the same.

---

# Design Principle

## Separate movement from orientation.

The character's movement determines where they travel.

Their orientation determines where they appear to face.

These are related...

...but they are not the same thing.

Keeping them separate makes character animation much easier to manage.

---

# Practical Observation

Many beginning programmers create separate animations.

```text
Walk Left

Walk Right

Idle Left

Idle Right
```

For many side-scrolling games...

this is unnecessary.

Instead, a single animation combined with:

```gdscript
flip_h
```

produces both directions automatically.

This saves both development time and artwork.

---

# Common Misconceptions

### "Flipping changes gameplay."

No.

It changes only the visual representation.

The player's movement and collisions remain exactly the same.

---

### "Every animation needs a left and right version."

Usually not.

For many side-scrolling games, one animation is enough.

The engine mirrors it automatically.

---

### "Orientation depends on keyboard input."

Not directly.

It usually depends on gameplay.

For example:

```gdscript
velocity.x
```

or

```gdscript
facing_direction
```

Animation should respond to the character's state rather than directly to the keyboard.

---

### "Flipping always works."

Not always.

Some artwork contains text, asymmetrical equipment, or unique poses that require separate animations.

Choosing whether to flip or create new artwork is a design decision.

---

# Reflection

Imagine creating each of the following.

Would flipping the sprite work?

| Character | Flip H? |
|------------|----------|
| Player | |
| Skeleton Enemy | |
| Archer | |
| Signpost | |
| Character Holding a Shield | |
| Character Wearing Text on Their Shirt | |

Can you explain why?

---

# Looking Back

Our visual representation now communicates:

- movement
- jumping
- falling
- direction

The player's state controls the animation.

The animation communicates the gameplay.

The sprite's orientation completes that communication by showing which way the character is facing.

---

# Looking Ahead

Sprites and animations help players understand what is happening.

Sometimes, however, movement alone is not enough.

Good games often use visual effects to reinforce important events.

The next section explores how animation becomes one part of a much larger system of player feedback.