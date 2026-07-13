# 8.1.3 Grid Movement

## Classification

**Type:** Engineering Technique

**Category:** Overworld

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Problem

Continuous movement asks the player:

> **Where are you moving right now?**

Grid movement asks a different question.

> **Where do you want to move next?**

Instead of constantly adjusting the player's position...

the game moves the player one grid cell at a time.

Each movement becomes a deliberate decision.

---

# Why This Matters

Grid movement appears in many games including:

- classic adventure games
- puzzle games
- tactical games
- roguelikes

Because movement occurs one cell at a time...

designers gain precise control over:

- positioning
- puzzles
- timing
- interaction

Every movement becomes meaningful.

---

# Mental Model

Think about playing chess.

You do not continuously slide a piece across the board.

You choose:

```text
Move Here
```

The piece moves.

Then you make another decision.

Grid movement follows the same pattern.

```text
Decision

↓

Movement

↓

Decision

↓

Movement
```

Movement becomes a sequence of choices.

---

# Starter Implementation

Suppose each tile is:

```text
32 × 32 pixels
```

When the player presses a direction...

calculate the destination.

```gdscript
var target = position + Vector2.RIGHT * 32
```

Instead of instantly changing the position...

smoothly move toward it.

```gdscript
var tween = create_tween()

tween.tween_property(
    self,
    "position",
    target,
    0.15
)
```

The movement now feels deliberate while remaining visually smooth.

---

# Dissecting the System

Notice what changed.

Continuous movement:

```text
Hold Key

↓

Continuous Motion
```

Grid movement:

```text
Press Key

↓

Choose Destination

↓

Tween

↓

Arrive
```

The player issues a command.

The movement completes.

Then the next decision begins.

---

# Design Principle

## One input.

One movement.

Grid movement works best when each player action produces one complete movement.

This rhythm creates:

- predictability
- precision
- intentional play

The player focuses on planning rather than continuous control.

---

# Practical Observation

Tweening is not changing the gameplay.

The gameplay already knows:

```text
Start Tile

↓

Destination Tile
```

Tweening simply changes **how the movement is presented**.

Without a Tween:

```text
Tile A

↓

Tile B
```

With a Tween:

```text
Tile A

↓

Smooth Motion

↓

Tile B
```

The movement feels more natural while preserving the same gameplay.

---

# Common Misconceptions

### "Grid movement should teleport."

It can.

However...

smooth interpolation often makes movement feel much more responsive and polished.

---

### "Tweening changes the destination."

No.

The destination is already known.

The Tween simply animates the journey.

---

### "Players should move continuously between tiles."

Usually not.

Most grid-based games complete one movement before accepting the next.

This creates predictable interactions.

---

### "Grid movement is less expressive."

Not necessarily.

Grid movement often creates deeper:

- puzzles
- planning
- tactical combat
- exploration

The movement becomes simpler.

The decisions become richer.

---

# Reflection

Imagine exploring a dungeon.

Would the experience feel different if movement were:

- continuous?

or

- one tile at a time?

How would this affect:

- puzzles?
- enemy movement?
- planning?

Now ask yourself:

What does the Tween change?

The gameplay...

...or only the player's experience?

---

# Looking Back

Earlier we implemented four-way movement.

Now we've transformed movement into a sequence of deliberate decisions.

Each key press produces:

- one destination
- one movement
- one opportunity to think

Tweening allows those decisions to feel smooth while preserving the precision of the underlying grid.

The movement system becomes another example of separating:

- gameplay
- presentation

---

# Looking Ahead

The player now moves smoothly from tile to tile.

The next question becomes:

Which direction should the player appear to face?

Should movement...

...animation...

...and interaction all share the same orientation?

We'll begin exploring:

> **Facing Direction**