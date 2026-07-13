# 5.7.2 Local Rules

## Classification

**Type:** Design / Engineering Guide

**Category:** Procedural Systems

**Difficulty:** Intermediate

---

# Design Problem

Imagine a world made of thousands of cells.

Suppose every cell follows one simple rule.

Perhaps:

- become a wall if most neighbors are walls
- become water if surrounded by water
- become grass if enough neighboring cells contain grass
- spread fire to neighboring trees

Each individual decision seems almost trivial.

But what happens when every location follows the same rule?

The answer is often surprising.

Large-scale structure begins to emerge.

---

# Why This Matters

Many computational systems are built from local rules.

Examples include:

- cave generation
- erosion simulation
- fire propagation
- disease spread
- crystal growth
- fluid simulation
- image filters

None of these algorithms understand the entire world.

Each location makes decisions using only nearby information.

Complex behavior emerges from simple local interactions.

---

# Mental Model

Imagine a neighborhood.

Every house follows the same rule.

```text
Look Around

↓

Make Decision

↓

Repeat
```

No house knows the layout of the entire city.

Each responds only to its immediate surroundings.

Over time...

the entire city changes.

Computational systems work in much the same way.

---

# Representation

Suppose every location begins with one of two values.

```text
Wall

or

Open
```

Each location repeatedly asks:

> **What do my neighbors look like?**

Then applies one rule.

```text
Observe Neighbors

↓

Apply Rule

↓

Become New Value
```

The rule is local.

The result becomes global.

---

# Dissecting the Strategy

Notice something remarkable.

No location ever asks:

```text
What does the entire world look like?
```

Instead, every location asks only:

```text
Who are my neighbors?
```

That tiny question is repeated across every location.

The repeated local decisions gradually transform the entire world.

---

# Design Principle

## Complex systems often emerge from simple local rules.

Many natural-looking patterns require surprisingly little information.

Rather than designing the final artifact directly...

...design the local behavior.

The larger structure often emerges naturally.

---

# Examples

Many different systems use local rules.

| System | Local Decision |
|----------|----------------|
| Cave Generation | Majority of neighboring cells |
| Fire Simulation | Burning neighbors |
| Crystal Growth | Nearby crystals |
| Disease Spread | Nearby infected cells |
| Image Blur | Neighboring pixel values |
| Terrain Smoothing | Nearby elevations |

Although these systems appear unrelated...

...they all follow the same computational strategy.

---

# Practical Observation

Beginning programmers often try to describe the finished world.

Professional programmers often describe the behavior of one location.

The computer repeats that behavior everywhere.

This shift—from designing artifacts to designing rules—is one of the most important ideas in procedural generation.

---

# Common Misconceptions

### "Every local rule produces interesting results."

No.

Many simple rules quickly produce boring or repetitive patterns.

Designing effective local rules is part of the creative process.

---

### "The algorithm understands the whole world."

Not necessarily.

Many local-rule systems never examine anything beyond the immediate neighborhood.

The larger behavior emerges automatically.

---

### "Local rules are random."

Not usually.

Most local-rule systems are entirely deterministic.

The same initial conditions produce the same results.

Randomness is often used only to generate the starting world.

---

### "This idea only applies to Cellular Automata."

Not at all.

Cellular Automata are one example of a much broader computational strategy.

Many procedural systems rely on repeated local decision-making.

---

# Reflection

Imagine creating one of the following.

- a cave
- a forest
- a fire simulation
- a population model
- an image filter

Could each location make decisions using only nearby information?

Would the entire world still develop interesting structure?

Why?

---

# Looking Back

Earlier we discovered that randomness introduces variation.

Local rules introduce something different.

They introduce **organization**.

Rather than describing the finished artifact...

...we describe how individual locations behave.

The artifact emerges from repeated interaction.

---

# Looking Ahead

One family of procedural algorithms uses local rules to transform worlds.

Perhaps the most famous example is **Cellular Automata**.

We'll explore it as one example of this broader computational strategy before moving on to other ways computers generate structure.