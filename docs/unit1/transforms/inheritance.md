# Technique 3.3 — Parent Transform Inheritance

## Classification

**Type:** Transform Systems Technique

**Category:** Transform Systems

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Objects in a hierarchy do not exist independently.

When a parent object changes its transform, every child object must decide:

> "Should I change too?"

In Godot, the answer is almost always:

> **Yes.**

Children inherit the transforms of their parents.

This is called **Transform Inheritance**.

---

# Why This Technique Matters

Transform inheritance is one of the most important ideas in Godot.

Without it, every complex object would need to be moved piece by piece.

Imagine driving a car.

If the wheels, headlights, mirrors, and camera all had to be moved separately every frame, building even simple systems would become nearly impossible.

Instead:

```text
Vehicle
├── Wheels
├── Camera
├── Headlights
└── Driver
```

Move the Vehicle.

Everything else follows automatically.

---

# Mental Model

Imagine carrying a backpack.

As you walk:

* your backpack moves
* the books inside the backpack move
* the pencil inside the book moves

You did not move each object individually.

The movement was inherited.

Transform hierarchies behave in exactly the same way.

---

# Core Idea

Every parent controls three transformations:

* Position
* Rotation
* Scale

Every child inherits all three.

This means:

```text
Move Parent
        ↓
Children Move

Rotate Parent
        ↓
Children Rotate

Scale Parent
        ↓
Children Scale
```

This inheritance continues through every level of the hierarchy.

---

# Experiment

Create the following hierarchy:

```text id="8lshq2"
Parent Cube
└── Child Cube
```

Position the Child Cube so it is clearly visible beside the Parent.

---

### Experiment A — Position

Before running the scene:

Predict:

> What happens if I move only the Parent?

Test your prediction.

Observe:

* Parent position
* Child position

---

### Experiment B — Rotation

Reset the scene.

Now rotate only the Parent.

Before testing:

Predict:

> What path will the Child follow?

Run the experiment.

Observe carefully.

---

### Experiment C — Scale

Reset again.

Scale only the Parent.

Predict:

* Does the Child become larger?
* Does the Child move farther away?

Run the experiment.

Observe the result.

---

# Investigation

Create this hierarchy:

```text id="rjlwm1"
Sun
└── Earth
    └── Moon
```

Rotate only the Sun.

Observe.

Rotate only the Earth.

Observe.

Ask yourself:

Why does the Moon behave differently in each case?

---

# Design Principle

## Relationships are often more important than objects.

Many beginning developers focus on individual objects.

Experienced developers often think about relationships.

Examples:

A wheel belongs to a vehicle.

A moon belongs to a planet.

A sword belongs to a player.

Those relationships determine how objects move through the world.

---

# Practical Applications

Transform inheritance appears throughout game development.

Examples include:

### Solar Systems

Planets inherit movement from stars.

Moons inherit movement from planets.

---

### Vehicles

Wheels inherit movement from the chassis.

---

### Cameras

A camera inherits movement from the player.

---

### Weapons

A sword inherits movement from a character.

---

### User Interface

Buttons inherit movement from menus.

---

# Common Misconceptions

### "Only movement is inherited."

Not true.

Rotation and scale are also inherited.

---

### "Children become independent after they are created."

No.

They remain connected until the hierarchy changes.

---

### "The child's transform disappears."

The child still has its own transform.

It simply exists relative to the parent.

---

### "Inheritance is a programming feature."

No.

Transform inheritance exists even before a single line of code is written.

It is part of the scene hierarchy itself.

---

# Challenge

Predict the outcome before testing.

Create:

```text id="jlwm56"
Parent

└── Child
```

Position the Child:

```text
3 meters to the right
```

Now:

Rotate the Parent **90°**.

Question:

Without running the scene...

Where will the Child end up?

Draw your prediction.

Then test it.

---

# Reflection

Consider the following questions:

* Which transform surprised you the most?
* Why is inheritance useful?
* Can you think of a real-world object that depends on transform inheritance?

Complete the sentence:

> Parent Transform Inheritance allows me to...

---

# Self Check

Before moving on, ask yourself:

✓ Can I predict what happens when a parent moves?

✓ Can I predict what happens when a parent rotates?

✓ Can I predict what happens when a parent scales?

✓ Can I explain why hierarchies make complex systems easier to build?

---

# Looking Ahead

Transform inheritance explains many of the systems you will build throughout this course.

In the next techniques, you'll begin exploring something even more powerful:

Objects do not simply have positions.

They also have their own sense of:

* forward
* right
* up

Those directions are encoded within the object's **Transform Basis**, allowing every object to carry its own coordinate system through the world.
