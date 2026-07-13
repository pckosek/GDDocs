# 4.2.5 Reset the Game

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Our Game Manager now remembers information for the entire lifetime of the game.

That's exactly what we wanted.

But eventually every game reaches a familiar moment.

The player chooses:

```text
New Game
```

Should the previous score still exist?

Should the player keep all of their lives from the last playthrough?

Should previously completed objectives remain complete?

Usually not.

When a new game begins, the game's state should return to its starting values.

---

# Why This Technique Matters

Changing scenes does **not** reset an Autoload.

The Game Manager continues to exist until the application closes.

That means global variables continue remembering their values.

If we want to begin a completely new game, we must intentionally restore those variables to their initial state.

---

# Starter Implementation

Suppose your Game Manager currently stores:

```gdscript
extends Node

var score = 0
var player_lives = 3
var current_level = 1
var game_paused = false
```

Create a new function.

```gdscript
func reset_game():
	score = 0
	player_lives = 3
	current_level = 1
	game_paused = false
```

Whenever a new game begins, call:

```gdscript
GameManager.reset_game()
```

All of the game's global state returns to its starting values.

---

# Dissecting the Code

Notice that we are **not** creating new variables.

Instead, we are changing the values of the existing ones.

```gdscript
score = 0
```

does not create another score.

It restores the original value.

The Game Manager remains the owner of the information.

Only the contents change.

---

# Design Principle

## Reset state intentionally.

A new game should begin from a known, predictable state.

Rather than hoping variables happen to contain the correct values...

...explicitly restore them.

Programs become much easier to understand when initialization happens in one place.

---

# Experiment

Imagine the player finishes a game with:

```text
Score = 1840

Lives = 1

Current Level = 7
```

Now the player chooses:

```text
New Game
```

After calling:

```gdscript
GameManager.reset_game()
```

What should each value become?

Should every variable return to its default?

Are there any values that should remain unchanged?

---

# Practical Observation

Many games separate two kinds of information.

Some information belongs to the current play session.

Examples include:

- score
- player health
- current checkpoint
- collected items

Other information survives between play sessions.

Examples include:

- unlocked achievements
- graphics settings
- volume controls
- key bindings

Only information belonging to the current game should usually be reset.

Persistent settings are often stored separately.

---

# Common Misconceptions

### "Loading a new scene resets the Game Manager."

No.

Autoloads continue to exist across scene changes.

Their variables keep their current values until you change them.

---

### "Creating a new Game Manager resets everything."

No.

There is still only one Game Manager.

The reset function changes its variables back to their starting values.

---

### "Every variable should be reset."

Not necessarily.

Some information is intended to persist beyond a single play session.

Consider carefully what belongs to the game, and what belongs to the player.

---

### "Resetting means deleting variables."

No.

The variables continue to exist.

Only their values change.

---

# Reflection

Suppose your Game Manager contains the following variables.

```gdscript
score
player_lives
current_level
difficulty
volume
music_enabled
```

Which variables should usually be reset when starting a new game?

Which should remain unchanged?

Explain your reasoning.

---

# Looking Ahead

Our Game Manager now owns global information...

...allows every script to access it...

...and can restore the game to a clean starting state.

The next challenge is communication.

> **How can the Game Manager notify the rest of the game when something important changes?**