# 7.1.4 Core Loops

## Classification

**Type:** Design / Engineering Guide

**Category:** Understanding Games

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Problem

Suppose someone asks:

> "What do players do in your game?"

You answer:

- jump
- fight
- collect items
- craft

Those are mechanics.

But another question is even more important.

> **What do players do over and over again?**

Games are rarely defined by a single action.

Instead...

players repeat a sequence of actions.

That repeating sequence is called a **Core Loop**.

---

# Why This Matters

The Core Loop is the heartbeat of a game.

It describes the cycle of actions players perform throughout most of their playtime.

A satisfying loop encourages players to continue playing because each repetition feels meaningful.

Understanding your Core Loop helps answer one of the most important design questions:

> **Why would someone keep playing?**

---

# Mental Model

Think about riding a bicycle.

Pedals move in circles.

The motion repeats.

Yet every rotation moves you farther forward.

Core Loops work similarly.

```text
Action

↓

Result

↓

Reward

↓

Repeat
```

The player repeats familiar actions...

...while continually making progress.

---

# Example Loops

Many games can be summarized by remarkably simple loops.

### Platformer

```text
Run

↓

Jump

↓

Avoid Hazards

↓

Reach Goal

↓

Repeat
```

---

### RPG

```text
Explore

↓

Fight

↓

Loot

↓

Upgrade

↓

Explore
```

---

### Minecraft

```text
Explore

↓

Collect

↓

Craft

↓

Build

↓

Explore
```

---

### Puzzle Game

```text
Observe

↓

Think

↓

Solve

↓

New Puzzle

↓

Observe
```

Notice that every loop returns to its beginning.

The player is always ready for another cycle.

---

# Dissecting the Loop

Notice the difference.

Mechanics describe:

```text
Jump

Attack

Collect
```

The Core Loop describes:

```text
How those mechanics work together over time.
```

Individual mechanics become meaningful because they support the larger cycle of play.

The experience emerges from repetition.

---

# Design Principle

## Players return because the loop remains satisfying.

Individual mechanics may attract a player.

The Core Loop keeps them engaged.

A strong Core Loop balances:

- challenge
- reward
- progression
- repetition

Each cycle should encourage the player to begin the next one.

---

# Practical Observation

Beginning designers often list features.

For example:

- inventory
- crafting
- dialogue
- combat

Experienced designers often sketch a loop instead.

```text
Fight

↓

Reward

↓

Upgrade

↓

Fight Stronger Enemy
```

The loop quickly reveals:

- what the player spends time doing
- why progression exists
- where rewards belong

Designing the loop often clarifies the entire game.

---

# Common Misconceptions

### "The Core Loop is the entire game."

No.

The Core Loop describes the primary repeating experience.

Many games also contain:

- side activities
- narrative moments
- exploration
- optional challenges

---

### "More mechanics create a better loop."

Not necessarily.

Many excellent games rely on surprisingly simple loops.

The quality of the loop usually matters more than the number of mechanics.

---

### "Players consciously notice the Core Loop."

Usually not.

Players simply experience the rhythm of the game.

Designers deliberately shape that rhythm.

---

### "Every game has the same loop."

No.

Different genres emphasize different patterns of play.

The Core Loop reflects the experience the designer wants the player to have.

---

# Reflection

Choose one of the following games.

- Mario
- Zelda
- Minecraft
- Pokémon
- Stardew Valley

Sketch its Core Loop.

Can you describe it using only four or five repeated actions?

Now ask yourself:

If you removed one step from the loop...

would the game still feel the same?

Why?

---

# Looking Back

Earlier we explored:

- genres
- mechanics

Now we've discovered how mechanics become experiences.

Mechanics are individual actions.

Core Loops organize those actions into meaningful cycles that players repeat throughout the game.

The loop is often what players remember long after individual mechanics have become familiar.

---

# Looking Ahead

Repeating the same loop forever would eventually become repetitive.

Games need another ingredient.

How do players feel that they are growing stronger, learning more, or unlocking new possibilities?

The next lesson explores one of the most important long-term design ideas:

> **Progression**