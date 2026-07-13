# Technique 2.1 — Create a Collider

## Classification

**Type:** Engineering Technique

**Category:** Physical Interaction

**Difficulty:** Beginner

**Estimated Time:** 15–20 minutes

---

# Design Problem

Until now, every object in our worlds has been purely visual.

Players can see:

* cubes
* trees
* walls
* buildings

But the physics engine cannot.

As far as the engine is concerned, these objects have no physical presence.

To make an object participate in the physical world, it must be given a **Collider**.

---

# Why This Technique Matters

A collider tells the engine:

> **"This object occupies space."**

Once an object has a collider, it can begin participating in interactions such as:

* collisions
* triggers
* physics
* movement constraints

Without a collider, objects simply pass through one another.

---

# Starter Implementation

Create the following hierarchy.

```text
Wall
├── MeshInstance3D
└── CollisionShape3D
```

Assign:

* A **BoxMesh** to the MeshInstance3D.
* A **BoxShape3D** to the CollisionShape3D.

Run the scene.

Although nothing visible has changed, your object now has both:

* a visual representation
* a physical representation

---

# Dissecting the Scene

Notice that two different nodes now describe the same object.

```text
MeshInstance3D
```

determines:

> What the player sees.

---

```text
CollisionShape3D
```

determines:

> What the physics engine sees.

These two representations often resemble one another, but they serve completely different purposes.

---

# Design Principle

## Every interactive object has two identities.

The player experiences:

```text
Appearance
```

The engine simulates:

```text
Collision
```

Good game development keeps those ideas separate.

---

# Experiment

Create a simple cube.

Now try three versions.

---

### Version A

Only:

```text
MeshInstance3D
```

Run the project.

Observe.

---

### Version B

Add:

```text
CollisionShape3D
```

Assign a BoxShape.

Observe.

---

### Version C

Delete the mesh.

Keep only the collider.

Observe.

Ask yourself:

What changed?

What didn't?

---

# Practical Observation

The player cannot normally see collision geometry.

That does **not** mean it isn't there.

Many important systems in games are invisible:

* collisions
* triggers
* navigation meshes
* spawn points

As developers, we often work with systems the player never directly sees.

---

# Common Misconceptions

### "The Mesh is the Collider."

No.

Meshes are visual.

Colliders are physical.

---

### "Adding a CollisionShape makes the object visible."

No.

CollisionShapes are usually invisible during gameplay.

---

### "Every Mesh automatically collides."

It does not.

Collision must be created intentionally.

---

### "The player interacts with the mesh."

The player actually interacts with the collider.

The mesh simply provides visual feedback.

---

# Reflection

Complete the sentence:

> A Mesh describes...

Complete the sentence:

> A Collider describes...

Now answer:

Why do game engines separate these two ideas instead of combining them into one object?

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain the purpose of a CollisionShape?

✓ Can I distinguish between appearance and interaction?

✓ Can I build an object with both a mesh and a collider?

✓ Can I explain why an invisible collider is still important?

---

# Looking Ahead

Creating a collider is only the first step.

The next question becomes:

> **What shape should that collider have?**

A cube?

A sphere?

A capsule?

Choosing the right collision shape is one of the most important design decisions in building interactive worlds.
