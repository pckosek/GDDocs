# 5.7.4 Sampling

## Classification

**Type:** Design / Engineering Guide

**Category:** Procedural Systems

**Difficulty:** Intermediate

---

# Design Problem

Imagine creating a forest.

You need to place hundreds of trees.

Where should they go?

Should they be arranged in perfect rows?

```text
T   T   T   T

T   T   T   T

T   T   T   T
```

Probably not.

Should they be placed completely at random?

```text
TT

      T

          TT
```

That often creates awkward clusters.

Instead...

...we usually want something in between.

A distribution that feels natural.

The computational strategy of placing objects throughout space is called **Sampling**.

---

# Why This Matters

Sampling appears throughout procedural generation.

Examples include:

- forests
- rocks
- flowers
- enemy placement
- treasure placement
- Voronoi regions
- terrain features
- procedural cities

Although these applications look very different...

...they all begin with the same question.

> **Where should objects exist?**

---

# Mental Model

Imagine throwing seeds across a field.

Every seed becomes the starting point for something larger.

```text
Space

↓

Sample Locations

↓

Structure
```

The locations themselves are often simple.

The interesting artifacts emerge later.

Many procedural systems begin not with objects...

...but with carefully chosen sample points.

---

# Sampling Strategies

Different computational systems answer the placement question differently.

Some examples include:

| Strategy | General Idea |
|-----------|--------------|
| Uniform Sampling | Even spacing |
| Random Sampling | Completely random positions |
| Jittered Sampling | Regular structure with small variations |
| Blue Noise Sampling | Evenly distributed randomness |
| Poisson Disc Sampling | Minimum separation distance |
| Voronoi Seeds | Representative regions |

Although the strategies differ...

...they are all solving the same computational problem.

---

# Dissecting the Strategy

Notice that sampling usually happens **before** the interesting artifact appears.

For example:

```text
Choose Locations

↓

Grow Forest
```

or

```text
Choose Seeds

↓

Construct Voronoi Regions
```

or

```text
Place Sample Points

↓

Generate Terrain Features
```

The samples provide the foundation.

Later algorithms build upon them.

---

# Design Principle

## Placement influences everything that follows.

Sampling is often one of the earliest decisions in a procedural system.

Small differences in how objects are distributed can dramatically change the final artifact.

Good sampling creates opportunities for later algorithms.

---

# Experiment

Suppose you are generating each of the following.

How might you choose sample locations?

| System | What Is Being Sampled? |
|----------|------------------------|
| Forest | |
| Dungeon | |
| Stars | |
| Villages | |
| Treasure | |
| Rivers | |

Now ask yourself:

Would every application benefit from the same sampling strategy?

Why or why not?

---

# Practical Observation

Beginning programmers often think about placing objects.

Professional programmers often think about distributing points.

Those points later become:

- trees
- enemies
- caves
- regions
- structures
- gameplay elements

Separating sampling from generation makes procedural systems much easier to experiment with.

Changing only the sampling strategy often produces entirely different worlds.

---

# Common Misconceptions

### "Sampling is randomness."

Not exactly.

Many sampling strategies use randomness.

Others are completely deterministic.

Sampling is about **distribution**, not randomness.

---

### "Every procedural system uses Poisson Disc Sampling."

No.

Poisson Disc Sampling is one member of a much larger family of sampling strategies.

Different problems require different distributions.

---

### "The sampled points are the final artifact."

Usually not.

Sample points often become the starting point for much larger computational processes.

---

### "Better sampling always means more randomness."

Often the opposite.

Many of the most natural-looking procedural systems carefully limit randomness to create balanced spatial distributions.

---

# Reflection

Imagine creating a Zelda-style world.

You need to place:

- forests
- caves
- villages
- enemies
- treasures

Would you use exactly the same sampling strategy for every one?

Why?

Now ask yourself:

What characteristics make a spatial distribution feel natural?

---

# Looking Back

Randomness introduced variation.

Local rules introduced organization.

Traversal introduced growth.

Sampling introduces **distribution**.

Instead of asking:

> "What should happen?"

Sampling asks:

> **"Where should it happen?"**

---

# Looking Ahead

Sampling determines where things begin.

Another family of procedural systems approaches the world differently.

Instead of distributing points...

...it assigns a value to every location in space.

The next computational strategy becomes:

> **Fields.**