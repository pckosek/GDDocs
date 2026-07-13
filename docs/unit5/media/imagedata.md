# 5.5.1 Images as Data

## Classification

**Type:** Design / Engineering Guide

**Category:** Computational Media

**Difficulty:** Beginner

---

# Design Problem

When you look at a digital image...

...you see a picture.

A computer does not.

The computer sees:

- numbers
- locations
- colors

Nothing more.

Every digital image is simply a representation of information arranged across space.

Understanding this idea changes the way we think about images.

Instead of asking:

> **How do I draw a picture?**

we begin asking:

> **What information does each location contain?**

---

# Why This Matters

Images appear throughout game development.

Examples include:

- textures
- sprites
- height maps
- normal maps
- procedural textures
- user interface graphics
- lighting masks

Although these images look different...

...they all share the same underlying representation.

They are collections of values arranged on a grid.

Once we understand that representation...

...we can begin creating images ourselves.

---

# Mental Model

Earlier in this unit we represented a world using a grid.

```text
□ □ □ □

□ □ □ □

□ □ □ □
```

An image works exactly the same way.

Instead of storing:

- walls
- trees
- enemies

each location stores a color.

```text
255

120

90

...

```

The representation has changed.

The underlying structure has not.

An image is simply another kind of gridworld.

---

# Representation

Think about one pixel.

```text
□
```

By itself...

...it contains only one piece of information.

Perhaps:

```text
Brightness = 180
```

Now imagine thousands of these pixels arranged together.

```text
□□□□□□□□□□□□

□□□□□□□□□□□□

□□□□□□□□□□□□
```

Together they become an image.

No single pixel is interesting.

The pattern formed by many pixels is.

---

# Design Principle

## Images are representations before they are pictures.

The computer never stores "a tree."

It stores many individual pixel values.

Our eyes interpret those values as a tree.

Separating representation from appearance is one of the most important ideas in computational media.

---

# Examples

Different kinds of images store different information.

| Image Type | One Pixel Represents |
|------------|----------------------|
| Grayscale Image | Brightness |
| Color Image | Color |
| Height Map | Elevation |
| Distance Field | Distance |
| Tile Mask | Category |
| Collision Map | Walkable / Blocked |

Although they look different...

...they are all grids of values.

---

# Practical Observation

Beginning programmers often think about drawing shapes.

Professional programmers often think about assigning values.

Instead of asking:

> How do I draw a circle?

they begin asking:

> Which pixels should belong to the circle?

That small change in thinking makes procedural image generation much more approachable.

---

# Common Misconceptions

### "Images are pictures."

Not to a computer.

Images are collections of values.

The picture is something our brains perceive.

---

### "Every pixel stores a color."

Not necessarily.

Some images store:

- heights
- temperatures
- terrain types
- transparency
- lighting
- distances

A pixel is simply one location containing one piece of information.

---

### "Images are different from gridworlds."

Structurally, they are remarkably similar.

Both represent two-dimensional space as many individual cells.

The only difference is what each cell represents.

---

### "The image is the important part."

Usually the representation is.

Once we understand the representation...

...we can create many different visualizations from the same data.

---

# Reflection

Consider the following.

Suppose every pixel represented:

- terrain height
- enemy danger
- temperature
- water depth

Would those still be images?

Or would they simply be visualizations of different kinds of information?

Now ask yourself:

What really makes something an image?

---

# Looking Back

Earlier in this unit we discovered that computers represent worlds using grids.

Now we've discovered something surprising.

Images are also grids.

The representation is almost identical.

Only the meaning of each cell has changed.

---

# Looking Ahead

Now that we understand what an image really is...

...the next question becomes:

> **What information does one individual pixel actually contain?**