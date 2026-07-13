# Operation 0.2.4 — Create a Transform Hierarchy

## Classification

**Type:** Operation
**Category:** Object Placement
**Difficulty:** Beginner
**Estimated Time:** 1 minute

---

## Purpose

Creating a transform hierarchy allows multiple objects to be linked together so that one object controls the movement, rotation, and scale of another.

In Godot, this is accomplished using **parent** and **child** relationships.

A useful mental model is:

> A parent leads.
>
> A child follows.

When a parent moves, rotates, or scales, its children inherit those transformations.

---

## When Would I Use This?

Use this operation whenever multiple objects should behave as a single system.

Examples:

* A planet orbiting a star
* A camera attached to a player
* A wheel attached to a vehicle
* A weapon attached to a character
* A light attached to a moving object
* Decorative objects attached to a structure

This operation is one of the foundations of scene construction in Godot.

---

## Why Not Move Everything Individually?

Imagine a car made from:

```text
Car Body
Wheel 1
Wheel 2
Wheel 3
Wheel 4
Camera
```

Without a hierarchy:

```text
Move Body
Move Wheel 1
Move Wheel 2
Move Wheel 3
Move Wheel 4
Move Camera
```

Every object must be repositioned separately.

With a hierarchy:

```text
Car
├── Wheel 1
├── Wheel 2
├── Wheel 3
├── Wheel 4
└── Camera
```

Moving the parent automatically moves everything else.

---

## Prerequisites

Before beginning:

* A scene exists
* At least two objects exist

Examples:

```text
Planet
Moon
```

or

```text
Player
Camera
```

---

## Procedure

### Step 1 — Identify the Parent

Determine which object should control the group.

Example:

```text
Player
```

or

```text
Vehicle
```

or

```text
Planet
```

This object will become the parent.

---

### Step 2 — Create or Select the Child

Identify the object that should follow the parent.

Example:

```text
Camera
```

or

```text
Wheel
```

or

```text
Moon
```

---

### Step 3 — Place the Child Under the Parent

In the Scene Tree, drag the child node onto the parent node.

Example:

Before:

```text
World
├── Player
└── Camera
```

After:

```text
World
└── Player
    └── Camera
```

---

### Step 4 — Verify the Relationship

Expand the parent node.

The child should appear beneath it.

Example:

```text
Vehicle
├── Wheel1
├── Wheel2
├── Wheel3
└── Wheel4
```

---

### Step 5 — Test the Hierarchy

Move the parent.

Observe that the child moves with it.

Rotate the parent.

Observe that the child rotates with it.

This confirms the hierarchy is functioning correctly.

---

## Success Check

You should now have:

✓ A parent object

✓ A child object

✓ A hierarchy relationship

✓ Transform inheritance

Example:

```text
Player
└── Camera
```

Moving the player also moves the camera.

---

## Common Examples

### Camera Following a Player

```text
Player
└── Camera3D
```

Result:

The camera automatically follows the player.

---

### Solar System

```text
Sun
└── Planet
    └── Moon
```

Result:

The moon follows the planet.

The planet follows the sun.

---

### Vehicle Construction

```text
Vehicle
├── WheelFL
├── WheelFR
├── WheelBL
├── WheelBR
└── Camera
```

Result:

All components move together.

---

### Weapon Attachment

```text
Player
└── Sword
```

Result:

The sword moves with the player.

---

## Common Mistakes

### Mistake 1

Choosing the wrong parent.

Result:

Objects inherit unexpected movement.

Solution:

Ask:

> Which object should control the others?

---

### Mistake 2

Creating extremely deep hierarchies.

Example:

```text
A
└── B
    └── C
        └── D
            └── E
```

Result:

The scene becomes difficult to understand.

Solution:

Keep hierarchies as simple as possible.

---

### Mistake 3

Forgetting that children inherit rotation.

Result:

Objects rotate unexpectedly.

Solution:

Remember that movement, rotation, and scale all propagate through the hierarchy.

---

### Mistake 4

Moving a child when the parent should move.

Result:

The hierarchy becomes harder to manage.

Solution:

Whenever possible, move the highest-level object responsible for the group.

---

## Why This Matters

Transform hierarchies are one of the core ideas behind Godot.

Many complex systems are built from simple parent-child relationships.

Examples:

* vehicles
* cameras
* orbiting systems
* character equipment
* UI systems
* animated structures

Without hierarchies, these systems become much more difficult to manage.

---

## Design Insight

A hierarchy creates relationships.

Consider:

```text
Camera
```

floating independently.

versus:

```text
Player
└── Camera
```

The second version communicates intent.

The camera belongs to the player.

Hierarchy is one of the primary ways developers express those relationships.

---

## Professional Practice

Professional developers use hierarchies constantly.

A common workflow is:

```text
Create Object
↓
Create Supporting Objects
↓
Organize Into Hierarchy
↓
Test Transform Inheritance
```

Many large projects consist primarily of carefully organized hierarchies.

---

## Relationship to Other Transform Operations

The previous transform operations affect a single object:

```text
Move
Rotate
Scale
```

Transform Hierarchies affect groups of objects.

For example:

```text
Vehicle
├── Wheels
├── Camera
└── Lights
```

Moving the parent affects the entire system.

This makes hierarchies one of the most powerful organizational tools in the engine.

---

## Related Operations

* 0.2.1 Move Object
* 0.2.2 Rotate Object
* 0.2.3 Scale Object
* 0.1.1 Add a Child Node
* 0.1.5 Instantiate a Scene

---

## Related Techniques

This operation supports the following techniques:

* Hierarchical Motion
* Scene Organization
* Camera Systems
* Vehicle Construction
* Procedural Animation
* World Building