---
tags: [technique, enemy]
---

# 8.4.3 Investigation

## Classification

**Type:** Engineering Technique

**Category:** Enemy Behaviour

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine an enemy chasing the player.

The player turns a corner.

Hides behind a wall.

The enemy reaches the corner...

...but the player is gone.

What should happen?

Should the enemy:

- instantly forget?
- continue chasing forever?

Neither usually feels believable.

Instead...

the enemy begins searching.

This behaviour is often called **Investigation**.

---

# Why This Matters

Investigation creates uncertainty.

The enemy no longer knows exactly where the player is.

Instead...

it explores the last known location before deciding what to do next.

This creates opportunities for:

- stealth
- planning
- escape
- tension

The player is no longer simply running.

They are hiding.

---

# Mental Model

Think about losing sight of a friend in a crowd.

You do not immediately give up.

You first look around.

Only after searching do you decide they have gone.

Games work the same way.

```text
Player Seen

↓

Player Lost

↓

Search

↓

Return
```

The enemy reacts naturally to incomplete information.

---

# Starter Workflow

A simple enemy might follow this sequence.

```text
Patrol

↓

Player Detected

↓

Chase

↓

Player Lost

↓

Investigate

↓

Return To Patrol
```

Investigation becomes the bridge between chasing and normal behaviour.

---

# Dissecting the System

Notice what changes.

Earlier the enemy asked:

```text
Where is the player?
```

Now the question becomes:

```text
Where was the player?
```

The behaviour changes because the enemy's knowledge changes.

Investigation is driven by uncertainty rather than certainty.

---

# Design Principle

## React to uncertainty.

Interesting AI does not always know the correct answer.

Sometimes the most believable behaviour comes from acting on incomplete information.

Searching creates opportunities for suspense and player decision making.

The enemy appears thoughtful rather than mechanical.

---

# Practical Observation

Investigation often follows a simple pattern.

```text
Last Known Position

↓

Move There

↓

Look Around

↓

Wait

↓

Return To Patrol
```

Even this small amount of searching makes enemies feel significantly more aware of the world.

Complex intelligence often begins with simple behaviours.

---

# Common Misconceptions

### "Losing sight should immediately stop the chase."

Usually not.

Searching the last known location often creates much more interesting gameplay.

---

### "Investigation requires complicated AI."

Not necessarily.

Many games create convincing investigation using only:

- one destination
- a short delay
- a return to patrol

Simple systems can feel remarkably believable.

---

### "The enemy should always find the player."

Not at all.

Investigation creates opportunities for players to:

- hide
- distract
- outsmart

The uncertainty is part of the gameplay.

---

### "Investigation is only for stealth games."

Many action and adventure games also use investigation to make enemy behaviour feel more natural.

It creates transitions between combat and exploration.

---

# Reflection

Imagine creating a guard.

The player disappears behind a wall.

How should the guard respond?

- run to the last location?
- wait?
- search nearby?
- immediately return to patrol?

Which behaviour would feel the most believable?

Why?

---

# Looking Back

Earlier we explored:

- Patrol
- Chase

Now we've added another important behaviour.

Enemies do not always possess perfect information.

Sometimes they must search.

Investigation makes the world feel more believable because enemies react to what they know rather than what the player knows.

The behaviour becomes driven by knowledge instead of certainty.

---

# Looking Ahead

Enemies can now:

- patrol
- chase
- investigate

Eventually...

they reach the player.

How should they respond?

How do we create:

- melee attacks
- ranged attacks
- projectiles
- combat encounters

that feel responsive and engaging?

We'll begin exploring:

> **Combat**