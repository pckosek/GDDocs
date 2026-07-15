# Pattern 2.10.2 — Identify What I Collided With

## Classification

**Type:** Gameplay Pattern

**Category:** Collision Detection

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- move_and_slide()

---

# Problem

Many gameplay systems need to know **what** the player collided with.

Examples include:

- walls
- enemies
- moving platforms
- crates
- hazards

Different objects often require different responses.

This pattern identifies the object involved in a collision and allows your code to respond appropriately.

---

# Starter Implementation

```gdscript
extends CharacterBody3D

func _physics_process(delta):

	# Movement code goes here...

	move_and_slide()

	for i in get_slide_collision_count():

		var collision = get_slide_collision(i)
		var collider = collision.get_collider()

		print(collider)
```

Run the scene.

Walk into different objects.

Observe the Output panel.

Notice that different collisions report different objects.

---

# Dissecting the Code

After:

```gdscript
move_and_slide()
```

Godot stores information about every collision that occurred during this frame.

Each collision contains a reference to the object that was hit.

```gdscript
var collider = collision.get_collider()
```

This object can then be inspected just like any other node.

---

# Pattern Variations

Sometimes we only care about the object's name.

```gdscript
print(collider.name)
```

---

Sometimes we care about its type.

```gdscript
if collider is StaticBody3D:
	print("Wall")
```

---

```gdscript
if collider is RigidBody3D:
	print("Physics Object")
```

---

```gdscript
if collider is CharacterBody3D:
	print("Another Character")
```

---

```gdscript
if collider is AnimatableBody3D:
	print("Moving Platform")
```

---

Sometimes we care about a specific node.

```gdscript
if collider.name == "Goal":
	print("Scored!")
```

---

Or perhaps:

```gdscript
if collider.is_in_group("Enemies"):
```

which becomes even more useful as projects become larger.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Print:

```gdscript
collider.name
```

instead of:

```gdscript
collider
```

Observe.

---

### Experiment B

Create:

- one wall
- one moving platform
- one crate

Walk into each.

Can your script distinguish between them?

---

### Experiment C

Replace:

```gdscript
print(...)
```

with:

```gdscript
if collider is StaticBody3D:
	print("Hit Wall")
```

Observe.

---

### Experiment D

Instead of checking the type...

check:

```gdscript
collider.name
```

Compare the two approaches.

Which seems more flexible?

---

# Practical Applications

This pattern appears throughout game development.

Examples include:

- enemy damage
- wall impacts
- checkpoints
- moving platforms
- pushing crates
- environmental hazards
- footsteps
- sound effects

Many gameplay systems begin by asking:

> What did I collide with?

---

# Common Misconceptions

### "The collision tells me what to do."

No.

The collision simply provides information.

Your script decides how to respond.

---

### "Every collision is the same."

Different objects often require completely different gameplay.

Learning to identify them is one of the foundations of gameplay programming.

---

### "Checking the node name is always best."

Names work well for simple projects.

As projects become larger, checking:

- type
- groups
- metadata

often becomes more reliable.

---

# Workbench Habit

Treat collision detection as a two-step process.

Step 1

Determine **what** happened.

```gdscript
var collider = collision.get_collider()
```

Step 2

Decide **how** your game should respond.

Separating these two ideas usually leads to cleaner, easier-to-maintain code.

---

# Challenge

Build a simple room containing:

- a wall
- a moving platform
- a crate

Write one script that prints a different message for each object the player collides with.

For example:

```
Hit Wall

Riding Platform

Pushable Crate
```

Notice that the movement code never changes.

Only the collision response does.