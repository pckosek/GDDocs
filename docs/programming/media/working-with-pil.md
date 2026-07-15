# 5.5.3 Creating Images (PIL)

## Classification

**Type:** Engineering Technique

**Category:** Computational Media

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

So far, we've learned that:

- images are representations
- images are collections of pixels
- every pixel stores information

But our pixels still exist only as ideas inside our program.

How can we transform those values into an image that we can actually see?

Python's **Pillow (PIL)** library provides exactly that capability.

PIL allows us to visualize pixel data as an image file.

---

# Why This Technique Matters

Computers naturally work with numbers.

Humans naturally work with pictures.

PIL acts as a bridge between those two worlds.

Instead of looking at:

```text
255

120

90

...

```

we can produce:

```text
████████████
████░░░████
██░░░░░░███
...
```

or even save a PNG image.

Visualization allows us to inspect, debug, and explore computational representations.

---

# Starter Implementation

Begin by importing Pillow.

```python
from PIL import Image
```

Create a blank grayscale image.

```python
width = 128
height = 128

img = Image.new(
    "L",
    (width, height)
)
```

The image now exists.

At the moment...

every pixel is black.

Finally, save the result.

```python
img.save("blank.png")
```

You have created your first computational image.

---

# Dissecting the Technique

Notice that we never "draw."

Instead, we create a representation.

```text
Image

↓

Width

↓

Height

↓

Pixels
```

PIL simply provides a way to store and visualize that representation.

The image itself is still just a collection of pixel values.

---

# Design Principle

## Build the representation first.

Visualize it second.

Good computational systems separate:

- the information
- the visualization

The representation determines what the image contains.

PIL simply displays it.

---

# Experiment

Suppose you create:

```python
Image.new("L", (32,32))
```

Then:

```python
Image.new("L", (512,512))
```

What changed?

What remained the same?

Now ask yourself:

Did either image become more complicated...

...or simply larger?

---

# Practical Observation

Professional programmers rarely generate images by drawing individual shapes.

Instead, they generate pixel values using computational rules.

Later in this unit we'll produce images representing:

- gradients
- distance fields
- procedural textures
- cellular automata
- terrain
- random distributions

Every one of these begins with the same simple image object.

The creativity comes from the pixel values.

---

# Common Misconceptions

### "PIL creates pictures."

Not exactly.

PIL creates image objects.

The picture emerges from the values assigned to the pixels.

---

### "Drawing comes first."

Usually the representation comes first.

Visualization simply allows us to inspect it.

---

### "Images require artistic ability."

Not necessarily.

Many computational images emerge entirely from mathematical or algorithmic processes.

Programming becomes another creative medium.

---

### "The image stores the algorithm."

No.

The image stores only the final representation.

The algorithm is what produced it.

---

# Reflection

Imagine generating each of the following.

- a checkerboard
- a gradient
- a maze
- a cave
- a height map

Would PIL create those directly?

Or would your algorithm first create the pixel values?

Now ask yourself:

What is PIL actually responsible for?

---

# Looking Ahead

Our image now exists.

The next question becomes:

> **How can we assign meaningful values to every pixel instead of leaving the image blank?**