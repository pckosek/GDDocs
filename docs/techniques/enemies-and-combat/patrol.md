---
tags: [technique, enemy]
---

# 8.4.1 Patrol

## Classification

**Type:** Engineering Technique

**Category:** Enemy Behaviour

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine entering a dungeon.

An enemy walks back and forth through a hallway.

The player immediately begins asking questions.

- Can I sneak past?
- Should I wait?
- Should I attack?
- Is there another route?

The enemy has not even noticed the player.

Yet its movement has already changed the player's decisions.

Patrol is more than movement.

It shapes the player's experience of the world.

---

# Why This Matters

Patrolling enemies make worlds feel inhabited.

Instead of standing perfectly still...

they create movement, uncertainty, and opportunities for decision making.

Patrol behaviour supports:

- exploration
- stealth
- combat
- timing
- observation

The enemy becomes another part of the environment.

---

# Mental Model

Think about a security guard walking through a museum.

The guard is not chasing anyone.

They simply follow a routine.

Visitors naturally adjust their own behaviour in response.

Games work exactly the same way.

```text
Enemy Patrol

↓

Player Observes

↓

Player Decides
```

The patrol creates gameplay before combat ever begins.

---

# Starter Implementation

Earlier we built patrol behaviour using a State Machine.

```text
Patrol

↓

Reach Waypoint

↓

Next Waypoint

↓

Patrol
```

The behaviour itself has not changed.

What has changed is its purpose.

The patrol is no longer demonstrating AI.

It is shaping the player's experience of the world.

---

# Dissecting the System

Notice the relationship.

```text
Enemy Movement

↓

Player Information

↓

Player Decision
```

The patrol communicates:

- safe moments
- dangerous areas
- predictable routines

The player begins planning around the enemy's behaviour.

---

# Design Principle

## Behaviour creates opportunities.

A patrolling enemy is not simply an obstacle.

Its predictable movement creates choices.

Should the player:

- wait?
- sneak?
- fight?
- explore elsewhere?

Good enemy behaviour encourages interesting decisions rather than constant combat.

---

# Practical Observation

Many beginning projects treat patrol as background animation.

In practice...

patrol often becomes an important level design tool.

Changing:

- speed
- path
- pauses
- direction

can dramatically alter how the player experiences the same environment.

The movement communicates information.

---

# Common Misconceptions

### "Patrol exists only before combat."

Not necessarily.

Many enemies return to patrol after losing the player.

Patrol often becomes the enemy's normal state.

---

### "Random movement is more realistic."

Usually not.

Predictable patrol routes allow players to observe, plan, and make meaningful decisions.

Consistency often creates better gameplay than unpredictability.

---

### "Patrol only matters for stealth games."

Patrolling enemies influence exploration, pacing, and combat in many different genres.

Even action games benefit from enemies that make the world feel active.

---

### "Patrol is only about movement."

Movement is only the visible part.

Patrol changes how players think about the world around them.

---

# Reflection

Imagine placing a patrolling enemy in a dungeon.

How might changing:

- the patrol route
- the patrol speed
- the waiting time

change the player's decisions?

Would the player:

- attack immediately?
- wait?
- explore another route?

How does the patrol create gameplay before the battle even begins?

---

# Looking Back

Earlier we implemented patrol as an enemy behaviour.

Now we've returned to it with a different perspective.

Patrol is not simply movement.

It is communication.

It helps players understand the world, anticipate danger, and make thoughtful decisions.

The enemy becomes another part of the level's design.

---

# Looking Ahead

Patrol creates predictable behaviour.

Sometimes, however...

the enemy notices something unusual.

A sound.

A movement.

The player.

How should the enemy respond?

We'll begin exploring:

> **Chase**