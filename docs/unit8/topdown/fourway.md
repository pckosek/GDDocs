# 8.1.2 Four-Way Movement

## Classification

**Type:** Engineering Technique

**Category:** Overworld

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

In a platformer, movement is influenced by:

- gravity
- jumping
- falling
- momentum

In many overworld games...

none of these exist.

The player simply moves:

- north
- south
- east
- west

Without gravity...

movement becomes much simpler.

The challenge shifts from controlling physics to navigating the world.

---

# Why This Matters

Four-way movement appears in many kinds of games.

Examples include:

- adventure games
- role-playing games
- puzzle games
- strategy games

The player focuses on:

- exploration
- positioning
- interaction

rather than jumping or falling.

This creates a very different style of gameplay.

---

# Starter Implementation

Unlike our platformer...

there is no gravity.

Instead, we determine the player's intended direction directly from the input.

```gdscript
var direction := Input.get_vector(
    "move_left",
    "move_right",
    "move_up",
    "move_down"
)

velocity = direction * SPEED

move_and_slide()
```

The player moves in the direction they choose.

When no input is pressed...

the player stops immediately.

---

# Dissecting the Code

Notice what disappeared.

Platformer movement looked something like:

```text
Input

↓

Velocity

↓

Gravity

↓

move_and_slide()
```

Overworld movement becomes:

```text
Input

↓

Direction

↓

Velocity

↓

move_and_slide()
```

Without gravity...

the movement system becomes much more direct.

---

# Direction

The player's movement also determines which direction they are facing.

For example:

```gdscript
if direction.x > 0:
    facing = EAST

elif direction.x < 0:
    facing = WEST

elif direction.y > 0:
    facing = SOUTH

elif direction.y < 0:
    facing = NORTH
```

Later...

this facing direction can control:

- animations
- attacks
- interaction
- dialogue

Movement becomes one part of a larger gameplay system.

---

# Design Principle

## Separate movement from direction.

Movement answers:

> **Where is the player going?**

Direction answers:

> **Which way is the player facing?**

Although these ideas are related...

they often become independent systems later in development.

Keeping them separate makes future features much easier to add.

---

# Practical Observation

Many overworld games intentionally avoid momentum.

When the player releases a movement key...

the character stops immediately.

This creates:

- precise movement
- responsive controls
- predictable positioning

These qualities are especially important when interacting with NPCs, puzzles, and tile-based environments.

---

# Common Misconceptions

### "Four-way movement doesn't use velocity."

It still does.

Velocity simply comes directly from player input rather than from gravity and acceleration.

---

### "Gravity should always exist."

Not necessarily.

Many overworld games intentionally remove gravity because vertical movement is no longer part of the design.

---

### "Facing direction and movement are the same."

Usually they begin together.

Later...

many games allow the player to face one direction while moving or interacting in another.

Keeping these systems separate makes that possible.

---

### "Simpler movement creates simpler gameplay."

Not at all.

Reducing movement complexity often allows designers to create richer:

- puzzles
- exploration
- interactions
- combat

Simple movement can support surprisingly deep games.

---

# Reflection

Compare these two movement systems.

| Platformer | Overworld |
|------------|-----------|
| Gravity | |
| Jumping | |
| Falling | |
| Four Directions | |
| Precise Positioning | |

How does removing gravity change the player's decisions?

What kinds of gameplay become easier to design?

---

# Looking Back

Earlier we explored the difference between continuous and grid movement.

Now we've implemented one of the simplest forms of overworld movement.

Without gravity...

movement becomes a direct relationship between:

- input
- direction
- velocity

This simpler movement system creates new opportunities for exploration and interaction.

---

# Looking Ahead

Four-way movement allows the player to explore freely.

Sometimes, however...

movement should feel much more deliberate.

Instead of moving continuously...

the player may move one tile at a time.

The next lesson explores another important movement system:

> **Grid Movement**