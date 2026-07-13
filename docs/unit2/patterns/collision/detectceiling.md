# Pattern 2.10.7 — Detect the Ceiling

## Classification

**Type:** Gameplay Pattern

**Category:** CharacterBody3D

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- move_and_slide()

---

# Problem

Sometimes your game needs to know:

> **Did the player hit the ceiling?**

Examples include:

- stopping a jump
- preventing continued upward movement
- playing a "bonk" sound
- spawning impact particles
- triggering traps

Rather than inspecting every collision manually, CharacterBody3D already provides this information.

---

# Starter Implementation

Attach the following code to a **CharacterBody3D**.

```gdscript
extends CharacterBody3D

func _physics_process(delta):

	# Movement code goes here...

	move_and_slide()

	if is_on_ceiling():

		print("Hit the ceiling!")
```

Run the scene.

Create a low ceiling above the player.

Jump into it.

Observe.

The message appears only while the player is contacting the ceiling.

---

# How It Works

After:

```gdscript
move_and_slide()
```

CharacterBody3D analyzes all collisions from the current frame.

If one of those collisions is considered a ceiling contact,

```gdscript
is_on_ceiling()
```

returns:

```gdscript
true
```

You do not need to inspect the collision list yourself.

---

# Why Not Check Collision Normals?

Earlier we learned how to inspect collision normals manually.

That approach still works.

However, ceiling detection is such a common gameplay question that CharacterBody3D already answers it for us.

Whenever possible, use the built-in helper functions.

They communicate your intent much more clearly.

---

# Experiment

Only change one thing.

---

### Experiment A

Create a low ceiling.

Jump into it.

Observe.

---

### Experiment B

Raise the ceiling.

Observe.

Does the player still trigger ceiling detection?

---

### Experiment C

Replace:

```gdscript
print("Hit the ceiling!")
```

with:

```gdscript
velocity.y = 0
```

Observe.

How does this change the jump?

---

### Experiment D

Print both:

```gdscript
is_on_floor()
```

and

```gdscript
is_on_ceiling()
```

Observe.

Can both be true at the same time?

Under what circumstances?

---

### Experiment E

Add several ceilings at different heights.

Observe.

Does CharacterBody3D detect all of them correctly?

---

# Practical Applications

Ceiling detection appears throughout games.

Examples include:

- cancelling jumps
- preventing upward movement
- cave exploration
- climbing systems
- head-bump effects
- platforming mechanics

Many movement systems rely on knowing when upward movement should stop.

---

# Common Misconceptions

### "The player automatically stops when hitting the ceiling."

Collision prevents the player from passing through the ceiling.

Your gameplay code still decides what additional behavior should occur.

---

### "Every collision above the player is a ceiling."

CharacterBody3D determines this automatically based on the collision geometry.

---

### "I should inspect every collision."

Usually not.

`is_on_ceiling()` already answers the gameplay question directly.

---

### "This only matters for jumping."

Ceiling detection is useful for many gameplay systems beyond jumping.

Any movement involving vertical space can benefit from it.

---

# Workbench Habit

When your gameplay asks:

> **Did I hit the ceiling?**

start with:

```gdscript
is_on_ceiling()
```

before writing more complicated collision detection code.

The engine already understands this common situation.

---

# Challenge

Build a simple room containing:

- a floor
- a ceiling
- a player

When the player touches the ceiling:

- print a message
- stop upward movement
- change the player's color (optional)

Experiment with different ceiling heights.

Observe how the gameplay changes as the available vertical space becomes smaller.