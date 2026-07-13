# Operation 0.2.3 — Scale Object

## Classification

**Type:** Operation
**Category:** Object Placement
**Difficulty:** Beginner
**Estimated Time:** 5 seconds

---

## Purpose

Scaling an object changes its size in the scene.

This operation allows an object to become:

* larger
* smaller
* taller
* wider
* thinner

without changing its position or orientation.

A useful mental model is:

> Movement changes where an object is.
>
> Rotation changes which direction it faces.
>
> Scaling changes how large it is.

---

## When Would I Use This?

Use this operation whenever:

* An object is too large
* An object is too small
* You want to create variation
* You need an object to fit a space
* You are prototyping an environment
* You are adjusting proportions

Examples:

* Make a tree taller
* Make a platform wider
* Create a giant crystal
* Create a miniature house
* Adjust the dimensions of a wall

---

## Prerequisites

Before beginning:

* A scene exists
* An object exists in the scene
* The object can be selected

Examples:

```text
MeshInstance3D
Node3D
Camera3D
Light3D
```

---

## Procedure

### Step 1 — Select the Object

Click the object in the Scene Tree or viewport.

Example:

```text
Tree
```

or

```text
Platform
```

or

```text
Building
```

---

### Step 2 — Enter Scale Mode

Use the scale tool.

In most cases, this is done with:

```text
R
```

or by clicking the scale tool icon in the editor toolbar.

The transform gizmo should display scale handles.

---

### Step 3 — Scale the Object

Click and drag one of the scale handles.

The object will change size along the selected axis.

Common axes:

* **X** = width
* **Y** = height
* **Z** = depth

---

### Step 4 — Adjust as Needed

Continue scaling until the desired size is achieved.

You may also enter exact values in:

```text
Transform
→ Scale
```

within the Inspector.

---

## Success Check

You should now have:

✓ A selected object

✓ A modified scale

✓ An object that better fits the scene

Example:

```text
Before:
Tiny Tree

After:
Large Tree
```

---

## Common Examples

### Create a Large Tree

```text
Scale
(1,1,1)

↓

(3,5,3)
```

Result:

A taller and wider tree.

---

### Create a Wide Platform

```text
Scale
(1,1,1)

↓

(10,1,4)
```

Result:

A large platform suitable for player movement.

---

### Create Environmental Variation

Start with:

```text
Rock
```

Create several copies.

Scale them differently.

Result:

The environment appears more natural and less repetitive.

---

## Common Mistakes

### Mistake 1

Using Scale when a mesh property would be better.

Example:

Scaling a PlaneMesh to create a large ground plane.

Result:

Texture stretching and unexpected behavior.

Solution:

When possible, modify the mesh dimensions directly.

For example:

```text
PlaneMesh
→ Size
```

rather than:

```text
Transform
→ Scale
```

---

### Mistake 2

Creating extremely large scales.

Example:

```text
(1000,1000,1000)
```

Result:

Navigation and placement become difficult.

Solution:

Use reasonable scale values.

---

### Mistake 3

Creating extremely small scales.

Example:

```text
(0.01,0.01,0.01)
```

Result:

Objects become difficult to see and manipulate.

Solution:

Work at sensible scene scales.

---

### Mistake 4

Scaling collision geometry unintentionally.

Result:

Collisions may no longer match expectations.

Solution:

Always verify collision behavior after significant scaling.

---

### Mistake 5

Scaling parent nodes without realizing it.

Result:

All child objects scale as well.

Solution:

Understand hierarchy relationships before scaling.

---

## Why This Matters

Scale is one of the primary ways developers communicate importance.

Consider:

```text
Small Statue
Large Statue
```

Even if they use the same mesh, they create very different impressions.

Scale helps establish:

* importance
* mood
* realism
* visual hierarchy

---

## Design Insight

Beginning developers often think:

> Bigger is better.

Experienced designers think:

> Size communicates meaning.

Examples:

| Large Objects | Suggest    |
| ------------- | ---------- |
| Castle        | Power      |
| Mountain      | Scale      |
| Monument      | Importance |

| Small Objects | Suggest       |
| ------------- | ------------- |
| Trinket       | Detail        |
| Collectible   | Precision     |
| Creature      | Vulnerability |

Scale is a storytelling tool as much as a technical operation.

---

## Special Note: Mesh Size vs Transform Scale

There are two common ways to make an object larger:

### Option 1 — Scale the Object

```text
Transform
→ Scale
```

---

### Option 2 — Change the Mesh Dimensions

Example:

```text
BoxMesh
→ Size
```

or

```text
PlaneMesh
→ Size
```

For many primitive meshes, modifying the mesh dimensions directly is preferred.

This often produces:

* cleaner geometry
* more predictable texturing
* fewer hierarchy complications

As a general rule:

> If you want a different object size, consider adjusting the mesh first.
>
> Use Transform Scale when you want to resize the entire object hierarchy.

---

## Professional Practice

Professional developers frequently use scale during prototyping.

A common workflow is:

```text
Create Primitive
↓
Scale Primitive
↓
Test Layout
↓
Replace With Final Asset
```

This allows environments to be built rapidly before final art assets exist.

---

## Relationship to Other Transform Operations

The three primary transform operations are:

### Move

Changes:

```text
Position
```

---

### Rotate

Changes:

```text
Orientation
```

---

### Scale

Changes:

```text
Size
```

Together these form the foundation of object placement.

---

## Related Operations

* 0.2.1 Move Object
* 0.2.2 Rotate Object
* 0.2.4 Parent Objects
* 0.0.4 Focus Selected Object
* 0.3.2 Assign Mesh

---

## Related Techniques

This operation supports the following techniques:

* Scene Composition
* Level Design
* Environmental Storytelling
* Object Placement
* Rapid Prototyping