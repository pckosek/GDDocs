# Operation 0.0.2 — Pan the View

## Classification

**Type:** Operation
**Category:** Editor Navigation
**Difficulty:** Beginner
**Estimated Time:** 5 seconds

---

## Purpose

Panning allows you to move the viewport sideways, up, or down without changing the viewing direction.

Unlike orbiting, which rotates the camera around a focal point, panning shifts the entire view laterally.

A useful mental model is:

> Orbiting turns your head.
>
> Panning slides your chair.

---

## When Would I Use This?

Use this operation whenever:

* An object is partially off-screen
* You need to reposition your view
* You are building a large environment
* You want to inspect neighboring objects
* You need a better composition without changing viewing angle

In practice:

> Panning is often used immediately after orbiting.

---

## Prerequisites

Before beginning:

* A scene is open
* The viewport is visible

A visible object is recommended.

---

## Procedure

### Step 1 — Position the Cursor Over the Viewport

Move the mouse into the 3D viewport.

Example:

```text
Perspective
```

view.

---

### Step 2 — Hold Shift + Middle Mouse Button

Press and hold:

```text
Shift
```

while also holding:

```text
Middle Mouse Button
```

---

### Step 3 — Move the Mouse

Move the mouse.

The camera should slide sideways relative to its current orientation.

Notice that:

* the viewing angle remains unchanged
* the focal point shifts
* the entire view moves

---

### Step 4 — Release the Controls

Release the mouse wheel and Shift key when the desired view has been reached.

---

## Success Check

You should now be able to:

✓ Move the viewport left and right

✓ Move the viewport up and down

✓ Reposition your view without rotating

✓ Explore nearby portions of the scene

---

## Common Examples

### Inspecting a Large Environment

Before:

```text
Only the center of the level is visible
```

After panning:

```text
The edge of the level becomes visible
```

without changing camera orientation.

---

### Adjusting Composition

Before:

```text
Object is near the edge of the viewport
```

After panning:

```text
Object is centered in the viewport
```

---

### Working on Nearby Objects

Before:

```text
Crate A is visible
Crate B is off-screen
```

After panning:

```text
Crate B becomes visible
```

without changing zoom level.

---

## Common Mistakes

### Mistake 1

Using orbit when panning is needed.

Result:

The viewing angle changes unnecessarily.

Solution:

Use pan when you want to move the view without rotating.

---

### Mistake 2

Using zoom to navigate horizontally.

Result:

The camera becomes too close or too far away.

Solution:

Use pan for lateral movement.

---

### Mistake 3

Panning while extremely zoomed out.

Result:

Large movements become difficult to control.

Solution:

Adjust zoom level appropriately before panning.

---

### Mistake 4

Getting lost in a large scene.

Result:

The object of interest leaves the viewport.

Solution:

Use:

```text
0.0.4 Focus Selected Object
```

to recover orientation.

---

## Why This Matters

Many scene-building tasks require precise positioning.

Sometimes the viewing angle is already correct.

The problem is simply that the object is not centered.

Panning solves this problem efficiently.

Without panning, developers often:

* rotate unnecessarily
* zoom unnecessarily
* lose their orientation

Panning provides a cleaner solution.

---

## Design Insight

Viewport navigation consists of three fundamental movements:

### Zoom

Changes distance.

```text
Closer
Farther
```

---

### Orbit

Changes angle.

```text
Left
Right
Above
Below
```

---

### Pan

Changes position.

```text
Left
Right
Up
Down
```

Understanding these three movements makes viewport navigation much easier.

---

## Professional Practice

Experienced developers constantly combine:

```text
Zoom
Orbit
Pan
```

while building scenes.

A common workflow looks like:

```text
Zoom In
↓
Orbit
↓
Pan
↓
Adjust Object
↓
Repeat
```

These operations become second nature with practice.

---

## Relationship to Other Navigation Operations

Panning works closely with:

```text
0.0.1 Zoom View
```

to control distance.

and

```text
0.0.2 Orbit View
```

to control viewing angle.

Together these three operations form the foundation of 3D viewport navigation.

---

## Related Operations

* 0.0.1 Zoom View
* 0.0.2 Orbit View
* 0.0.4 Focus Selected Object
* 0.0.5 Align View to Axis
* 0.1.0 Create a Scene

---

## Related Techniques

This operation supports the following techniques:

* Scene Navigation
* Level Design
* Environment Construction
* Object Placement
* Spatial Reasoning