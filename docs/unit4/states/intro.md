# 4.4.1 What is a State?

## Classification

**Type:** Design / Engineering Guide

**Category:** Game Architecture

**Difficulty:** Intermediate

---

# Design Problem

Earlier in this unit, we learned that games remember information.

Examples included:

- player health
- score
- inventory
- current level

That information describes **the game**.

Now consider a player character.

At any given moment, the player might be:

- standing still
- walking
- jumping
- falling
- climbing
- attacking

These are not pieces of information like score or health.

They describe **the player's current behavior.**

This is another kind of state.

---

# Why This Matters

As games become more complex, objects often have many different behaviors.

Without some way to organize those behaviors, code quickly becomes difficult to understand.

Imagine trying to answer questions like:

- Can the player jump while climbing?
- Can an enemy attack while defeated?
- Can a door be both opening and closing?

Thinking in terms of **states** helps organize these behaviors.

Instead of asking:

> "What should happen?"

we begin asking:

> **"What state is this object currently in?"**

---

# Mental Model

Behavioral state describes **what an object is currently doing.**

For example:

```text
Player

↓

Idle

Walking

Jumping

Falling

Attacking
```

At any given moment, the player is usually in **one** of these states.

As gameplay changes...

...the player's state changes too.

---

Think of a traffic light.

```text
Red

↓

Green

↓

Yellow
```

The light is always in one state.

Changing behavior simply means changing states.

---

# Two Meanings of "State"

Earlier, we discussed **Game State**.

Now we're introducing **Behavioral State**.

Although they share the same word, they answer different questions.

| Game State | Behavioral State |
|-------------|------------------|
| Score | Walking |
| Health | Jumping |
| Inventory | Attacking |
| Current Level | Falling |
| Coins Collected | Idle |

Game state describes **facts about the game.**

Behavioral state describes **what an object is currently doing.**

Both are important.

They simply solve different problems.

---

# Design Principle

## Behavior becomes easier to manage when only one state is active at a time.

Instead of asking hundreds of independent questions...

```text
Is Walking?

Is Jumping?

Is Falling?

Is Climbing?

Is Attacking?
```

we can simply ask:

> **"What state am I in?"**

This often produces code that is easier to read and reason about.

---

# Practical Observation

Many beginning programmers build behavior using long chains of conditions.

```text
if jumping...

if climbing...

if attacking...

if falling...

if swimming...

...
```

As more abilities are added, these chains become increasingly difficult to maintain.

Organizing behavior into states provides a clearer way to think about the problem.

---

# Common Misconceptions

### "Behavioral state replaces game state."

No.

Games need both.

Game state remembers information.

Behavioral state organizes behavior.

---

### "An object can only ever have one kind of state."

Objects often have many kinds of state.

For example:

```text
Player

Health = 85

Inventory = 12 Items

Current State = Jumping
```

These describe different aspects of the same object.

---

### "Changing state means changing objects."

No.

The object stays the same.

Only its current behavior changes.

---

### "States are only for players."

Many different objects use states.

Examples include:

- enemies
- elevators
- doors
- traffic lights
- menus
- NPCs

Any object whose behavior changes over time may benefit from using states.

---

# Reflection

Think about the following objects.

What behavioral states might each one have?

| Object | Possible States |
|----------|-----------------|
| Player | |
| Enemy | |
| Door | |
| Elevator | |
| Traffic Light | |

Now ask yourself:

Can each object perform all of those behaviors at the same time?

Or is it usually in one state before changing to another?

---

# Looking Ahead

Understanding behavioral states is only the beginning.

Our code now needs a way to represent those states.

The next question becomes:

> **How can we give each state a clear, meaningful name?**