# 5.2.6 Transform

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Operations

**Difficulty:** Beginner

---

# Design Problem

Suppose we have an image.

Every pixel has a brightness value.

```text
20
45
80
120
...
```

How could we make the entire image brighter?

Or suppose we have a sound.

How could we make every sample quieter?

Or perhaps a game world.

How could we raise the height of every tile?

None of these problems involve changing just one value.

Instead, we want to change **every** value according to the same rule.

This operation is called **transformation**.

---

# Why This Matters

Transformation is one of the most powerful ideas in computation.

Rather than changing information one value at a time...

...we describe a rule.

The computer applies that rule to every value in the representation.

Examples include:

- brightening an image
- scaling terrain heights
- increasing audio volume
- offsetting coordinates
- converting walls into passages
- translating game objects

Many computational systems are built almost entirely from repeated transformations.

---

# Mental Model

Think of a rubber stamp.

You carve one design into the stamp.

Then you press it onto many pieces of paper.

The rule stays the same.

Only the values change.

Transformation works similarly.

```text
Representation

↓

Apply Rule

↓

New Representation
```

The rule is repeated for every element.

---

# Starter Implementation

Suppose we have a list of numbers.

```python
values = [
    1,
    2,
    3,
    4
]
```

We want to double every value.

```python
result = [
    value * 2
    for value in values
]
```

Result:

```text
2

4

6

8
```

The original list remains unchanged.

The transformation produces a new representation.

---

Now imagine an image.

Instead of numbers...

...the values represent pixels.

```text
30

60

120

200
```

The transformation

```text
Brightness × 2
```

produces

```text
60

120

240

255
```

(The final value would normally be limited to the maximum brightness.)

The operation is identical.

Only the meaning of the values has changed.

---

The same idea appears in digital audio.

```text
Samples

↓

Multiply every sample by 0.5

↓

Quieter Sound
```

And in terrain generation.

```text
Heights

↓

Add 10

↓

Higher Terrain
```

The medium changes.

The operation remains transformation.

---

# Dissecting the Operation

Transformation asks one question.

```text
Given one value...

↓

What should it become?
```

The same rule is applied repeatedly.

```text
1

↓

2

----------------

2

↓

4

----------------

3

↓

6
```

Every value is transformed independently.

---

# Design Principle

## Describe the rule once.

Let the computer apply it many times.

One of the greatest strengths of computation is repeating the same transformation accurately and consistently across thousands—or millions—of values.

---

# Experiment

Suppose you have each of the following.

Describe a transformation.

| Representation | Possible Transformation |
|----------------|-------------------------|
| Image | |
| Sound | |
| Tile Map | |
| Height Map | |
| Enemy Health | |
| Distance Field | |

Notice that every example applies one rule to many values.

---

# Practical Observation

Transformation is one of the most reusable ideas in computing.

Many seemingly unrelated algorithms are actually repeated transformations.

For example:

- converting grayscale into color
- increasing image contrast
- scaling a waveform
- offsetting coordinates
- smoothing terrain
- applying cellular automata rules

Although the results look very different...

...the computational operation is often exactly the same.

---

# Common Misconceptions

### "Transformation modifies the original representation."

Not necessarily.

Many transformations produce a completely new representation while preserving the original.

---

### "Every value must transform differently."

Usually not.

Most transformations apply one consistent rule across every value.

The power comes from repeating that rule many times.

---

### "Transformation is only useful for mathematics."

No.

Images, sound, maps, simulations, procedural worlds, and game data all rely heavily on transformation.

It is one of the most fundamental operations in computational creation.

---

### "Transformation only changes numbers."

Not at all.

Any representation can be transformed.

Numbers, colors, coordinates, strings, pixels, samples, tiles, and many other kinds of information can all be transformed according to appropriate rules.

---

# Reflection

Think about one computational artifact.

- an image
- a sound
- a maze
- a tile map

Imagine applying one simple rule repeatedly.

What new artifact might emerge?

Now ask yourself:

Could a complicated result emerge from a surprisingly simple transformation?

---

# Looking Ahead

Transformation changes every value according to a rule.

Often, however, one transformation is not enough.

The same operation must be repeated many times.

The next question becomes:

> **How can we apply an operation over and over again to build increasingly complex systems?**