# Pattern 2.10.4 — Push a RigidBody

## Classification

**Type:** Gameplay Pattern

**Category:** Collision Detection

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- RigidBody3D
- move_and_slide()
- Collision Detection

---

# Problem

Sometimes the player should affect the world.

Examples include:

- pushing a crate
- rolling a barrel
- moving a ball
- nudging debris

The player should remain under scripted control.

The object should remain under physics control.

How do these two systems cooperate?

---

# Starter Implementation

Create the following scene.

```text
World
├── Player (CharacterBody3D)
└── Crate (RigidBody3D)
```

Use the CharacterBody3D movement script from the previous techniques.

Attach the following code immediately after:

```gdscript
move_and_slide()
```

```gdscript
for i in get_slide_collision_count():

	var collision = get_slide_collision(i)
	var body = collision.get_collider()

	if body is RigidBody3D:

		var direction = -collision.get_normal()

		body.apply_central_impulse(direction * 2.0)
```

Run the scene.

Walk into the crate.

Observe.

The player continues moving normally.

The crate responds to the collision by moving away.

---

# How It Works

The CharacterBody does **not** move the crate directly.

Instead:

```text
CharacterBody3D

↓

Detect Collision

↓

Identify RigidBody3D

↓

Apply Impulse

↓

Physics Takes Over
```

Notice that after the impulse is applied...

your script stops controlling the crate.

The physics engine continues the simulation.

---

# Anatomy

## CharacterBody3D

Responsible for:

- movement
- collision detection

---

## Collision

Responsible for:

- identifying the object
- providing the collision normal

---

## RigidBody3D

Responsible for:

- responding to the impulse
- simulating the resulting motion

Each object remains responsible for its own behavior.

---

# Design Principle

## Interact.

Don't control.

The player does **not** tell the crate where to go.

Instead, the player provides a force.

The crate decides what happens next through physics.

This separation produces interactions that feel natural.

---

# Experiment

Only change one thing.

---

### Experiment A

Increase:

```gdscript
2.0
```

to:

```gdscript
10.0
```

Observe.

---

### Experiment B

Reduce the impulse dramatically.

Observe.

---

### Experiment C

Replace:

```gdscript
apply_central_impulse()
```

with:

```gdscript
apply_impulse()
```

Read the documentation.

What additional capability does this provide?

---

### Experiment D

Push:

- a small crate
- a large crate

Observe.

Does mass affect the interaction?

---

### Experiment E

Create three crates.

Push them into one another.

Observe.

The player only interacts with the first crate.

Physics handles the rest.

---

# Practical Applications

This pattern appears throughout games.

Examples include:

- pushing boxes
- soccer balls
- physics puzzles
- explosive barrels
- bowling
- debris
- destructible environments

Many interactive worlds rely on players influencing physics rather than directly controlling it.

---

# Common Misconceptions

### "The CharacterBody moves the crate."

Not exactly.

It applies an impulse.

Physics performs the movement.

---

### "I should change the crate's position."

Usually not.

Doing so bypasses the physics simulation.

---

### "Every collision should push objects."

Often only specific gameplay objects should be pushable.

Walls generally should not move.

---

### "The player becomes a RigidBody."

The player remains a CharacterBody3D.

Only the crate participates in the physics simulation.

---

# Workbench Habit

Whenever a scripted object needs to influence a physics object:

Don't move it directly.

Instead ask:

> **Can I apply a force or impulse instead?**

Doing so usually produces more natural gameplay.

---

# Challenge

Build a simple room containing:

- one player
- three crates
- one wall

Experiment with different:

- masses
- impulse strengths
- friction values

Observe.

Can you create interactions that feel:

- heavy?
- slippery?
- playful?
- difficult?

Remember:

The same code can produce very different gameplay simply by changing the physical properties of the objects involved.