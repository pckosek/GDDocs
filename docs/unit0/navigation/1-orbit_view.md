# Operation 0.0.1 — Orbit the View

## Classification

**Type:** Operation
**Category:** Editor Navigation
**Difficulty:** Beginner
**Estimated Time:** 5 seconds

---

## Purpose

Orbiting allows you to rotate the viewport around a focal point without changing the location of objects in the scene.

This operation lets you observe an object from different angles while maintaining your focus on the object itself.

A useful mental model is:

> Orbiting changes where you are looking from.
>
> It does not move the object.

---

## When Would I Use This?

Use this operation whenever:

* You want to inspect an object from multiple angles
* You are positioning objects in 3D space
* You are evaluating lighting
* You are adjusting materials
* You are building environments
* You need a better perspective on a scene

In practice:

> Orbiting is one of the most frequently used navigation operations in 3D development.

---

## Prerequisites

Before beginning:

* A 3D scene is open
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

### Step 2 — Hold the Middle Mouse Button

Press and hold:

```text
Mouse Wheel Button
```

---

### Step 3 — Move the Mouse

Move the mouse while holding the wheel.

The camera should rotate around the current focal point.

---

### Step 4 — Continue Adjusting

Move the mouse until the desired viewing angle is achieved.

Release the mouse wheel when finished.

---

## Alternative Orbit Method

Many users also orbit using:

```text
Right Mouse Button
```

while moving the mouse.

The exact behavior may vary depending on editor settings and Godot version.

The goal remains the same:

> Rotate your view around the scene.

---

## Success Check

You should now be able to:

✓ View an object from multiple angles

✓ Rotate around a focal point

✓ Examine details from different perspectives

✓ Navigate a 3D scene more effectively

---

## Common Examples

### Inspecting a Model

Before:

```text
Front View Only
```

After orbiting:

```text
Front
Side
Top
Rear
```

become visible.

---

### Evaluating Lighting

Before:

```text
Only one side of the object is visible
```

After orbiting:

```text
Light and shadow behavior can be observed
```

from multiple angles.

---

### Positioning Objects

Before:

```text
Object placement appears correct
```

After orbiting:

```text
Object is revealed to be floating above the ground
```

or intersecting another object.

---

## Common Mistakes

### Mistake 1

Confusing orbiting with object rotation.

Result:

Students think they changed the object.

Solution:

Orbiting changes only the camera view.

The object remains unchanged.

---

### Mistake 2

Orbiting around empty space.

Result:

The viewport becomes difficult to control.

Solution:

Focus on an object first using:

```text
0.0.4 Focus Selected Object
```

---

### Mistake 3

Attempting to build complex scenes from a single angle.

Result:

Objects become misaligned in 3D space.

Solution:

Regularly orbit and inspect from multiple viewpoints.

---

### Mistake 4

Getting lost after excessive camera movement.

Result:

Students lose track of the scene.

Solution:

Refocus on an object and continue working.

---

## Why This Matters

3D development requires spatial awareness.

A position that looks correct from one angle may be completely wrong from another.

For example:

From the front:

```text
Cube appears centered.
```

From the side:

```text
Cube is floating several meters above the ground.
```

Orbiting helps reveal these issues.

---

## Design Insight

Many beginning developers think:

> The viewport is the world.

A more accurate understanding is:

> The viewport is a camera looking at the world.

Orbiting moves the camera.

It does not move the world.

Understanding this distinction makes many editor behaviors easier to understand.

---

## Professional Practice

Experienced level designers rarely work from a single angle.

A common workflow is:

```text
Place Object
↓
Orbit
↓
Inspect
↓
Adjust
↓
Orbit Again
```

This process repeats continuously throughout development.

---

## Relationship to Other Navigation Operations

Orbiting is usually combined with:

```text
0.0.1 Zoom View
```

to adjust distance.

and

```text
0.0.3 Pan View
```

to reposition the camera.

Together these operations provide complete control over viewport navigation.

---

## Related Operations

* 0.0.1 Zoom View
* 0.0.3 Pan View
* 0.0.4 Focus Selected Object
* 0.0.5 Align View to Axis
* 0.1.1 Add a Child Node

---

## Related Techniques

This operation supports the following techniques:

* Scene Navigation
* Level Design
* Object Placement
* Environment Construction
* Visual Inspection