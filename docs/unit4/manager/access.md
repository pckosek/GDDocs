# 4.2.4 Access the Game Manager

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Our Game Manager now stores the game's global information.

Unfortunately, information that cannot be accessed isn't very useful.

The player earns points.

The HUD needs to display the score.

The pause menu needs to know whether the game is paused.

The game over screen needs to know how many lives remain.

How can every part of the game access the same information?

Because the Game Manager is an **Autoload**, every script can refer to it directly.

---

# Why This Technique Matters

One of the biggest advantages of an Autoload is that it exists everywhere.

Instead of searching for an object in the scene...

Instead of passing references through multiple scripts...

Every script can simply access the Game Manager by name.

That means every system works with the same shared information.

---

# Starter Implementation

Suppose your Game Manager contains the following variables.

```gdscript
extends Node

var score = 0
var player_lives = 3
```

Now imagine the player collects a coin.

Inside another script, write:

```gdscript
GameManager.score += 1
```

The Game Manager now remembers the updated score.

---

Reading information is just as straightforward.

```gdscript
print(GameManager.score)
```

Or

```gdscript
if GameManager.player_lives <= 0:
    print("Game Over")
```

Every script refers to the same variables.

---

# Dissecting the Code

This line:

```gdscript
GameManager.score += 1
```

does **not** create a new variable.

It modifies the one stored inside the Game Manager.

Later...

```gdscript
print(GameManager.score)
```

reads the same value.

Every script is looking at the same piece of information.

---

Think of it like a shared whiteboard.

```text
GameManager

Score = 17
```

Any script can read the board.

Some scripts may also update it.

There is still only one score.

---

# Design Principle

## Shared information should be accessed from its owner.

If the Game Manager owns the score...

...other objects should ask the Game Manager for the score.

They should not keep their own separate copy.

This keeps every system working with the same information.

---

# Experiment

Suppose these scripts all execute.

### Player

```gdscript
GameManager.score += 10
```

---

### Coin

```gdscript
GameManager.score += 1
```

---

### HUD

```gdscript
print(GameManager.score)
```

What value should the HUD display?

How many score variables exist?

Where is that value actually stored?

---

# Practical Observation

Reading global information is usually much more common than changing it.

For example:

- the HUD reads the score
- the pause menu reads the pause state
- the game over screen reads the player's lives

Only a few systems should actually modify those values.

Thinking carefully about **who changes information** is an important part of designing reliable software.

---

# Common Misconceptions

### "GameManager.score creates a new variable."

No.

It refers to the variable already stored inside the Game Manager.

There is only one score.

---

### "Every script gets its own Game Manager."

No.

The Autoload creates one shared object.

Every script accesses that same object.

---

### "Reading a variable changes it."

No.

Reading simply retrieves the current value.

Only assignment statements change the state.

---

### "Any script should change any variable."

Just because every script *can* access a variable doesn't mean every script *should* modify it.

Good software carefully limits which systems are responsible for changing important information.

---

# Reflection

Imagine your game contains the following systems.

- Player
- HUD
- Pause Menu
- Enemy
- Game Over Screen

Which systems should:

- Read the player's score?
- Change the player's score?

Can every system use the Game Manager without becoming responsible for updating it?

---

# Looking Ahead

Our Game Manager can now store information...

...and every script can access it.

The next challenge is deciding what happens when we want to start a completely new game.

> **How do we reset the game's global state?**