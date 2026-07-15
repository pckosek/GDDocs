# 4.1.2 Identify Gameplay State

## Classification

**Type:** Design / Engineering Guide

**Category:** Game Architecture

**Difficulty:** Intermediate

---

# Design Problem

Now that we know what **game state** is, the next challenge is recognizing it.

When building a game, not every piece of information deserves to be remembered.

Some things happen for only a brief moment.

Others continue to describe the world long after the original event has ended.

As game developers, one of our jobs is deciding:

> **What information must the game continue to remember?**

---

# Why This Matters

Before we can store information, we must first identify what information actually matters.

Remembering too little causes the game to forget important events.

Remembering too much makes systems unnecessarily complicated.

Good software engineering begins with deciding what information belongs in the game's memory.

---

# The Persistence Test

When you're unsure whether something is game state, ask yourself one question.

> **If the game forgot this information on the next frame, would something break?**

If the answer is **yes**, you've probably found game state.

If the answer is **no**, you're probably looking at an event or a temporary behavior instead.

---

# Examples

## Example 1

A player presses the jump button.

State?

❌ No.

The button press is an event.

---

The player has 3 lives remaining.

State?

✅ Yes.

The game must remember that number throughout the level.

---

## Example 2

A coin spins in place.

State?

❌ Usually not.

The spinning animation is temporary.

---

The player collected the coin.

State?

✅ Yes.

Otherwise the coin would immediately reappear.

---

## Example 3

An enemy walks across the room.

State?

❌ Usually not.

Walking is current behavior.

---

The enemy has 15 health remaining.

State?

✅ Yes.

The next attack depends on remembering that value.

---

## Example 4

A door opens.

State?

The opening animation?

❌ No.

The animation is temporary.

The fact that the door is open?

✅ Yes.

Future gameplay depends on remembering that information.

---

# Practice

Decide whether each example represents game state.

| Situation | Game State? | Why? |
|------------|-------------|------|
| Player Health | ✅ | Must persist |
| Mouse Click | ❌ | Temporary event |
| Current Score | ✅ | Affects future gameplay |
| Explosion Animation | ❌ | Temporary visual effect |
| Inventory Items | ✅ | Must be remembered |
| Timer Value | ✅ | Describes the current game |
| Enemy Patrol Animation | ❌ | Current behavior |
| Selected Weapon | ✅ | Determines future actions |

---

# Design Principle

## Good games remember only what future gameplay depends upon.

Not everything needs to be stored.

The game only needs to remember information that will influence future decisions.

---

# Practical Observation

When beginners first start programming games, they often try to repeat events over and over.

Experienced programmers usually do something different.

Instead of repeating the event...

...they remember its result.

For example:

```text
Player collects key
        ↓
has_key = true
```

The game never needs to replay the collection event.

It only needs to remember that the player now has the key.

---

# Common Misconceptions

### "Everything that changes is game state."

No.

Animations, sounds, and button presses all change over time.

Many are temporary events rather than lasting state.

---

### "Only numbers are game state."

No.

Game state can be:

- numbers
- true/false values
- references to objects
- collections of objects
- text
- many other kinds of information

---

### "If something is visible, it must be state."

Not necessarily.

Many visual effects exist only for a single moment.

The important question is not whether the player can see it.

The important question is whether the game needs to remember it.

---

# Reflection

Think about one of your favorite games.

Identify five pieces of game state that the game must remember while you play.

Now ask yourself:

Which of those pieces of information could the game safely forget?

Which could it never forget?

Why?

---

# Looking Ahead

Once we've identified what information the game needs to remember, the next question becomes:

> **Where should that information be stored?**