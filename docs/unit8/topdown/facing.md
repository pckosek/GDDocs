# 8.1.5 Facing Direction

## Classification

**Type:** Engineering Technique

**Category:** Overworld

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Suppose the player stops moving.

Which way should they face?

The answer matters.

If the player presses:

```text
Interact
```

Which object should respond?

If they swing a sword...

Which direction should the attack travel?

In overworld games...

direction becomes part of the gameplay itself.

---

# Why This Matters

Facing direction influences many gameplay systems.

Examples include:

- interaction
- attacks
- dialogue
- animation
- enemy awareness

Movement determines where the player goes.

Facing determines how the player interacts with the world.

These are related...

...but they are not the same thing.

---

# Mental Model

Imagine standing in a room.

You may remain completely still.

Yet you can still choose to look:

- north
- south
- east
- west

Your position has not changed.

Only your orientation has.

Games work the same way.

```text
Position

+

Direction

↓

Player State
```

Both pieces of information are important.

---

# Starter Implementation

Store the player's current facing direction.

```gdscript
enum Direction {
    NORTH,
    SOUTH,
    EAST,
    WEST
}

var facing = Direction.SOUTH
```

Whenever the player moves...

update the direction.

```gdscript
if direction.x > 0:
    facing = Direction.EAST

elif direction.x < 0:
    facing = Direction.WEST

elif direction.y > 0:
    facing = Direction.SOUTH

elif direction.y < 0:
    facing = Direction.NORTH
```

Movement updates the facing direction.

Later...

many other systems can use it.

---

# Dissecting the System

Notice the separation.

```text
Movement

↓

Position
```

```text
Direction

↓

Interaction
```

The player may stop moving...

while still facing a particular direction.

Gameplay systems continue using that information.

---

# Sprite Orientation

Earlier we learned about sprite orientation.

In a platformer...

we often flipped the sprite horizontally.

```text
Left

↓

Right
```

Overworld games expand that idea.

Instead of two directions...

the sprite may now have:

- North
- South
- East
- West

The gameplay direction determines which animation should be displayed.

Animation becomes another representation of gameplay state.

---

# Design Principle

## Direction is gameplay information.

Facing direction is not only visual.

Many gameplay systems depend on knowing which way the player is facing.

Keeping direction separate from animation makes those systems easier to build.

Gameplay determines direction.

Animation communicates it.

---

# Practical Observation

Many beginning projects use the sprite to determine direction.

As projects become larger...

it often becomes more reliable to let the gameplay own this information.

For example:

```text
Facing Direction

↓

Animation

↓

Attack

↓

Interaction
```

Several systems now share one source of truth.

---

# Common Misconceptions

### "Facing direction only changes the sprite."

No.

It often determines:

- attack direction
- interaction direction
- dialogue targets
- item placement

Gameplay frequently depends on orientation.

---

### "Movement and facing are identical."

Often...

but not always.

Many games allow characters to remain stationary while changing the direction they face.

---

### "The sprite decides which way the player faces."

Usually the opposite.

Gameplay determines direction.

The sprite visualizes that information.

---

### "Only the player needs facing direction."

Enemies.

NPCs.

Projectiles.

Many gameplay objects use orientation.

Direction becomes another shared gameplay concept.

---

# Reflection

Imagine standing next to a treasure chest.

You are facing:

- north

The chest is:

- east

Should pressing **Interact** open the chest?

Why?

Now imagine turning to face the chest without moving.

Should the result change?

What information did the game actually need?

---

# Looking Back

Earlier we explored:

- continuous movement
- four-way movement
- grid movement
- interpolation

Now we've discovered that movement alone is not enough.

The game also needs to know which way the player is facing.

Direction becomes another piece of gameplay information that many systems can share.

The sprite simply communicates that information visually.

---

# Looking Ahead

The player can now move through the overworld with clear direction.

The next challenge is interacting with the world itself.

How do players:

- open doors?
- talk to NPCs?
- collect objects?
- activate switches?

We'll begin exploring:

> **World Interaction**