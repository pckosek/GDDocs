# Pattern 2.11.5 — Open a Door

## Classification

**Type:** Gameplay Pattern

**Category:** Area Detection

**Difficulty:** Intermediate

**Prerequisites:**

- Area3D
- Signals
- AnimatableBody3D
- Tweening

---

# Problem

Many games contain doors.

The player reaches a trigger.

The trigger tells the door to open.

Notice that these are **two different objects**.

The trigger detects the player.

The door performs the animation.

This is one of the simplest examples of objects communicating with one another.

---

# Starter Implementation

Create the following scene.

```text
World
├── Door (AnimatableBody3D)
└── DoorTrigger (Area3D)
```

Attach the following script to the **DoorTrigger**.

```gdscript
extends Area3D

@export var door : AnimatableBody3D

func _on_body_entered(body):

	if body is CharacterBody3D:

		door.open()
```

Attach the following script to the **Door**.

```gdscript
extends AnimatableBody3D

func open():

	var tween = create_tween()

	tween.tween_property(
		self,
		"position:y",
		position.y + 3,
		1.0
	)
```

Run the scene.

Walk into the trigger.

Observe.

The trigger does not move.

The door does not detect the player.

Instead, the trigger asks the door to perform its own behavior.

---

# How It Works

```text
Player

↓

Area Detects

↓

Signal

↓

Door.open()

↓

Tween Animation
```

Each object performs only one responsibility.

---

# Anatomy

## Area3D

Detects the player.

---

## Door

Knows how to open.

---

## Tween

Animates the movement.

---

Notice that neither object performs the other's job.

---

# Design Principle

## Objects should own their own behavior.

The trigger should not contain door animation code.

Instead, the trigger simply says:

> Open yourself.

The door already knows how to do that.

This separation keeps projects organized as they become larger.

---

# Experiment

Only change one thing.

---

### Experiment A

Increase the Tween duration.

Observe.

How does the door feel?

---

### Experiment B

Instead of moving upward...

Rotate the door.

Observe.

Which feels more believable?

---

### Experiment C

Create two triggers.

Connect both to the same door.

Observe.

Can multiple objects activate the same system?

---

### Experiment D

Create two doors.

Connect one trigger to both.

Observe.

Can one event affect multiple objects?

---

### Experiment E

Comment out:

```gdscript
door.open()
```

Observe.

The trigger still detects the player.

The door simply never receives the message.

---

# Practical Applications

This communication pattern appears throughout games.

Examples include:

- doors
- elevators
- bridges
- pressure plates
- secret passages
- puzzle mechanisms
- traps

Many gameplay systems are simply one object asking another object to perform its own behavior.

---

# Common Misconceptions

### "The trigger opens the door."

Not exactly.

The trigger requests.

The door performs.

---

### "The Area should contain the animation."

Usually not.

Each object should manage its own behavior whenever possible.

---

### "The door should detect the player."

The trigger already performs that job.

Avoid duplicating responsibilities.

---

# Workbench Habit

Whenever one object needs another object to perform an action, ask yourself:

> **Which object should own this behavior?**

Usually the object performing the action should contain the code.

Other systems simply request it.

---

# Challenge

Create a small room containing:

- one player
- one trigger
- one door

Experiment with different opening animations.

Try:

- sliding upward
- rotating
- moving sideways

Notice that the trigger code never changes.

Only the door's implementation changes.

This separation makes your gameplay systems much easier to expand later.