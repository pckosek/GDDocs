# Pattern 2.12.6 — Patrol Between Points

## Classification

**Type:** Movement Pattern

**Category:** NPC Movement

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- Movement
- Distance Calculation

---

# Problem

Many NPCs patrol between specific locations.

Examples include:

- guards
- security robots
- wildlife
- moving hazards
- tour guides

Unlike wall patrols, these NPCs are not reacting to collisions.

Instead, they are intentionally moving toward destinations.

---

# Starter Implementation

Create the following scene.

```text
World
├── PointA (Marker3D)
├── PointB (Marker3D)
└── Guard (CharacterBody3D)
```

Attach the following script to the Guard.

```gdscript
extends CharacterBody3D

@export var speed := 3.0

@export var point_a : Marker3D
@export var point_b : Marker3D

var target : Marker3D

func _ready():

	target = point_b

func _physics_process(delta):

	var direction = (target.global_position - global_position).normalized()

	velocity = direction * speed

	move_and_slide()

	if global_position.distance_to(target.global_position) < 0.25:

		if target == point_a:

			target = point_b

		else:

			target = point_a
```

Run the scene.

Observe.

The guard continuously walks back and forth between the two markers.

---

# How It Works

```text
Choose Target

↓

Move Toward Target

↓

Arrive

↓

Choose New Target

↓

Repeat
```

Unlike the previous patrol pattern, the NPC is no longer waiting for a collision.

It already knows where it wants to go.

---

# Anatomy

## PointA

One patrol destination.

---

## PointB

The second patrol destination.

---

## target

Stores the NPC's current goal.

---

## distance_to()

Determines when the destination has been reached.

---

# Design Principle

## Movement often begins with a goal.

The NPC is not wandering randomly.

It always has a destination.

Many AI systems begin with this simple idea.

As goals become more sophisticated, behavior becomes more believable.

---

# Experiment

Only change one thing.

---

### Experiment A

Move PointA.

Observe.

The patrol automatically updates.

---

### Experiment B

Move PointB.

Observe.

---

### Experiment C

Increase:

```gdscript
speed
```

Observe.

---

### Experiment D

Reduce the distance threshold.

```gdscript
0.25
```

↓

```gdscript
0.05
```

Observe.

Does the NPC overshoot?

---

### Experiment E

Create a much larger patrol route.

Observe.

The same code works without modification.

---

# Practical Applications

Point patrols appear throughout games.

Examples include:

- guards
- civilians
- wildlife
- drones
- maintenance robots
- decorative NPCs

Many AI systems begin by moving between predefined locations.

---

# Common Misconceptions

### "The NPC needs collisions to patrol."

Not necessarily.

This patrol depends on destinations rather than walls.

---

### "The NPC knows where it is."

The NPC continuously measures its distance to the current target.

---

### "Markers are visible in the game."

Marker3Ds exist primarily as editor tools.

They define useful locations within the level.

---

# Workbench Habit

Whenever an object should move intentionally rather than reactively, ask yourself:

> **Where is it trying to go?**

Many gameplay systems become much simpler once destinations are represented explicitly.

---

# Challenge

Create a simple museum.

Place four guards.

Give each guard a different pair of patrol points.

Experiment with:

- long patrols
- short patrols
- overlapping patrols

Notice that each NPC behaves differently even though every guard uses exactly the same script.

The only thing that changes is the location of the patrol points.