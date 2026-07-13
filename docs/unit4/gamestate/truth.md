# 4.1.5 Single Source of Truth

## Classification

**Type:** Design / Engineering Guide

**Category:** Game Architecture

**Difficulty:** Intermediate

---

# Design Problem

Imagine your game keeps track of the player's score.

Now imagine three different objects each have their own copy of that score.

```text
Player
Score = 150

HUD
Score = 140

Enemy Manager
Score = 150
```

Which one is correct?

If different parts of the game remember different values for the same information, the game can no longer be certain what is true.

Good software avoids this problem by giving each important piece of information **one authoritative owner**.

This idea is called a **Single Source of Truth**.

---

# Why This Matters

As games become larger, many different systems need access to the same information.

The player's health might be displayed by:

- the HUD
- the pause menu
- a game over screen
- enemy AI
- achievements

Every one of those systems needs to *know* the player's health.

But only one system should *own* it.

Everyone else should simply ask for the current value.

---

# Mental Model

Think of important game information as living in one official location.

```text
Player
Health = 85
```

Whenever another object needs that information...

```text
HUD
```

or

```text
Enemy AI
```

or

```text
Game Over Screen
```

they all look at the same value.

Nobody keeps their own separate copy.

---

Another way to think about it is:

```text
One Owner

↓

Many Readers
```

The owner is responsible for updating the information.

Everyone else simply uses it.

---

# Design Principle

## Every important fact should have one authoritative owner.

Multiple systems may *use* the information.

Only one system should *own* it.

This keeps the game consistent and prevents different parts of the program from disagreeing.

---

# Example

Suppose the player collects a coin.

Instead of updating five different score variables...

```text
Player Score += 1

HUD Score += 1

Achievement Score += 1

Menu Score += 1

Save Score += 1
```

The game updates **one** score.

```text
Score += 1
```

Every other system simply displays or uses that value.

---

# Practical Observation

Many beginner programmers accidentally duplicate information.

For example, they might store:

- the player's health inside the Player
- another copy inside the HUD
- another copy inside an enemy script

At first, everything seems to work.

Eventually, one copy changes while another does not.

Now the HUD says the player has 40 health.

The Player says 35.

Which one is correct?

The bug isn't in the arithmetic.

The bug is that the game has forgotten which value is the real one.

---

# Common Misconceptions

### "It's faster to keep lots of copies."

Usually not.

Multiple copies must all be updated correctly.

That makes the program more complicated and introduces opportunities for mistakes.

---

### "Every object should store the information it uses."

Not necessarily.

Using information is different from owning it.

Many objects can read the same value without keeping their own copy.

---

### "Duplicating information makes the program safer."

Usually the opposite is true.

Whenever the same fact exists in multiple places, those copies can eventually disagree.

One owner is almost always easier to manage than many copies.

---

# Reflection

Consider each piece of information below.

Who should own it?

| Information | Possible Owner |
|--------------|----------------|
| Player Health | |
| Current Score | |
| Door Open | |
| Enemy Health | |
| Volume Setting | |
| Current Level | |
| Inventory | |

Now ask yourself:

Which other systems might need to *read* that information?

Do they really need their own copy?

---

# Looking Ahead

We've now answered several important questions about game state.

- What is game state?
- How do we recognize it?
- Where should it be stored?
- What should be allowed to change?
- Who owns each piece of information?

The next challenge is practical.

> **How do we create a single object that owns the game's shared state?**

In the next section, we'll build a **Game Manager** to do exactly that.