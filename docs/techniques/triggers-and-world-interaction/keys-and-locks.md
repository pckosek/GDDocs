---
tags: [technique, trigger]
---

# 8.3.3 Keys & Doors

## Classification

**Type:** Engineering Technique

**Category:** Interaction

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine the player reaches a locked door.

They press:

```text
Interact
```

Nothing happens.

Later...

they discover a key.

They return.

The same interaction now opens the door.

What changed?

The player pressed the same button.

The door looked almost the same.

The answer is simple.

The **state** of the world changed.

---

# Why This Matters

Many adventure games are built around changing world state.

Examples include:

- locked doors
- collected keys
- activated switches
- opened bridges
- completed puzzles

These objects remember previous events.

The world gradually changes as the player explores.

Progress becomes visible.

---

# Mental Model

Think about a light switch.

It has two possible states.

```text
Off

↓

On
```

The switch itself remains the same.

Only its state changes.

A locked door works in exactly the same way.

```text
Locked

↓

Unlocked
```

The player's actions change the state.

The world responds differently.

---

# Starter Implementation

A simple door might store:

```gdscript
var locked = true
```

When the player interacts:

```gdscript
if locked:

    print("The door is locked.")

else:

    open_door()
```

Finding a key simply changes the state.

```gdscript
locked = false
```

The interaction code never changes.

Only the world's state changes.

---

# Dissecting the System

Notice the sequence.

```text
Find Key

↓

Change State

↓

Interact

↓

Door Opens
```

The key does not open the door directly.

It changes information.

The door interprets that information later.

---

# Design Principle

## State determines behaviour.

Gameplay objects rarely ask:

> **What just happened?**

Instead they ask:

> **What state is the world currently in?**

Behaviour emerges from state.

Changing the state changes future interactions.

---

# Practical Observation

Many different gameplay systems share this idea.

Examples include:

```text
Chest

↓

Opened

↓

Closed
```

---

```text
Bridge

↓

Raised

↓

Lowered
```

---

```text
Quest

↓

Incomplete

↓

Complete
```

Although the objects differ...

the underlying pattern remains the same.

State controls behaviour.

---

# Common Misconceptions

### "The key opens the door."

Not directly.

The key changes the world's state.

The door later responds to that new state.

---

### "Every door needs different code."

Usually not.

Many doors share exactly the same interaction logic.

Only the state changes.

---

### "State only belongs to characters."

The world also has state.

Doors.

Switches.

Bridges.

NPCs.

Many gameplay objects remember previous events.

---

### "Opening the door removes the puzzle."

Changing state often creates new possibilities.

One solved puzzle frequently unlocks another part of the world.

Progression emerges through changing world state.

---

# Reflection

Imagine creating an adventure game.

Which of these objects have state?

| Object | Possible States |
|---------|-----------------|
| Door | |
| Treasure Chest | |
| Bridge | |
| Quest | |
| NPC | |

How does changing each state affect future gameplay?

---

# Looking Back

Earlier we explored:

- interaction
- dialogue

Now we've discovered that interaction often changes the world itself.

Adventure games are built from objects that remember.

The player gradually transforms the world by changing its state.

The world becomes another participant in the gameplay.

---

# Looking Ahead

Changing one object is useful.

Changing many objects together is even more powerful.

How can one interaction activate:

- doors
- bridges
- traps
- puzzles

throughout the world?

We'll begin exploring:

> **Switches & Events**