# Technique 2.3 — Create an AnimatableBody3D

## Classification

**Type:** Engineering Technique

**Category:** Physical Interaction

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Scenario

You are building an **elevator**.

The elevator should:

- move because **your script** tells it to
- carry the player
- interact correctly with the physics engine
- never be pushed by another object

Consulting the **Physical Representation Guide**, we choose:

```text
AnimatableBody3D
```

because the movement is **scripted**, not simulated.

---

# Why This Technique Matters

Many game objects move.

But not all moving objects should be controlled by physics.

Consider:

- elevators
- moving platforms
- sliding doors
- rotating hazards
- crushing walls

These objects move according to gameplay rules rather than physical forces.

AnimatableBody3D is designed specifically for this kind of object.

---

# Starter Implementation

Create the following hierarchy.

```text
Elevator (AnimatableBody3D)
├── CollisionShape3D
└── MeshInstance3D
```

Assign:

**MeshInstance3D**

- BoxMesh

**CollisionShape3D**

- BoxShape3D

Attach the following script.

```gdscript
extends AnimatableBody3D

@export var speed := 2.0
@export var height := 3.0

var start_position : Vector3

func _ready():
	start_position = position

func _process(delta):

	position.y = start_position.y + sin(Time.get_ticks_msec() / 1000.0 * speed) * height
```

Run the scene.

The platform should move smoothly up and down.

---

# Anatomy

This object is built from three cooperating parts.

## AnimatableBody3D

Responsible for:

> **Participating in physics while being moved by your code.**

Unlike a RigidBody3D, physics does not decide where the object goes.

Your script does.

---

## CollisionShape3D

Responsible for:

> **The physical volume of the elevator.**

Without it, the player would fall through the platform.

---

## MeshInstance3D

Responsible for:

> **What the player sees.**

The mesh gives the platform its appearance.

The collision shape gives it physical presence.

---

# Design Principle

## Some objects follow rules instead of physics.

A rolling barrel should respond to forces.

An elevator should not.

The elevator follows gameplay rules.

It moves because the designer decided it should move.

Not because gravity or momentum made it move.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Increase:

```gdscript
height
```

Observe.

How does the ride change?

---

### Experiment B

Increase:

```gdscript
speed
```

Observe.

When does the motion begin to feel unrealistic?

---

### Experiment C

Replace:

```gdscript
position.y
```

with:

```gdscript
position.x
```

Observe.

The elevator now becomes a moving platform.

---

### Experiment D

Replace the oscillating motion with:

```gdscript
rotation.y += delta
```

Observe.

What kinds of game objects could use this behavior?

---

### Experiment E

Stand on the platform while it moves.

Observe.

Does the player move with the platform?

Why?

---

# Practical Observation

AnimatableBody3Ds often represent objects whose movement is part of the level design.

Examples include:

- elevators
- conveyor belts
- moving bridges
- rotating hazards
- sliding walls
- animated architecture

These systems are usually predictable.

Players learn their behavior through observation.

---

# Common Uses

AnimatableBody3Ds commonly represent:

- elevators
- moving platforms
- doors
- bridges
- rotating obstacles
- environmental hazards

Whenever **your script** determines the motion while the object still participates in collisions, AnimatableBody3D is often the correct choice.

---

# Common Misconceptions

### "This should be a RigidBody3D."

Not usually.

RigidBody3Ds move because of physics.

AnimatableBody3Ds move because your script tells them to.

---

### "This is just a moving StaticBody."

Not quite.

AnimatableBody3D exists specifically to support scripted movement while interacting correctly with other physical bodies.

---

### "I should move the MeshInstance."

Move the AnimatableBody3D itself.

Its children—including the mesh and collider—will move automatically.

---

### "Everything that moves should be Animatable."

Objects that should respond naturally to collisions, forces, or gravity are often better represented by RigidBody3D.

---

# Reflection

Complete the following sentence.

> AnimatableBody3D is useful because...

Now answer:

Why is an elevator a better candidate for AnimatableBody3D than RigidBody3D?

Can you think of three other objects that should probably be AnimatableBody3Ds?

---

# Self Check

Before moving on, ask yourself:

✓ I can build an AnimatableBody3D.

✓ I understand why it requires a CollisionShape3D.

✓ I can move it through scripting.

✓ I can explain why scripted motion is different from physics-driven motion.

---

# Looking Ahead

AnimatableBody3Ds move because **you** decide where they should go.

The next technique explores the opposite idea.

What if the object should move because of:

- gravity
- momentum
- collisions
- physical forces

For those systems, we'll explore **RigidBody3D**, where the physics engine becomes responsible for the motion.