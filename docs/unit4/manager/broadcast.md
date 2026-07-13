# 4.2.6 Broadcast Global Events

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Suppose the player collects a coin.

The Game Manager updates the score.

```gdscript
GameManager.score += 1
```

The score has changed.

Now consider everything else that might care about that change.

- The HUD should update the score display.
- An achievement system may check whether a milestone was reached.
- A sound effect may play.
- A save system may record the new progress.

How do all of those systems know that something happened?

---

# Why This Technique Matters

Updating a variable changes the game's state.

It does **not** automatically notify the rest of the game.

Without communication, every object would need to repeatedly ask:

> Has the score changed?

> Has the score changed now?

> What about now?

Checking over and over again is inefficient and difficult to maintain.

Instead, the Game Manager can announce that something important happened.

Other systems can decide whether they care.

---

# Starter Implementation

Imagine the Game Manager contains a function like this.

```gdscript
func add_score(points):
	score += points

	# Tell the rest of the game that the score changed.
	print("Score Updated")
```

Whenever another object wants to award points...

```gdscript
GameManager.add_score(10)
```

The Game Manager becomes responsible for both:

- updating the score
- announcing that something changed

For now, we are simply using a print statement to represent the announcement.

Later, we'll replace it with a proper signal.

---

# Dissecting the Technique

Think about the sequence of events.

```text
Player Collects Coin
        ↓
Game Manager Updates Score
        ↓
Game Manager Announces
        ↓
Other Systems React
```

Notice that the Game Manager does **not** tell the HUD what to do.

It simply announces:

> "The score changed."

The HUD decides what to do with that information.

So does every other interested system.

---

# Design Principle

## The owner of information should announce meaningful changes.

Objects that own important state should communicate when that state changes.

Other systems can choose whether or not to respond.

This keeps systems independent while allowing them to work together.

---

# Experiment

Suppose the player's health changes.

Which systems might care?

- HUD
- Screen Flash Effect
- Game Over Screen
- Enemy AI
- Achievement System

Should the Player script directly call every one of those systems?

Or would it be simpler to announce:

```text
Player Health Changed
```

and let interested systems respond?

---

# Practical Observation

As projects become larger, many systems begin sharing information.

Imagine adding a new achievement system six months after your game was written.

If every gameplay script directly updates the achievement system...

...many files need to be modified.

If the Game Manager simply announces important events...

...the achievement system can begin listening without changing existing gameplay code.

This makes software much easier to extend.

---

# Common Misconceptions

### "The Game Manager should update every system itself."

No.

Its responsibility is to manage game state.

Other systems remain responsible for their own behavior.

---

### "Every object needs to constantly check for changes."

Usually not.

Repeatedly checking information is inefficient.

It's often better for important changes to be announced when they happen.

---

### "Broadcasting means every object must respond."

No.

A broadcast simply announces that something happened.

Objects that care can react.

Objects that don't care can ignore it.

---

### "Print statements are the final solution."

No.

We're using `print()` only to illustrate the idea of broadcasting.

The next section introduces **Signals**, which provide a much more powerful and flexible way to communicate between independent systems.

---

# Reflection

Imagine your game contains the following events.

- Score Changed
- Player Died
- Door Opened
- Level Completed
- Game Reset

For each one, list two systems that might want to know it happened.

Do those systems need to own the information...

...or simply react to it?

---

# Looking Ahead

Our Game Manager can now:

- store global state
- share that information
- reset the game
- announce important changes

The next question is:

> **How can independent objects communicate without becoming tightly connected?**

The answer is one of the most powerful tools in Godot:

> **Signals.**