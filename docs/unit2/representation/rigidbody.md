# Technique 2.4 — Create a RigidBody3D

## Classification

**Type:** Engineering Technique

**Category:** Physical Interaction

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Scenario

You are building a **rolling ball**.

The ball should:

- fall because of gravity
- bounce off the floor
- roll down ramps
- collide naturally with other objects
- respond to physical forces

Consulting the **Physical Representation Guide**, we choose:

```text
RigidBody3D
```

because we want **the physics engine** to determine the object's movement.

---

# Why This Technique Matters

Until now, every moving object has moved because **our code** decided where it should go.

RigidBody3Ds work differently.

Instead of prescribing motion directly, we describe the physical properties of the object and allow the engine to simulate the results.

This is one of the biggest conceptual shifts in Unit 2.

Instead of asking:

> "Where should the ball move?"

we begin asking:

> "What forces are acting on the ball?"

---

# Starter Implementation

Create the following hierarchy.

```text
Ball (RigidBody3D)
├── CollisionShape3D
└── MeshInstance3D
```

Assign:

**MeshInstance3D**

- SphereMesh

**CollisionShape3D**

- SphereShape3D

Place the ball several meters above a floor built with a **StaticBody3D**.

Run the scene.

Observe.

The ball should:

- fall
- collide with the floor
- bounce slightly
- eventually come to rest

Notice that no movement script was required.

---

# Anatomy

This object is built from three cooperating parts.

## RigidBody3D

Responsible for:

> **Allowing the physics engine to simulate motion.**

Unlike an AnimatableBody3D, you generally do **not** tell a RigidBody3D where to go every frame.

Instead, physics determines its movement.

---

## CollisionShape3D

Responsible for:

> **The physical volume of the ball.**

Without it, the physics engine has nothing to simulate.

---

## MeshInstance3D

Responsible for:

> **The visible appearance of the ball.**

The player sees the mesh.

The engine simulates the collider.

---

# Design Principle

## Describe the object, not the movement.

With scripted objects, you usually write:

> Move here.

With RigidBody3Ds, you instead describe:

- mass
- gravity
- friction
- bounce

The engine determines what happens next.

This shift—from prescribing movement to describing physical behavior—is one of the defining ideas behind physics simulation.

---

# Experiment

Modify only one thing at a time.

---

### Experiment A

Increase the ball's:

```text
Mass
```

Observe.

Does it fall faster?

Does it bounce differently?

---

### Experiment B

Increase:

```text
Bounce
```

Observe.

How does the collision change?

---

### Experiment C

Increase:

```text
Friction
```

Observe.

How does the ball roll after landing?

---

### Experiment D

Place the ball on a ramp.

Observe.

The script never tells the ball to roll.

Why does it move?

---

### Experiment E

Duplicate the ball.

Give each copy different:

- mass
- bounce
- friction

Drop them simultaneously.

Compare their behavior.

---

# Starter Code — Applying an Impulse

Sometimes we want to give a RigidBody3D an initial push.

Attach the following script.

```gdscript
extends RigidBody3D

@export var launch_force := Vector3(0, 5, -10)

func _ready():
	apply_central_impulse(launch_force)
```

Run the scene.

The ball immediately launches into the air.

Notice that after the impulse is applied, the physics engine completely takes over.

---

# Practical Observation

RigidBody3Ds often represent objects whose exact motion is **not predetermined**.

Examples include:

- barrels
- rocks
- crates
- soccer balls
- debris
- bowling pins

Each playthrough may produce slightly different results.

That unpredictability often makes games feel more natural.

---

# Common Uses

RigidBody3Ds commonly represent:

- rolling objects
- falling objects
- throwable objects
- breakable props
- environmental debris
- physics puzzles

Whenever physics should determine an object's motion, a RigidBody3D is often the appropriate choice.

---

# Common Misconceptions

### "I should move a RigidBody3D by changing its position every frame."

Usually not.

Doing so bypasses the physics simulation.

Whenever possible, allow physics to determine the movement.

---

### "Gravity is part of my script."

No.

Gravity is part of the physics simulation.

The RigidBody3D automatically participates.

---

### "Mass changes how fast objects fall."

Not by itself.

In a vacuum, heavy and light objects accelerate equally under gravity.

Mass primarily affects how objects respond during collisions and impulses.

---

### "RigidBody3Ds are always the correct choice."

Only when you want physics to own the motion.

Many gameplay objects are better represented by CharacterBody3Ds or AnimatableBody3Ds.

---

# Reflection

Complete the sentence.

> A RigidBody3D differs from an AnimatableBody3D because...

Now answer:

When would you intentionally choose a RigidBody3D instead of scripting the movement yourself?

Can you think of three gameplay objects that should probably be RigidBody3Ds?

---

# Self Check

Before moving on, ask yourself:

✓ I can build a RigidBody3D.

✓ I understand the purpose of its CollisionShape3D.

✓ I can explain why gravity affects it automatically.

✓ I understand the difference between scripting motion and simulating motion.

✓ I can apply an impulse to start the object's motion.

---

# Looking Ahead

RigidBody3Ds allow the **physics engine** to decide how objects move.

Players, however, usually require something different.

Players need:

- precise control
- responsive movement
- predictable behavior
- reliable collisions

In the next technique, we'll explore **CharacterBody3D**, where movement returns to your script while still interacting with the physical world.