# Technique 2.6 — Create an Area3D

## Classification

**Type:** Engineering Technique

**Category:** Physical Interaction

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Scenario

You are building a **checkpoint**.

The checkpoint should:

- detect when the player enters it
- notify the game that the player arrived
- allow the player to pass through it
- never physically block movement

Consulting the **Physical Representation Guide**, we choose:

```text
Area3D
```

because the object should **observe interaction** rather than physically participate in it.

---

# Why This Technique Matters

Until now, every physical object has existed to **block** or **respond** to movement.

Area3D introduces a completely different idea.

Instead of asking:

> "Should I collide?"

it asks:

> **"Did something enter me?"**

Area3D represents one of the most common gameplay building blocks.

It allows the world to detect events without interfering with movement.

---

# Starter Implementation

Create the following hierarchy.

```text
Checkpoint (Area3D)
├── CollisionShape3D
└── MeshInstance3D
```

Assign:

**MeshInstance3D**

- CylinderMesh
- (or another visible marker)

**CollisionShape3D**

- CylinderShape3D

Connect the:

```text
body_entered()
```

signal.

Attach the following script.

```gdscript
extends Area3D

func _on_body_entered(body):

	print(body.name)
	print("Checkpoint Reached!")
```

Run the scene.

Walk the player through the checkpoint.

Observe.

The player passes through the object.

The signal fires.

---

# Anatomy

This object is built from three cooperating parts.

## Area3D

Responsible for:

> **Observing overlap events.**

Unlike a StaticBody3D, it does not physically stop movement.

Instead, it watches for objects entering or leaving its volume.

---

## CollisionShape3D

Responsible for:

> **Defining the detection volume.**

Without a CollisionShape3D, the Area has nothing to monitor.

---

## MeshInstance3D

Responsible for:

> **Showing the player where the checkpoint exists.**

Many Area3Ds are actually invisible during gameplay.

The mesh simply helps visualize the object during development.

---

# Dissecting the Code

Unlike CharacterBody3D, we never ask:

```gdscript
move_and_slide()
```

Unlike RigidBody3D, we never apply forces.

Instead, the Area simply waits.

When another object enters its collision volume:

```gdscript
body_entered(body)
```

is emitted.

Notice that we never continuously ask:

> "Is the player here?"

Godot tells us when that becomes true.

---

# Design Principle

## Observe.

Don't obstruct.

Area3Ds exist to answer questions such as:

- Has the player arrived?
- Has an enemy entered?
- Did the projectile reach the goal?
- Did something leave the safe zone?

They measure interaction.

They do not prevent it.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Resize the CollisionShape3D.

Observe.

How does changing the invisible volume affect gameplay?

---

### Experiment B

Remove the MeshInstance3D.

Run the scene.

Can the checkpoint still detect the player?

---

### Experiment C

Remove the CollisionShape3D.

Run the scene.

Does the signal still fire?

Why?

---

### Experiment D

Print:

```gdscript
body.name
```

instead of:

```gdscript
"Checkpoint Reached!"
```

Observe.

What kinds of objects are entering the Area?

---

### Experiment E

Duplicate the checkpoint.

Create two separate trigger volumes.

Observe.

Can both Areas monitor the player independently?

---

# Practical Observation

Area3Ds appear throughout games.

Examples include:

- checkpoints
- finish lines
- pickup items
- damage zones
- interaction prompts
- save points
- enemy detection
- sound triggers

Many gameplay systems are simply Areas responding to events.

---

# Common Uses

Area3Ds commonly represent:

- collectible coins
- finish lines
- checkpoints
- trigger zones
- interactable objects
- hazard volumes
- detection regions

Whenever an object should **notice** interaction rather than physically stop movement, Area3D is often the correct choice.

---

# Common Misconceptions

### "Area3D is another collider."

Not exactly.

It has a CollisionShape3D.

But its purpose is detection rather than collision response.

---

### "Players should collide with checkpoints."

Usually not.

Players generally move through checkpoints while the game records their progress.

---

### "Area3D replaces Signals."

No.

Area3D frequently **uses** signals.

The Area detects.

The signal communicates.

---

### "Area3D is invisible."

Only if you want it to be.

Many Areas include visible meshes to communicate important gameplay information.

---

# Reflection

Complete the sentence.

> Area3D is different because...

Now answer:

Why might a checkpoint be better represented by an Area3D than a StaticBody3D?

Can you think of three other gameplay systems that could be implemented using Area3D?

---

# Self Check

Before moving on, ask yourself:

✓ I can build an Area3D.

✓ I understand why it requires a CollisionShape3D.

✓ I understand the purpose of `body_entered()`.

✓ I understand the difference between detecting interaction and blocking movement.

✓ I can explain why Area3D frequently works together with Signals.

---

# Looking Ahead

You now understand the five most common physical representations in Godot.

- StaticBody3D
- AnimatableBody3D
- RigidBody3D
- CharacterBody3D
- Area3D

The remainder of this unit focuses on what happens **when these objects begin interacting**.

A rolling ball hits the floor.

A player walks into a wall.

An elevator carries a character.

A player crosses a finish line.

Those interactions form the basis of gameplay.