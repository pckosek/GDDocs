# Pattern 2.10.1 — Detect Every Collision This Frame

## Classification

**Type:** Gameplay Pattern

**Category:** Collision Detection

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- move_and_slide()
- StaticBody3D

---

# Problem

Your CharacterBody3D is moving correctly.

Now you want to know:

> **What did I collide with this frame?**

Examples include:

- walls
- enemies
- projectiles
- moving platforms
- pushable objects

CharacterBody3D stores this information after every call to:

```gdscript
move_and_slide()
```

---

# Starter Implementation

```gdscript
extends CharacterBody3D

func _physics_process(delta):

	# Movement code goes here...

	move_and_slide()

	for i in get_slide_collision_count():

		var collision = get_slide_collision(i)

		print(collision.get_collider())
```

Run the scene.

Walk into walls.

Walk into several objects.

Observe the Output panel.

---

# How It Works

Every frame:

```text
Move

↓

Slide

↓

Store Collision Information

↓

Iterate Through Collisions
```

The CharacterBody remembers every collision that occurred during the movement.

You can inspect each one individually.

---

# Anatomy

## get_slide_collision_count()

Returns:

> **How many collisions occurred during this frame.**

---

## get_slide_collision(i)

Returns information about one collision.

Examples include:

- collider
- collision point
- collision normal
- collider velocity

---

## collision.get_collider()

Returns the object that was hit.

Examples:

```text
Wall

Enemy

Crate

MovingPlatform
```

---

# Experiment

Only change one thing.

---

### Experiment A

Print:

```gdscript
collision.get_collider().name
```

instead.

Observe.

---

### Experiment B

Create a narrow hallway.

Walk through it.

How many collisions occur?

---

### Experiment C

Walk into a corner.

Observe.

Can multiple collisions happen during the same frame?

---

### Experiment D

Walk into a moving platform.

Observe.

Is the collider different?

---

# Common Uses

This pattern is frequently used for:

- enemy detection
- footstep systems
- collision sounds
- wall effects
- pushing objects
- climbing systems
- parkour
- AI navigation

---

# Common Mistakes

### Forgetting move_and_slide()

Collision information is only generated after movement.

---

### Only checking the first collision

A CharacterBody can collide with multiple objects during one frame.

Always consider whether multiple collisions are possible.

---

### Assuming every collider is the same type

The returned object might be:

- StaticBody3D
- RigidBody3D
- CharacterBody3D
- AnimatableBody3D
- Area3D (depending on the interaction)

Always inspect the object before making assumptions.

---

# Pattern Variations

Instead of:

```gdscript
print(collision.get_collider())
```

You might:

Damage an enemy.

---

Play a sound.

---

Bounce.

---

Reverse direction.

---

Push a crate.

---

Spawn particles.

The collision detection remains identical.

Only the response changes.

---

# Workbench Habit

Whenever you need to ask:

> **"What did I hit?"**

start with this pattern.

It is one of the most common building blocks in gameplay programming.