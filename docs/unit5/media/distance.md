# 5.5.5 Distance Fields

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Media

**Difficulty:** Intermediate

---

# Design Problem

Imagine placing a single point in the center of an image.

```text
□ □ □ □ □

□ □ □ □ □

□ □ X □ □

□ □ □ □ □

□ □ □ □ □
```

Now ask a different question.

Instead of asking:

> What color should each pixel be?

ask:

> **How far away is each pixel from the center?**

Every pixel now represents a distance.

The image has become a **distance field**.

---

# Why This Matters

Distance fields appear throughout computational media.

Examples include:

- procedural textures
- lighting
- terrain generation
- collision detection
- navigation
- image effects
- signed distance fields (SDFs)

Although the applications differ...

...they all begin with the same representation.

Each location stores its distance from something.

---

# Mental Model

Imagine dropping a pebble into a still pond.

Ripples spread outward.

The farther from the center...

...the larger the distance.

A distance field measures that relationship.

```text
Center

↓

Distance

↓

Every Location
```

Instead of storing color...

every pixel stores geometry.

---

# Representation

Suppose this location is the center.

```text
□ □ □

□ X □

□ □ □
```

The center pixel has distance:

```text
0
```

Nearby pixels have small distances.

Faraway pixels have larger distances.

The image gradually changes because the stored values gradually change.

Nothing has been drawn.

The pattern emerges entirely from computation.

---

# Dissecting the Representation

Notice something remarkable.

The algorithm does not know anything about circles.

It simply asks:

```text
For every pixel...

↓

How far am I from the center?
```

The resulting values naturally form circular patterns.

Geometry emerges from repeated computation.

---

# Design Principle

## Store relationships instead of appearances.

Distance fields do not store circles.

They store distances.

The circles appear because many locations share the same distance.

Representing relationships often produces surprisingly rich visual structure.

---

# Experiment

Suppose you create distance fields measured from:

| Reference Point | Result |
|-----------------|--------|
| Image Center | |
| Upper-Left Corner | |
| Bottom Edge | |
| Two Different Points | |
| A Line | |

How might each visualization differ?

---

# Practical Observation

Distance fields are one of the first examples where mathematics begins producing images that feel artistic.

The algorithm itself is remarkably simple.

The richness comes from applying the same computation to every pixel.

Later in this course we'll transform these distance fields into:

- gradients
- rings
- ripples
- terrain
- procedural textures

The distance field becomes the raw material for many other computational artifacts.

---

# Common Misconceptions

### "A distance field stores colors."

No.

It stores distances.

The colors are simply one way of visualizing those distances.

---

### "The algorithm draws circles."

Not at all.

The algorithm computes distances.

Our eyes interpret equal-distance regions as circles.

---

### "Distance fields are only useful for graphics."

No.

Distance fields appear in:

- robotics
- navigation
- game AI
- physics
- procedural generation
- simulation

They are fundamentally geometric representations.

---

### "Distance fields are complicated."

The underlying idea is surprisingly simple.

Every location answers exactly one question:

> **How far am I from something?**

Complex visual effects emerge from repeating that question across an entire representation.

---

# Reflection

Imagine computing the distance from every location to:

- the nearest tree
- the player
- a river
- a wall
- the edge of the world

Would those still be distance fields?

What kinds of gameplay systems could use them?

Now ask yourself:

Are you storing pictures...

...or are you storing geometry?

---

# Looking Back

Earlier we transformed images by changing pixel values.

Distance fields reveal something even more interesting.

Pixel values do not have to represent appearance.

They can represent relationships.

Geometry.

Structure.

Meaning.

Images become another way of visualizing computation.

---

# Looking Ahead

Distance fields reveal beautiful patterns through mathematics.

The next challenge is discovering that even simple repeating functions can produce rich computational textures.

> **How can mathematical patterns become computational art?**