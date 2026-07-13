# Pattern 2.10.6 — Detect the Floor

## Classification

**Type:** Gameplay Pattern

**Category:** CharacterBody3D

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- move_and_slide()

---

# Problem

Many gameplay systems need to know one simple thing:

> **Is the player standing on the ground?**

Examples include:

- jumping
- footsteps
- landing effects
- resetting jumps
- playing animations
- detecting when the player falls

Although you *could* inspect every collision manually, CharacterBody3D already provides a much simpler solution.

---

# Starter Implementation

Attach the following script to a **CharacterBody3D**.

```gdscript
extends CharacterBody3D

func _physics_process(delta):

	# Movement code goes here...

	move_and_slide()

	if is_on_floor():

		print("Standing on the floor.")
```

Run the scene.

Stand on the floor.

Observe.

Walk off a ledge.

Observe.

The message immediately stops.

---

# How It Works

After:

```gdscript
move_and_slide()
```

CharacterBody3D automatically determines whether it is standing on a walkable surface.

Instead of inspecting every collision yourself, you simply ask:

```gdscript
is_on_floor()
```

Godot has already done the work.

---

# Why Not Check Every Collision?

Earlier we learned how to iterate through collision information.

That approach is still useful.

However...

Detecting whether the player is standing on the ground is such a common task that CharacterBody3D provides a dedicated function.

Whenever the engine provides a higher-level tool, prefer using it.

It is usually:

- simpler
- easier to read
- less error-prone

---

# Experiment

Only change one thing.

---

### Experiment A

Stand on the floor.

Observe.

---

### Experiment B

Walk off the edge.

Observe.

When does `is_on_floor()` become false?

---

### Experiment C

Create a small platform.

Jump (or fall) onto it.

Observe.

Does Godot recognize it as a floor?

---

### Experiment D

Print both:

```gdscript
print(is_on_floor())
```

and

```gdscript
print(get_slide_collision_count())
```

Observe.

Notice that collisions and floor detection are related—but not identical.

---

### Experiment E

Replace:

```gdscript
print("Standing on the floor.")
```

with:

```gdscript
$MeshInstance3D.visible = is_on_floor()
```

Observe.

The object now visually indicates whether it is grounded.

---

# Practical Applications

Floor detection appears throughout games.

Examples include:

- enabling jumps
- playing landing sounds
- resetting double jumps
- starting idle animations
- detecting falling
- enabling sprinting

Many player mechanics begin by asking:

> **Am I standing on something?**

---

# Common Misconceptions

### "Any collision means I'm on the floor."

Not necessarily.

You may have collided with:

- a wall
- a ceiling
- another player

Floor detection is a more specific question.

---

### "I need to inspect every collision."

Usually not.

CharacterBody3D already provides this information.

---

### "`is_on_floor()` works before `move_and_slide()`."

It does not.

The information is updated **after** movement has been resolved.

Always call:

```gdscript
move_and_slide()
```

before checking:

```gdscript
is_on_floor()
```

---

# Workbench Habit

Before writing a complex collision loop, ask yourself:

> **Does CharacterBody3D already provide this information?**

Many common gameplay questions already have built-in helper functions.

Using them often makes your code shorter and easier to understand.

---

# Challenge

Build a simple level with:

- one floor
- one platform
- one pit

Print:

```text
Grounded
```

only while the player is standing on a surface.

Then print:

```text
Falling
```

whenever the player walks off an edge.

Notice how a single built-in function can become the foundation for many gameplay systems.