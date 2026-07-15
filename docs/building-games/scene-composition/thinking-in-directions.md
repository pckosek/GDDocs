# Technique 3.5 — Thinking in Directions

## Classification

**Type:** Transform Systems Technique

**Category:** Transform Systems

**Difficulty:** Advanced

**Estimated Time:** 30–45 minutes

---

# Design Problem

Many beginning programmers think about movement using coordinates.

For example:

> Move 5 units in X.

or

> Increase Z by 10.

While this works, it quickly becomes difficult as objects begin rotating.

A better question is:

> Which way is the object trying to move?

Game development is often easier when we think in **directions** instead of **numbers**.

---

# Why This Technique Matters

Most moving objects do not care where the world axes are.

A spaceship wants to fly **forward**.

A car wants to drive **forward**.

A camera wants to move **forward**.

A character wants to walk **forward**.

Notice that none of these examples mention:

* X
* Y
* Z

Instead, they describe intention.

Thinking in directions allows your code to describe behavior rather than coordinates.

---

# Mental Model

Imagine driving a car.

Suppose someone tells you:

> Drive 10 meters east.

You probably wouldn't think in those terms.

Instead you would think:

> Drive forward.

Now imagine turning the steering wheel.

Your idea of "forward" changes.

The world hasn't changed.

Your direction has.

Objects in Godot behave exactly the same way.

---

# Core Idea

Objects do not move toward coordinates.

Objects move in directions.

Examples include:

```text id="zjjlwm"
Forward

Backward

Left

Right

Up

Down
```

These directions belong to the object itself.

They rotate whenever the object rotates.

---

# Experiment

Create a simple spaceship.

Write two movement systems.

---

### Version A

Move using:

```gdscript id="cgjlwm"
Vector3.FORWARD
```

---

### Version B

Move using:

```gdscript id="jlwmy4"
transform.basis * Vector3.FORWARD
```

Rotate the ship.

Test both versions.

Observe the difference.

---

# Investigation

Build a simple aircraft.

Turn the aircraft 90°.

Before pressing **W**, predict:

Where should the aircraft move?

Now test it.

Ask yourself:

Which movement system feels more natural?

Why?

---

# Design Principle

## Describe intentions, not coordinates.

Compare these two ideas.

```gdscript
position.z -= speed
```

versus

```gdscript
move_forward()
```

The second describes what the object is trying to accomplish.

Good game code often reads more like behavior than mathematics.

---

# Practical Applications

Thinking in directions appears throughout game development.

Examples include:

### Player Controllers

Walk forward.

---

### Flying Games

Accelerate in the current heading.

---

### Enemy AI

Move toward the player.

---

### Projectiles

Travel in the direction they were fired.

---

### Cameras

Move relative to where they are looking.

---

Every one of these systems becomes simpler when movement is described using directions.

---

# Common Misconceptions

### "Forward is always negative Z."

Only before the object rotates.

---

### "Coordinates and directions are the same."

Coordinates describe locations.

Directions describe motion.

---

### "Rotation changes the world."

No.

Rotation changes the object's relationship to the world.

---

### "Thinking in directions is only useful for vehicles."

Nearly every moving object benefits from directional thinking.

---

# Challenge

Create two cubes.

Cube A always moves:

```text id="jlwmr8"
World Forward
```

Cube B always moves:

```text id="jlwmh7"
Its Own Forward
```

Rotate both cubes.

Predict what will happen.

Now run the scene.

Which cube behaves the way you expected?

Which would you use for:

* a spaceship?
* a security camera?
* a moving platform?

Explain your reasoning.

---

# Reflection

Complete the sentence:

> Thinking in directions allows me to...

Now answer:

When would moving toward a world coordinate be preferable to moving in a local direction?

---

# Self Check

Before moving on, ask yourself:

✓ Can I distinguish between a coordinate and a direction?

✓ Can I explain why "forward" changes after rotation?

✓ Can I predict how an object will move after turning?

✓ Can I describe movement without referring to X, Y, or Z?

---

# Looking Ahead

Many advanced systems are built entirely around directional thinking.

Examples include:

* steering behaviors
* path following
* missile guidance
* flocking systems
* procedural animation
* camera rigs

The underlying mathematics becomes increasingly sophisticated.

The mental model remains surprisingly simple:

> Every object carries its own sense of direction.

Learning to think that way is one of the most important transitions from writing code that merely works to writing systems that behave naturally.
