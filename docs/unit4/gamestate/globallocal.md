# 4.1.3 Local vs Global State

## Classification

**Type:** Design / Engineering Guide

**Category:** Game Architecture

**Difficulty:** Intermediate

---

# Design Problem

Once you've identified a piece of game state, another question immediately appears.

> **Where should this information be stored?**

Some information belongs to a single object.

Other information belongs to the entire game.

Choosing the right place to store information is one of the most important design decisions in software engineering.

---

# Why This Matters

Imagine a game with several enemies.

Each enemy needs to remember:

- its own health
- whether it has seen the player
- its current movement speed

Should every enemy share the same health value?

Of course not.

Each enemy owns its own information.

Now consider the player's score.

Should every enemy have its own separate copy of the score?

Again, no.

There is only one score.

The entire game should share it.

Some information is **local**.

Some information is **global**.

---

# Mental Model

Think about asking two questions.

## Who owns this information?

and

## Who needs to use it?

The answers usually tell you where the state belongs.

---

## Local State

Local state belongs to a single object.

Only that object is responsible for updating it.

Examples include:

- an enemy's health
- a door's open/closed status
- a moving platform's speed
- a light's color
- a projectile's remaining lifetime

Each object keeps track of its own information.

```text
Enemy A
    health = 20

Enemy B
    health = 50

Enemy C
    health = 10
```

Each enemy has different state.

---

## Global State

Global state describes the game as a whole.

Many different objects may need to access it.

Examples include:

- current score
- current level
- player lives
- game difficulty
- paused/unpaused
- settings volume

There is only one copy.

```text
Current Score = 1250

Player Lives = 3

Difficulty = Hard
```

Everyone refers to the same information.

---

# Comparing Local and Global State

| Local State | Global State |
|--------------|--------------|
| Belongs to one object | Belongs to the entire game |
| Usually updated by one object | May be used by many objects |
| Many copies exist | Usually only one copy exists |
| Example: Enemy Health | Example: Player Score |

---

# Design Principle

## Information should live with the object that owns it.

If only one object needs a piece of information, it usually belongs there.

If many systems need the same information, it may belong somewhere shared.

Keeping information close to its owner makes programs easier to understand and maintain.

---

# Practical Observation

Beginning programmers often choose one of two extremes.

Some make everything global.

Others make everything local.

Both approaches create problems.

If everything is global, it becomes difficult to know which object is responsible for changing it.

If everything is local, objects constantly need to ask one another for information.

Good software design finds an appropriate balance.

---

# Common Misconceptions

### "Global means better."

No.

Global information is available everywhere, but that also means more systems can accidentally change it.

Global state should be used carefully.

---

### "Local information can't affect the rest of the game."

It can.

A local change can trigger events that influence many other systems.

The information itself is still owned locally.

---

### "Every object needs access to everything."

Usually not.

Well-designed systems give each object access only to the information it actually needs.

---

### "Duplicating information is harmless."

Imagine every enemy keeping its own copy of the player's score.

Eventually, one copy becomes different from the others.

Now which one is correct?

Keeping a single owner for important information prevents this problem.

---

# Reflection

For each piece of information below, decide whether it is usually local or global.

| Information | Local or Global? |
|--------------|------------------|
| Enemy Health | |
| Current Score | |
| Door Open | |
| Player Lives | |
| Volume Setting | |
| Current Weapon | |
| Puzzle Solved | |
| Coins Collected | |

Can you explain **who owns** each piece of information?

---

# Looking Ahead

We've learned that some information belongs to individual objects, while other information belongs to the game as a whole.

The next question becomes:

> **If the game needs shared information, where should that shared state live?**