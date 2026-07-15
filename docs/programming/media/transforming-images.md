# 5.5.4 Transform Images

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Media

**Difficulty:** Beginner

---

# Design Problem

Suppose we already have an image.

Perhaps every pixel stores a brightness value.

```text
20

45

80

120

...
```

Now imagine we want to:

- brighten the image
- darken the image
- invert the colors
- increase the contrast
- create a gradient

Notice something.

The image already exists.

We are not creating a new picture from scratch.

Instead, we are changing the values that already exist.

This process is called **image transformation**.

---

# Why This Matters

Most computational images are not drawn manually.

Instead, they are created through repeated transformations.

Examples include:

- gradients
- procedural textures
- height maps
- distance fields
- image filters
- terrain maps

Every one of these begins with the same idea.

Transform the value stored at each pixel.

---

# Mental Model

Think of an image as a spreadsheet.

Every cell contains a number.

Changing the spreadsheet means changing the numbers.

Images work exactly the same way.

```text
Pixels

↓

Apply Rule

↓

New Pixels

↓

New Image
```

The picture changes because the underlying values change.

---

# Starter Example

Suppose our image contains the following pixel values.

```text
20

40

80

160
```

Now apply one simple rule.

```text
Multiply every value by 2
```

The result becomes

```text
40

80

160

255
```

(The final value is limited to the maximum brightness.)

The transformation changed every pixel.

The image itself changed automatically.

---

Another example.

```text
Pixel

↓

255 - Pixel
```

A dark pixel becomes bright.

A bright pixel becomes dark.

The same image now has an entirely different appearance.

Again...

The only thing that changed was the rule.

---

# Dissecting the Transformation

Notice that every transformation asks the same question.

```text
Given one pixel...

↓

What should its new value become?
```

The computer repeats that question for every pixel.

One simple rule.

Thousands—or millions—of applications.

---

# Design Principle

## Images are transformed one pixel at a time.

Complex visual effects often emerge from surprisingly simple rules applied consistently across every pixel.

The computer performs the repetition.

We design the rule.

---

# Experiment

Imagine each of the following transformations.

What happens to the image?

| Rule | Visual Result |
|------|---------------|
| Double every value | |
| Halve every value | |
| Invert every value | |
| Replace every value with 128 | |
| Add 50 to every value | |

Can you describe the image without actually generating it?

---

# Practical Observation

One of the most important discoveries in computational media is that the same transformation often appears across many different domains.

For example:

```text
Brightness × 2
```

makes an image brighter.

```text
Height × 2
```

creates taller terrain.

```text
Amplitude × 2
```

creates louder audio.

The representation changes.

The operation remains the same.

Transformation is one of the most reusable ideas in computation.

---

# Common Misconceptions

### "Transformations create new images."

Not necessarily.

Sometimes they produce new representations.

Sometimes they modify existing ones.

The important idea is that pixel values change according to a rule.

---

### "Every pixel needs its own rule."

Usually not.

Most transformations apply one consistent rule across every pixel.

The complexity emerges from repetition.

---

### "Drawing and transformation are different."

Often they are the same process.

Many procedural images are never "drawn."

They emerge entirely through repeated transformations.

---

### "Image processing is unique."

Not at all.

The same transformation ideas appear in:

- audio
- terrain
- simulations
- procedural generation

Only the meaning of each value changes.

---

# Reflection

Imagine one of the following.

- a grayscale image
- a height map
- a cave representation

Can you think of one simple rule that would completely change its appearance?

Now ask yourself:

Did you really change the image...

...or did you simply change the values?

---

# Looking Ahead

Transforming images is only the beginning.

Some transformations produce remarkably interesting patterns.

The next challenge is creating representations that describe distance itself.

> **How can simple mathematical relationships produce surprisingly beautiful computational images?**