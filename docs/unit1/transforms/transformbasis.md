# Technique 3.4 — Understanding Transform Basis

## Classification

**Type:** Transform Systems Technique

**Category:** Transform Systems

**Difficulty:** Advanced

**Estimated Time:** 30–45 minutes

---

# Design Problem

Imagine a spaceship.

When it first appears in the world, pressing **W** moves it north.

Now rotate the spaceship 90°.

Press **W** again.

Most beginning programmers expect the ship to continue moving north.

Instead...

...it moves in the direction it is facing.

Why?

The answer is found in the object's **Transform Basis**.

---

# Why This Technique Matters

Every object carries its own coordinate system.

It has its own sense of:

* forward
* right
* up

These directions rotate with the object.

This allows objects to move naturally regardless of how they are oriented.

Without Transform Basis, many common game systems become extremely difficult to build.

Examples include:

* flying vehicles
* first-person cameras
* third-person characters
* missiles
* enemy AI
* procedural movement

---

# Mental Model

Imagine standing in a room.

Ask yourself:

> Which way is forward?

Now turn around.

Ask again.

Did "forward" change?

Yes.

The room did not rotate.

**You** did.

Every Node3D behaves the same way.

Each object carries its own personal sense of direction.

Transform Basis stores those directions.

---

# Core Idea

A Transform contains two major pieces of information.

### Origin

Where the object exists.

---

### Basis

How the object is oriented.

The Basis defines three local directions:

```text id="gjlwm2"
Right

Up

Forward
```

As the object rotates...

...its Basis rotates with it.

---

# Experiment

Create a simple scene.

```text id="jlwm71"
World

└── Ship
```

Attach a script.

Every frame, print:

```gdscript
print(transform.basis)
```

Observe the values.

Now rotate the ship.

Observe again.

Questions:

* What changed?
* What stayed the same?

---

# Investigation

Now create three arrows.

Color them:

* Red
* Green
* Blue

Attach them to the Ship.

Rotate the Ship.

Observe:

The arrows rotate with it.

These arrows are visualizing the object's local coordinate system.

Now compare:

The world's axes.

The ship's axes.

Are they still pointing in the same directions?

---

# Experiment

Instead of moving like this:

```gdscript
position += Vector3.FORWARD
```

try moving like this:

```gdscript
position += transform.basis * Vector3.FORWARD
```

Predict what will happen before running the scene.

Then test it.

Rotate the ship.

Run again.

Observe.

---

# Design Principle

## Every object carries its own frame of reference.

Beginning programmers often think:

> There is one "forward."

Experienced developers think:

> Every object has its own forward.

That simple shift in perspective explains a surprising amount of Godot's behavior.

---

# Practical Applications

Transform Basis appears everywhere.

Examples include:

### Aircraft

Always fly forward.

---

### Cameras

Always look where they are facing.

---

### Enemies

Move toward their own forward direction.

---

### Vehicles

Turn first.

Then accelerate in the new direction.

---

### Projectiles

Travel along the direction they were fired.

---

# Common Misconceptions

### "Forward always means negative Z."

Only before the object rotates.

After rotation, the object's forward direction changes.

---

### "The world rotates."

Usually not.

The object's local coordinate system rotates.

---

### "Basis stores position."

No.

Position is stored separately.

Basis stores orientation.

---

### "Transform Basis is only for advanced programming."

Not really.

Many common movement systems rely on it, even if tutorials hide the details.

Understanding Basis makes those systems much easier to reason about.

---

# Challenge

Before running the scene...

Predict.

Suppose a spaceship rotates:

```text
90°
```

to the right.

Questions:

Which direction is now:

* forward?
* right?
* up?

Sketch your prediction.

Now test it.

Was your mental model correct?

---

# Reflection

Complete the following sentence.

> Transform Basis allows an object to...

Now answer:

Why is this better than storing one universal "forward" direction for every object?

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain why an object's forward direction changes?

✓ Can I distinguish between world coordinates and local directions?

✓ Can I predict how Transform Basis changes after a rotation?

✓ Can I explain why flying games depend on Transform Basis?

---

# Looking Ahead

Transform Basis is one of the deepest ideas in Godot.

Many advanced systems—including:

* steering behaviors
* procedural animation
* AI navigation
* camera rigs
* physics
* procedural generation

all become easier to understand once you realize that every object carries its own coordinate system through the world.

Transform Basis is simply the mathematical description of that idea.
