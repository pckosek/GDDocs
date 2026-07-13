# 8.4.2 Chase

## Classification

**Type:** Engineering Technique

**Category:** Enemy Behaviour

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine an enemy walking along a patrol route.

The player quietly enters the room.

Should the enemy continue following its patrol forever?

Probably not.

Something important has happened.

The enemy has gained new information.

Its behaviour should change.

The patrol ends.

The chase begins.

---

# Why This Matters

Enemies become believable because they react to changes in the world.

Rather than performing one behaviour forever...

they transition between behaviours as situations change.

Examples include:

- spotting the player
- hearing a sound
- taking damage
- losing sight of the player

These events change the enemy's current state.

---

# Mental Model

Think about a security guard.

While nothing unusual happens...

they continue their patrol.

The moment they notice an intruder...

their priorities change.

```text
Patrol

↓

Player Detected

↓

Chase
```

The guard is still the same person.

Only their current behaviour has changed.

---

# Starter Workflow

A typical enemy might behave like this.

```text
Patrol

↓

Player Detected

↓

Chase

↓

Player Escapes

↓

Return To Patrol
```

The movement system changes automatically because the current state changes.

---

# Dissecting the System

Notice that the enemy is not choosing between movement algorithms.

It is choosing between states.

```text
Current State

↓

Movement Behaviour
```

When the state changes...

the movement naturally changes with it.

State controls behaviour.

---

# Design Principle

## React to information.

Enemies should change behaviour because something meaningful happened.

State transitions should represent changes in knowledge rather than occurring randomly.

The enemy behaves differently because its understanding of the world has changed.

---

# Practical Observation

Many beginning projects constantly check:

```text
Should I patrol?

Should I chase?

Should I attack?
```

State Machines simplify this process.

Instead...

the enemy asks one question.

```text
What state am I in?
```

Each state performs one behaviour.

Transitions occur only when new information appears.

---

# Common Misconceptions

### "Chase replaces patrol."

Not at all.

Patrol remains the enemy's normal behaviour.

Chase is simply another state.

The enemy often returns to patrol after losing the player.

---

### "Every enemy should chase immediately."

Different enemies respond differently.

Some investigate first.

Others attack from a distance.

The appropriate transition depends on the intended gameplay.

---

### "Chase is just faster movement."

Movement speed may change.

More importantly...

the enemy's purpose changes.

Instead of exploring the world...

it is now pursuing the player.

---

### "State transitions should happen continuously."

Usually not.

Transitions occur when meaningful events change the enemy's understanding of the situation.

---

# Reflection

Imagine creating three different enemies.

| Enemy | What Causes Chase? |
|--------|--------------------|
| Guard | |
| Wolf | |
| Robot | |

Would each enemy detect the player in the same way?

Should each return to patrol under the same conditions?

Why?

---

# Looking Back

Earlier we explored patrol behaviour.

Now we've discovered that behaviour changes over time.

Enemies become more believable because they respond to new information.

State Machines organize these changing behaviours into clear, understandable systems.

The world begins reacting to the player's actions.

---

# Looking Ahead

Sometimes the player escapes.

The enemy knows someone was there...

...but no longer knows exactly where.

What should happen next?

Should the enemy immediately return to patrol?

Or should it search the area first?

We'll begin exploring:

> **Investigation**