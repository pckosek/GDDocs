# Technique 1.1 — Create Ground

## Classification

**Type:** Technique

**Category:** Scene Construction

**Difficulty:** Beginner

**Estimated Time:** 10–20 minutes

---

# Design Problem

Every world needs somewhere to exist.

Before a player can explore, jump, drive, fly, or build, there must first be a world for those actions to occur within.

Ground establishes the physical and visual foundation of that world.

Although creating a plane may seem like a simple technical task, it is often the first design decision you make. The size, appearance, and scale of the ground immediately begin shaping how the player experiences the environment.

---

# Why This Technique Matters

Ground is one of the most common structures in game development.

Whether you're creating:

* a platformer
* a flight simulator
* an RPG
* a puzzle game
* an open-world environment

the player needs a reference point.

Ground provides that reference.

It establishes:

* scale
* orientation
* visual composition
* navigable space

Almost every project in this course will begin with some variation of this technique.

---

# Operations Used

This technique combines several Unit 0 Operations.

Required Operations:

* Create a New Scene
* Add a Child Node
* Assign a Mesh
* Move an Object
* Scale an Object
* Assign a Material
* Modify Material Properties
* Run a Scene

Helpful Supporting Operations:

* Zoom View
* Orbit View
* Focus Selected Object

---

# Recipe

The general workflow is:

```text
Create Scene
        ↓
Add MeshInstance3D
        ↓
Assign PlaneMesh
        ↓
Resize PlaneMesh
        ↓
Assign Material
        ↓
Modify Material
        ↓
Run Scene
```

The result should be a simple environment that is ready to support additional objects and gameplay.

---

# Design Principle

## Every world begins with a place to stand.

Beginning developers often think of ground as "just the floor."

Game designers think of it differently.

Ground establishes the first impression of a world.

A grassy field, a polished metal platform, an icy lake, and a glowing alien surface may all use exactly the same geometry.

What changes is the experience.

Small design decisions made here influence everything that follows.

---

# Experiment

Instead of building one version, build three.

### Version A

A plain white plane.

No material.

---

### Version B

A simple colored material.

Choose a color that feels natural.

---

### Version C

A textured surface.

Experiment with:

* grass
* stone
* sand
* metal
* wood

Do not worry about making it perfect.

Simply observe how the environment feels.

---

# Reflection

After building all three versions, consider the following questions:

* Which world felt the most inviting?
* Which felt the largest?
* Which would you want to continue building?
* What changed besides the appearance?

Write down one observation.

There is no single correct answer.

The goal is to begin noticing how visual decisions influence the player's experience.

---

# Common Mistakes

### Creating Ground That Is Too Small

Many beginning developers leave the PlaneMesh at its default size.

Ask yourself:

> Could a player actually explore this world?

If the answer is "not really," enlarge the ground.

---

### Scaling Instead of Resizing

For primitive meshes such as PlaneMesh, adjusting the mesh dimensions often produces better results than dramatically scaling the object.

---

### Forgetting Materials

Even a simple color can dramatically improve the readability of a scene.

White geometry is excellent for debugging.

Finished environments usually benefit from intentional materials.

---

# Self Check

Before moving on, ask yourself:

✓ Is there enough space to build the rest of the scene?

✓ Does the ground establish a clear sense of scale?

✓ Does the material support the atmosphere you want?

✓ Does this feel like the beginning of a world?

---

# Looking Ahead

Ground is rarely the goal.

Ground is the foundation.

Once it exists, you are ready to begin constructing:

* environments
* lighting
* reusable objects
* player movement
* physics
* gameplay

Every world starts somewhere.

This is yours.
