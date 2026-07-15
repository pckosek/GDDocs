# Technique 2.5 — Create a CharacterBody3D

## Classification

**Type:** Engineering Technique

**Category:** Physical Interaction

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Scenario

You are building a **player character**.

The player should:

- move exactly when the player provides input
- stop immediately when input stops
- collide with walls
- remain standing on the floor
- be completely under your control

Consulting the **Physical Representation Guide**, we choose:

```text
CharacterBody3D
```

because **our gameplay code** owns the movement while the physics engine assists with collision resolution.

---

# Why This Technique Matters

CharacterBody3D is one of the most important nodes in Godot.

Unlike a RigidBody3D, the physics engine does **not** decide where the character wants to move.

Instead:

- your script decides the desired movement
- Godot resolves collisions
- the engine prevents the player from passing through the environment

Think of CharacterBody3D as a partnership.

Your script controls the intention.

Godot handles the physical constraints.

---

# Starter Implementation

Create the following hierarchy.

```text
Player (CharacterBody3D)
├── CollisionShape3D
├── MeshInstance3D
└── Camera3D
```

Assign:

**MeshInstance3D**

- CapsuleMesh

**CollisionShape3D**

- CapsuleShape3D

Attach the following script.

```gdscript
extends CharacterBody3D

@export var speed := 5.0

func _physics_process(delta):

	var direction := Vector3.ZERO

	if Input.is_action_pressed("move_left"):
		direction.x -= 1

	if Input.is_action_pressed("move_right"):
		direction.x += 1

	if Input.is_action_pressed("move_forward"):
		direction.z -= 1

	if Input.is_action_pressed("move_backward"):
		direction.z += 1

	velocity.x = direction.x * speed
	velocity.z = direction.z * speed

	move_and_slide()
```

Run the scene.

The capsule should move around the environment while colliding with walls.

Notice:

We never directly modify:

```gdscript
position
```

Instead we control:

```gdscript
velocity
```

---

# Anatomy

This object is built from several cooperating parts.

## CharacterBody3D

Responsible for:

> **Managing scripted movement while respecting collisions.**

It provides built-in functionality for:

- velocity
- collision response
- floor detection
- sliding

---

## CollisionShape3D

Responsible for:

> **The player's physical volume.**

Without it, the player has no physical presence.

---

## MeshInstance3D

Responsible for:

> **The player's visible appearance.**

---

## Camera3D

Responsible for:

> **The player's view of the world.**

Although not required, cameras are commonly attached directly to CharacterBody3Ds.

---

# Dissecting the Code

Unlike the previous movement systems, we no longer write:

```gdscript
position += ...
```

Instead we describe the player's desired movement by updating:

```gdscript
velocity
```

Finally we ask Godot:

```gdscript
move_and_slide()
```

Godot performs:

- movement
- collision resolution
- sliding along walls

This is the first time we allow the engine to participate in the movement itself.

---

# Design Principle

## Describe intent.

Allow the engine to resolve collisions.

The player's intention is:

> Move forward.

The engine's responsibility is:

> Determine how that movement interacts with the world.

This separation produces movement that feels much more natural than manually changing position.

---

# Experiment

Only modify one thing at a time.

---

### Experiment A

Increase:

```gdscript
speed
```

Observe.

---

### Experiment B

Reduce:

```gdscript
speed
```

Observe.

---

### Experiment C

Comment out:

```gdscript
move_and_slide()
```

Run the scene.

What happens?

---

### Experiment D

Replace:

```gdscript
velocity.x
```

with:

```gdscript
position.x
```

Observe.

How does the behavior differ?

---

### Experiment E

Remove one wall from the environment.

Observe.

How does movement change?

---

# Practical Observation

CharacterBody3Ds are designed for objects that require:

- precision
- responsiveness
- predictable control

Unlike RigidBody3Ds, players generally expect their characters to move exactly when they provide input.

Predictability is often more important than realism.

---

# Common Uses

CharacterBody3Ds commonly represent:

- players
- enemies
- NPCs
- controllable vehicles
- AI agents

Whenever gameplay logic should control movement while respecting collisions, CharacterBody3D is often the correct choice.

---

# Common Misconceptions

### "CharacterBody3D is just a better RigidBody3D."

No.

The two solve different problems.

RigidBody3D simulates physics.

CharacterBody3D simulates player intent.

---

### "I should move the player by changing position."

Usually not.

CharacterBody3D is designed around:

```gdscript
velocity
```

and

```gdscript
move_and_slide()
```

---

### "move_and_slide() moves the player wherever I want."

Not exactly.

It attempts to move according to your velocity while respecting collisions.

---

### "The physics engine controls my character."

Not entirely.

Your script decides the desired movement.

Godot resolves the physical interactions.

---

# Reflection

Complete the sentence.

> CharacterBody3D differs from RigidBody3D because...

Now answer:

Why is player movement usually scripted rather than fully simulated?

Can you think of situations where using a RigidBody3D for the player would actually be desirable?

---

# Self Check

Before moving on, ask yourself:

✓ I can build a CharacterBody3D.

✓ I understand why it requires a CollisionShape3D.

✓ I understand the purpose of the velocity variable.

✓ I understand why move_and_slide() is necessary.

✓ I can explain the difference between scripted movement and simulated movement.

---

# Looking Ahead

Our CharacterBody3D can now move through the world.

But movement alone is not enough.

Players need to know:

- when they reached a checkpoint
- when they collected an item
- when they crossed a finish line
- when they entered a dangerous area

The next technique introduces **Area3D**, which allows objects to detect interaction without physically blocking movement.