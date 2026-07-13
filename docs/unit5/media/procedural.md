# 5.5.6 Procedural Patterns

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Media

**Difficulty:** Intermediate

---

# Design Problem

Imagine beginning with a blank image.

Every pixel is identical.

Nothing interesting exists.

Now suppose we apply one simple mathematical rule.

Perhaps:

- distance from the center
- brightness based on position
- a cosine wave
- random variation

Suddenly...

patterns begin to appear.

Not because we drew them.

Because the computation created them.

This is one of the central ideas of computational media.

---

# Why This Matters

Many digital artists never paint individual pixels.

Instead...

...they design mathematical processes.

Those processes produce:

- gradients
- rings
- ripples
- checkerboards
- interference patterns
- procedural textures
- terrain

The computer becomes a creative instrument.

The artwork emerges from the algorithm.

---

# Mental Model

Think about planting one seed.

From that single seed...

...an entire tree grows.

Procedural patterns work similarly.

```text
Simple Rule

↓

Repeated Computation

↓

Complex Pattern
```

The beauty comes from repetition.

Not complexity.

---

# Examples

Suppose every pixel stores:

```text
Distance from Center
```

The image naturally forms circles.

---

Suppose every pixel stores:

```text
Brightness = X Coordinate
```

The image becomes a gradient.

---

Suppose every pixel stores:

```text
cos(distance)
```

The image becomes concentric rings.

---

Suppose every pixel stores:

```text
Random Noise
```

The image becomes texture.

The rule changes.

The computational process remains remarkably similar.

---

# Dissecting the Pattern

Notice something interesting.

The algorithm never says:

```text
Draw Circle
```

Instead, it says:

```text
Compute Distance
```

The circles appear naturally.

Likewise...

The algorithm never says:

```text
Draw Ripples
```

Instead, it repeatedly applies:

```text
Cosine
```

The ripples emerge automatically.

Patterns are often consequences rather than intentions.

---

# Design Principle

## Interesting artifacts often emerge from simple rules.

The computer excels at repeating simple operations consistently.

Rather than designing every detail...

...design the rule.

Then explore the results.

Small changes in the rule often produce dramatically different artifacts.

---

# Experiment

Suppose you begin with the same blank image.

Now imagine changing only one thing.

| Rule | Possible Result |
|------|-----------------|
| Distance | |
| Random Values | |
| Cosine | |
| Checkerboard | |
| Height Function | |
| Noise | |

How might each image differ?

What stayed the same?

---

# Practical Observation

One of the joys of computational media is experimentation.

A programmer might spend an afternoon changing:

- one constant
- one mathematical function
- one neighborhood
- one transformation

The resulting image may become completely different.

The code barely changes.

The creative possibilities expand dramatically.

This is one reason procedural art is so engaging.

Tiny computational changes often produce unexpectedly beautiful results.

---

# Common Misconceptions

### "Procedural images are random."

Sometimes.

Many procedural images contain no randomness at all.

They emerge entirely from deterministic mathematics.

---

### "The computer is creating the artwork."

Not exactly.

The programmer designs the computational process.

The computer faithfully executes it.

Creativity comes from designing interesting rules.

---

### "Complicated images require complicated algorithms."

Often the opposite is true.

Many memorable procedural patterns emerge from remarkably simple computations repeated across an entire image.

---

### "These ideas only apply to graphics."

No.

The same ideas appear throughout computational media.

Simple rules generate:

- sounds
- terrain
- caves
- mazes
- textures
- animations

The medium changes.

The computational thinking remains remarkably consistent.

---

# Reflection

Imagine beginning with nothing but:

- a blank image
- one mathematical rule
- repetition

What kinds of patterns might emerge?

Now ask yourself:

If you changed only one line of the algorithm...

Would you still be creating the same artwork?

Or a completely different one?

---

# Looking Back

This section explored a surprising idea.

Images are not fundamentally pictures.

They are representations.

By transforming those representations through computation...

...we discovered that mathematics itself can produce rich visual structure.

Gradients.

Distance fields.

Patterns.

Textures.

All emerged from the same computational ideas.

Representation.

Transformation.

Repetition.

---

# Looking Ahead

Images are only one kind of computational media.

The same ideas apply to another fascinating medium.

Instead of pixels...

...we now turn our attention to samples.

The next question becomes:

> **How can computers represent and generate sound?**