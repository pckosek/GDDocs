# 4.2.3 Store Global Variables

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Our Game Manager now exists for the entire lifetime of the game.

At the moment, however, it doesn't actually remember anything.

A manager without information has nothing to manage.

The next step is to begin storing the pieces of game state that belong to the entire game.

---

# Why This Technique Matters

Global variables describe information that many different systems need to access.

Examples include:

- current score
- player lives
- current level
- game paused
- game difficulty

Rather than creating separate copies inside every object, the Game Manager keeps one authoritative version of each value.

This becomes the game's **Single Source of Truth**.

---

# Starter Implementation

Open **GameManager.gd**.

Add several variables.

```gdscript
extends Node

var score = 0
var player_lives = 3
var current_level = 1
var game_paused = false
```

Save the script.

Run the project.

Nothing visible has changed.

That is expected.

These variables exist to describe the game's current state.

---

# Dissecting the Script

Each variable answers a different question about the game.

```gdscript
score
```

How many points has the player earned?

---

```gdscript
player_lives
```

How many chances remain?

---

```gdscript
current_level
```

Where is the player?

---

```gdscript
game_paused
```

Should gameplay currently continue?

---

Together, these variables describe the current state of the game.

---

# Design Principle

## Variables describe the game.

Good variable names answer meaningful questions.

Instead of asking:

> What number is this?

Ask:

> What fact about the game does this variable represent?

A well-named variable should communicate its purpose without additional explanation.

---

# Experiment

Imagine adding the following variables.

```gdscript
var music_volume = 0.75
var difficulty = "Normal"
var coins_collected = 42
var player_name = "Alex"
```

Ask yourself:

Does this information belong to one object...

...or to the game as a whole?

If many systems need the value, it may belong inside the Game Manager.

---

# Practical Observation

Not every variable belongs in the Game Manager.

For example:

```gdscript
var enemy_health = 100
```

would usually be a poor choice.

Every enemy should remember its own health.

Storing all enemy health values globally would make the Game Manager responsible for information it does not own.

As a rule of thumb:

- Store **shared game information** globally.
- Store **object-specific information** locally.

---

# Common Misconceptions

### "Every variable belongs in the Game Manager."

No.

Only variables that describe the entire game should be stored globally.

---

### "The Game Manager replaces object variables."

No.

Enemies, players, doors, and other objects should continue owning their own local state.

The Game Manager exists to store information shared across the game.

---

### "Variables are only numbers."

No.

Variables can store many kinds of information.

Examples include:

- numbers
- text
- true/false values
- references to objects
- arrays
- dictionaries

Each represents a different kind of game state.

---

### "Global variables should constantly change."

Some do.

Others, such as game settings or player names, may change very rarely.

Whether a variable changes depends on what information it represents.

---

# Reflection

Consider each of the following variables.

Would you place it inside the Game Manager?

| Variable | Game Manager? |
|----------|---------------|
| score | |
| player_health | |
| current_level | |
| enemy_health | |
| game_paused | |
| inventory | |
| door_open | |
| difficulty | |

Can you explain **why** each variable belongs where it does?

---

# Looking Ahead

Right now, the Game Manager stores information.

The next question is:

> **How can the rest of the game access those variables?**