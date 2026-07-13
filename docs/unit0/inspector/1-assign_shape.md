# Operation 0.3.1 — Assign a Shape

## Classification

**Type:** Operation
**Category:** Inspector Operations
**Difficulty:** Beginner
**Estimated Time:** 30 seconds

---

## Purpose

Assigning a shape gives a **CollisionShape2D** or **CollisionShape3D** node a geometric boundary that can participate in collision detection.

Without a shape, a collision node has no physical presence.

A CollisionShape node without a shape is similar to:

> A cardboard box with nothing inside it.

The node exists, but Godot has no information about its size, boundaries, or volume.

---

## When Would I Use This?

Use this operation whenever you need an object to:

* collide with other objects
* block movement
* detect overlap
* trigger events
* participate in physics

Examples:

* Player hitboxes
* Enemy hitboxes
* Walls
* Floors
* Triggers
* Pickups
* Interactive objects

---

## Prerequisites

Before beginning:

* A scene exists
* A CollisionShape node exists

Examples:

```text
CollisionShape2D
```

or

```text
CollisionShape3D
```

---

## Procedure

### Step 1 — Select the CollisionShape Node

In the Scene Tree, click:

```text
CollisionShape3D
```

or

```text
CollisionShape2D
```

---

### Step 2 — Locate the Shape Property

In the Inspector, locate:

```text
Shape
```

This field is often empty when the node is first created.

Example:

```text
Shape: <empty>
```

---

### Step 3 — Create a Shape Resource

Click the dropdown arrow beside the Shape property.

Select:

```text
New BoxShape3D
```

or another appropriate shape type.

Common 3D choices include:

| Shape           | Typical Use              |
| --------------- | ------------------------ |
| BoxShape3D      | Crates, walls, buildings |
| SphereShape3D   | Balls, planets           |
| CapsuleShape3D  | Characters               |
| CylinderShape3D | Columns, barrels         |

Common 2D choices include:

| Shape            | Typical Use      |
| ---------------- | ---------------- |
| RectangleShape2D | Platforms, walls |
| CircleShape2D    | Pickups, bullets |
| CapsuleShape2D   | Characters       |

---

### Step 4 — Adjust the Shape Properties

After creating the shape, additional properties become available.

Examples:

```text
Size
Radius
Height
```

Modify these values until the shape matches the intended object.

---

### Step 5 — Verify the Collision Boundary

The shape should now appear in the viewport.

Most collision shapes are displayed as colored wireframes or outlines while editing.

Example:

```text
Player
└── CollisionShape3D
```

with a visible capsule outline surrounding the player.

---

## Success Check

You should now have:

✓ A CollisionShape node

✓ A shape resource assigned

✓ A visible collision boundary

✓ A collision object that can participate in physics

---

## Common Mistakes

### Mistake 1

Creating a CollisionShape node but never assigning a shape.

Example:

```text
CollisionShape3D
Shape: <empty>
```

Result:

The object has no collision boundary.

Solution:

Always assign a shape resource.

---

### Mistake 2

Choosing a shape that poorly matches the object.

Example:

A very large box around a small player.

Result:

Collisions feel inaccurate.

Solution:

Choose the simplest shape that reasonably approximates the object.

---

### Mistake 3

Making the collision shape much larger than the visual object.

Result:

Players collide with invisible space.

Solution:

Check the viewport and compare the collision boundary to the visible model.

---

### Mistake 4

Making the collision shape too small.

Result:

Objects partially pass through walls or appear to clip into geometry.

Solution:

Ensure the shape adequately covers the object.

---

## Why This Matters

Most physics systems rely on collision shapes.

Without them:

* players fall through floors
* walls cannot block movement
* triggers cannot activate
* pickups cannot be collected

Collision shapes are the invisible geometry that defines how objects interact.

---

## Design Insight

An important concept for beginners:

> Collision geometry and visual geometry are not the same thing.

The visible object might be highly detailed.

The collision shape is usually much simpler.

Example:

```text
Tree
├── MeshInstance3D
└── CollisionShape3D
```

The tree mesh may contain hundreds or thousands of polygons.

The collision shape might simply be:

```text
CapsuleShape3D
```

This is faster and easier for the physics engine to process.

---

## Professional Practice

Professional developers rarely use exact visual geometry for collisions.

Instead they create simplified collision shapes.

Examples:

| Visual Object | Collision Shape |
| ------------- | --------------- |
| Character     | Capsule         |
| Crate         | Box             |
| Coin          | Sphere          |
| Pillar        | Cylinder        |
| Building      | Multiple Boxes  |

Simple collision shapes improve performance and reduce unexpected behavior.

---

## Relationship to Resources

When you assign a shape, you are actually assigning a:

```text
Shape Resource
```

Examples:

```text
BoxShape3D
SphereShape3D
CapsuleShape3D
RectangleShape2D
CircleShape2D
```

This is why Assign Shape is a specialized example of the broader operation:

```text
0.3.0 Assign Resource
```

---

## Related Operations

* 0.3.0 Assign a Resource
* 0.3.2 Assign a Mesh
* 0.3.3 Assign a Material
* 0.3.4 Save a Resource
* 0.2.2 Run Scene

---

## Related Techniques

This operation supports the following techniques:

* Collision Detection
* Physics Setup
* Trigger Zones
* Character Controllers
* Interactive Objects