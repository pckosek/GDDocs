---
tags: [technique, enemy]
---

# 8.4.5 Navigation

## Classification

**Type:** Engineering Technique

**Category:** Enemy Behaviour

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine an enemy wants to reach the player.

The player stands on the other side of a wall.

Should the enemy:

- walk directly into the wall?
- instantly teleport?
- magically know the correct path?

Ideally...

the enemy should find a route around the obstacle.

Godot provides a navigation system to help solve this problem.

Rather than teaching enemies how to think...

...we teach the world where movement is possible.

---

# Why This Matters

Navigation allows gameplay objects to move intelligently through complex environments.

Examples include:

- enemies
- NPCs
- companions
- animals

Rather than moving directly toward a target...

they follow paths through the walkable world.

---

# Mental Model

Think about asking a navigation app for directions.

You provide:

- where you are
- where you want to go

The app determines the route.

Games work similarly.

```text
Destination

↓

Navigation

↓

Path

↓

Movement
```

The gameplay decides **where**.

The navigation system helps decide **how**.

---

# NavigationRegion2D

A **NavigationRegion2D** describes the parts of the world that can be traversed.

```text
Walkable Area

↓

Navigation Region
```

The region represents the world.

It does not move anything.

It simply describes where movement is possible.

---

# NavigationAgent2D

A **NavigationAgent2D** belongs to an object that wishes to move.

For example:

```text
Enemy

└── NavigationAgent2D
```

The agent requests a path.

The gameplay script moves the enemy toward the next point along that path.

The agent guides.

The enemy still performs the movement.

---

# Dissecting the System

Notice the responsibilities.

```text
NavigationRegion2D

↓

World Information
```

```text
NavigationAgent2D

↓

Path Information
```

```text
Enemy

↓

Movement
```

Each system performs one responsibility.

Navigation remains independent from enemy behaviour.

---

# Design Principle

## Describe the world.

Don't hardcode paths.

Good navigation systems allow the environment to describe where movement is possible.

Enemies simply ask:

> **How can I reach this destination?**

The navigation system provides a route.

The enemy follows it.

---

# Practical Observation

Many beginning projects attempt to manually script every movement path.

As worlds become larger...

navigation becomes much easier when the environment itself describes walkable space.

Changing the level automatically changes the available paths.

Enemy behaviour remains the same.

---

# Common Misconceptions

### "Navigation moves the enemy."

Not directly.

The NavigationAgent2D calculates paths.

Your movement code still moves the character.

---

### "Navigation replaces enemy AI."

No.

The State Machine still decides:

- patrol
- chase
- investigate

Navigation simply helps each state reach its destination.

---

### "Every enemy needs unique navigation."

Usually not.

Many enemies can share the same navigation system.

Only their behaviours and destinations differ.

---

### "Navigation always finds the perfect solution."

Navigation finds a path through the walkable world.

The gameplay still decides whether following that path is appropriate.

---

# Reflection

Imagine an enemy trying to reach the player.

Which system should decide:

| Question | System |
|----------|--------|
| Where can I walk? | |
| Where should I go? | |
| How do I move? | |

Notice that these are different responsibilities.

Why might keeping them separate make the project easier to maintain?

---

# Looking Back

Earlier we explored:

- patrol
- chase
- investigation
- combat

Now we've given those behaviours a way to move through complex worlds.

Enemy behaviour decides the destination.

Navigation finds the route.

Movement follows the path.

The systems cooperate while remaining independent.

---

# Looking Ahead

Enemies can now:

- patrol
- chase
- investigate
- fight
- navigate

The final challenge is bringing all of these behaviours together into one memorable encounter.

We'll begin exploring:

> **Boss Design**