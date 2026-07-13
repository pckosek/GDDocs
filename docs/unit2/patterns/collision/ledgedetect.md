# Pattern 2.10.8 — Detect a Ledge

## Classification

**Type:** Gameplay Pattern

**Category:** CharacterBody3D

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- move_and_slide()
- RayCast3D
- Floor Detection

---

# Problem

Sometimes your game needs to know:

> **Am I standing at the edge of a platform?**

Examples include:

- preventing NPCs from walking off cliffs
- allowing ledge grabbing
- warning the player
- changing animations
- AI patrol systems

Unlike floor detection, Godot does not provide a built-in:

```gdscript
is_on_ledge()
```

Instead, we build one ourselves.

---

# Starter Implementation

Attach a **RayCast3D** as a child of the CharacterBody3D.

Position it slightly in front of the player's feet.

Example:

```text
Player
├── CollisionShape3D
├── MeshInstance3D
└── RayCast3D
```

Point the RayCast downward.

Attach the following script.

```gdscript
extends CharacterBody3D

@onready var ledge_check := $RayCast3D

func _physics_process(delta):

	move_and_slide()

	if not ledge_check.is_colliding():

		print("Ledge Detected!")
```

Run the scene.

Walk toward the edge of a platform.

Observe.

The message appears when the ray no longer detects the floor.

---

# How It Works

The player may still be standing safely.

But the ray is looking slightly ahead.

When the ground disappears...

```gdscript
is_colliding()
```

becomes:

```gdscript
false
```

This allows us to detect the ledge *before* the player falls.

---

# Anatomy

## CharacterBody3D

Moves through the world.

---

## RayCast3D

Looks ahead.

Asks:

> Is there still ground here?

---

## Floor

Provides a collision target.

No collision means:

Potential ledge.

---

# Design Principle

## Sometimes you need to ask about the future.

Most collision systems answer:

> What just happened?

Raycasts often answer:

> What is about to happen?

This allows AI and gameplay systems to anticipate rather than simply react.

---

# Experiment

Only change one thing.

---

### Experiment A

Move the RayCast farther in front of the player.

Observe.

When is the ledge detected?

---

### Experiment B

Move the RayCast closer to the player.

Observe.

How late does the warning occur?

---

### Experiment C

Make the RayCast longer.

Observe.

Does it still detect the floor?

---

### Experiment D

Turn on:

```text
Visible Collision Shapes
```

Watch the ray while moving around.

Observe exactly what it is intersecting.

---

### Experiment E

Replace:

```gdscript
print("Ledge Detected!")
```

with:

```gdscript
velocity = Vector3.ZERO
```

The NPC now stops before walking off the edge.

---

# Practical Applications

Ledge detection appears throughout games.

Examples include:

- coyote time
- enemy patrols
- cliff avoidance
- parkour
- ledge grabbing
- climbing
- AI navigation
- platforming

Many intelligent movement systems begin with a simple raycast.

---

# Common Misconceptions

### "The player already knows where the ledge is."

Not necessarily.

The CharacterBody only knows about collisions that already happened.

The RayCast predicts what lies ahead.

---

### "RayCast3D replaces collisions."

No.

Raycasts complement collision detection.

They answer different questions.

---

### "The ray should start at the player's center."

Usually not.

For ledge detection, placing the ray near the feet often produces better results.

---

### "This only works for players."

Enemy AI frequently uses this exact pattern.

---

# Workbench Habit

Whenever gameplay requires anticipating the environment rather than reacting to it, consider using a RayCast3D.

It allows your code to ask:

> **What is ahead of me?**

instead of waiting until the interaction has already occurred.

---

# Challenge

Build a simple platform.

Place an NPC on it.

When the NPC reaches the edge:

- stop moving
- print "Turn Around"
- (optional) reverse direction

Notice that one RayCast can make an otherwise unintelligent NPC appear much more aware of its surroundings.