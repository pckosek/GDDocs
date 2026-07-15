# 5.5.2 Pixels

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Media

**Difficulty:** Beginner

---

# Design Problem

If an image is a collection of information...

...what exactly is being stored?

Suppose we zoom into one tiny part of an image.

Eventually, we reach the smallest unit that can still hold information.

That unit is called a **pixel**.

Every digital image is built from many individual pixels.

Understanding pixels means understanding how computers represent images.

---

# Why This Matters

Pixels are one of the most fundamental representations in digital media.

Examples include:

- photographs
- game textures
- sprites
- icons
- procedural textures
- height maps
- distance fields

Although these artifacts look very different...

...they are all collections of pixels.

The only difference is what each pixel represents.

---

# Mental Model

Think of a mosaic.

From far away...

...you see one picture.

Up close...

...you see thousands of individual tiles.

Digital images work the same way.

```text
Image

↓

Pixels

↓

Values
```

Each pixel stores one piece of information.

Together...

they create something much larger than any individual pixel.

---

# Representation

Imagine a tiny image.

```text
□ □ □

□ □ □

□ □ □
```

Each square represents one pixel.

Every pixel stores a value.

For example:

```text
255

120

80

...
```

Individually, these values have little meaning.

Together...

they become an image.

---

# Design Principle

## Complex images emerge from many simple pixels.

A single pixel rarely contains interesting information.

The structure created by many neighboring pixels is what produces recognizable shapes, textures, and patterns.

Large computational artifacts often emerge from many simple components working together.

---

# Examples

Pixels may represent many different things.

| Image | One Pixel Represents |
|--------|----------------------|
| Grayscale Image | Brightness |
| Color Image | Color |
| Height Map | Elevation |
| Distance Field | Distance |
| Procedural Texture | Pattern Value |
| Collision Mask | Walkable / Blocked |

The representation changes.

The idea of the pixel remains the same.

---

# Practical Observation

Beginning programmers often think about drawing lines, circles, and shapes.

Computers do not.

Computers change one pixel at a time.

Every image, regardless of complexity, is ultimately constructed by assigning values to individual pixels.

Understanding pixels makes procedural image generation much easier to understand.

---

# Common Misconceptions

### "A pixel is a tiny square."

Not exactly.

A pixel is one location that stores one value.

We often draw pixels as squares because it makes them easier for people to see.

---

### "Pixels always represent colors."

No.

Many computational images store entirely different kinds of information.

Color is simply one common interpretation.

---

### "Pixels know about one another."

No.

Each pixel stores only its own value.

Relationships between pixels emerge from their arrangement and from the algorithms that examine neighboring pixels.

---

### "Large pixels create better images."

Usually the opposite.

Smaller pixels allow more detailed representations because more information can be stored across the image.

---

# Reflection

Suppose one pixel represented each of the following.

- height
- temperature
- danger level
- water depth
- terrain type

Would those still be pixels?

Or would they simply be different interpretations of the same representation?

Now ask yourself:

Is a pixel defined by its color...

...or by its role as one location storing one value?

---

# Looking Ahead

Every pixel stores information.

The next question becomes:

> **What kinds of information can a pixel actually contain?**

We'll begin by exploring one of the simplest image representations:

> **Grayscale images.**