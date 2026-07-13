# Pattern 2.12.5 — Patrol Between Walls

## Classification

**Type:** Movement Pattern

**Category:** Character Movement

**Difficulty:** Intermediate

**Prerequisites:**

- CharacterBody3D
- move_and_slide()
- Detect Every Collision
- Identify What I Collided With

---

# Problem

Many games contain simple enemies that continuously patrol an area.

Examples include:

- guards
- robots
- moving hazards
- security drones
- wildlife

A simple patrol requires only one rule:

> Move until you hit a wall.

Then...

Turn around.

---

# Starter Implementation

Create the following scene.

```text
World
├── Left Wall (StaticBody3D)
├── Right Wall (StaticBody3D)
└── Guard (CharacterBody3D)
```

Attach the following script.

```gdscript
extends CharacterBody3D

@export var speed := 3.0

var direction := Vector3.RIGHT

func _physics_process(delta):

	velocity = direction * speed

	move_and_slide()

	for i in get_slide_collision_count():

		var collision = get_slide_collision(i)

		if collision.get_collider() is StaticBody3D:

			direction *= -1
```

Run the scene.

Observe.

The guard walks back and forth between the walls.

---

# How It Works

Every frame:

```text
Move

↓

Collision?

↓

Yes

↓

Reverse Direction

↓

Continue
```

Notice that the guard never knows where the walls are.

It simply reacts to the world around it.

---

# Anatomy

## direction

Stores the current movement direction.

---

## velocity

Moves the CharacterBody.

---

## Collision Detection

Determines whether the guard struck a wall.

---

## direction *= -1

Reverses movement.

The guard immediately begins walking in the opposite direction.

---

# Design Principle

## Simple rules create believable behavior.

This patrol system has no:

- pathfinding
- navigation mesh
- AI
- decision tree

It simply follows one rule:

> If I hit a wall...

Turn around.

Many convincing behaviors emerge from surprisingly simple rules.

---

# Experiment

Only change one thing.

---

### Experiment A

Increase:

```gdscript
speed
```

Observe.

---

### Experiment B

Create a longer hallway.

Observe.

How does the patrol change?

---

### Experiment C

Create a narrow hallway.

Observe.

---

### Experiment D

Replace:

```gdscript
direction *= -1
```

with:

```gdscript
direction = Vector3.LEFT
```

Observe.

Can the guard ever move right again?

Why?

---

### Experiment E

Create several guards.

Give each a different speed.

Observe.

How much more alive does the world feel?

---

# Practical Applications

This pattern appears throughout games.

Examples include:

- guards
- moving hazards
- robots
- patrolling enemies
- decorative NPCs
- conveyor robots

Many autonomous systems begin with this exact behavior.

---

# Common Misconceptions

### "This is artificial intelligence."

Not really.

The guard follows one simple rule.

More sophisticated AI builds upon many patterns like this.

---

### "The wall tells the guard to turn."

No.

The guard detects the collision.

The guard decides what to do.

---

### "The guard knows where the walls are."

It doesn't.

It simply reacts whenever a collision occurs.

---

# Workbench Habit

Many autonomous systems follow the same pattern.

```text
Move

↓

Observe

↓

Decide

↓

Repeat
```

Keeping those stages separate makes behavior much easier to expand later.

---

# Challenge

Build a simple hallway.

Create three guards.

Give each:

- a different speed
- a different starting position
- a different initial direction

Observe.

Although every guard uses exactly the same code, the hallway immediately feels much more dynamic.

Now ask yourself:

How might you extend this pattern so the guard:

- pauses before turning?
- chases the player?
- investigates a sound?

Notice that each new behavior begins with the same simple patrol pattern.