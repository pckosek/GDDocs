# Technique 2.11 — Scoring a Goal

## Classification

**Type:** Engineering Technique

**Category:** Physical Interaction

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Scenario

You are building a simple soccer goal.

The goal should:

- allow the ball to enter
- detect when the ball crosses the goal line
- increase the score
- not physically block the ball

The player does not score the goal.

The **ball** does.

This introduces one of the first gameplay systems where multiple independent objects cooperate.

---

# Why This Technique Matters

Up until now, most interactions have involved the player.

This technique demonstrates something important:

> Objects can interact with one another without the player's direct involvement.

The player merely creates the opportunity.

The game world handles the rest.

---

# Starter Implementation

Create the following scene.

```text
World
├── Ball (RigidBody3D)
└── Goal (Area3D)
```

Connect the Goal's:

```text
body_entered()
```

signal.

Attach the following script.

```gdscript
extends Area3D

var score := 0

func _on_body_entered(body):

	if body is RigidBody3D:

		score += 1

		print("GOAL!")
		print("Score:", score)
```

Run the scene.

Roll the ball into the goal.

Observe.

The ball continues moving naturally.

The goal detects the overlap.

The score increases.

---

# Anatomy of the Interaction

Three independent systems cooperate.

```text
RigidBody3D

↓

Area3D

↓

Signal

↓

Score
```

Each system performs one responsibility.

None of them know how the others are implemented.

---

# Design Principle

## Gameplay often emerges from communication.

The ball does not know what a goal is.

The goal does not know how the ball moves.

The score does not know anything about physics.

Each system simply performs its own responsibility.

Together they create gameplay.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Replace:

```gdscript
print("GOAL!")
```

with:

```gdscript
body.queue_free()
```

Observe.

The ball disappears after scoring.

---

### Experiment B

Replace:

```gdscript
score += 1
```

with:

```gdscript
score += 5
```

Observe.

---

### Experiment C

Create two goals.

Observe.

Does each maintain its own score?

---

### Experiment D

Roll two balls into the goal.

Observe.

Does each trigger the Area independently?

---

### Experiment E

Replace the ball with a CharacterBody3D.

Observe.

Should the player also score?

If not...

How could the script distinguish between different body types?

---

# Practical Observation

Many gameplay mechanics follow exactly this pattern.

Examples include:

- basketball hoops
- checkpoints
- collectible items
- capture zones
- pressure plates
- finish lines

A moving object enters an Area.

The Area emits a signal.

The game reacts.

---

# Common Uses

RigidBody3D interacting with Area3D commonly represents:

- scoring goals
- baskets
- targets
- object collection
- puzzle objectives
- delivery zones

The pattern appears throughout game development.

---

# Common Misconceptions

### "The Area stops the ball."

No.

The Area detects.

It does not obstruct.

---

### "The ball scores itself."

No.

The Area detects the interaction.

The Area updates the score.

---

### "Gameplay belongs inside the ball."

Usually not.

The ball simply behaves like a ball.

The gameplay emerges from interaction.

---

### "Signals are only for buttons."

Signals connect many different gameplay systems.

Area3D is one of the most common examples.

---

# Reflection

Complete the sentence.

> Gameplay emerged because...

Now answer:

Which object is responsible for:

- moving?
- detecting?
- scoring?

Why is that separation useful?

---

# Self Check

Before moving on, ask yourself:

✓ I understand how RigidBody3D and Area3D interact.

✓ I can detect when a ball enters a goal.

✓ I understand how Signals connect gameplay systems.

✓ I can explain why each object has a separate responsibility.

---

# Looking Ahead

By this point, you've built several interactions between physical systems.

CharacterBody3D ↔ StaticBody3D

CharacterBody3D ↔ AnimatableBody3D

RigidBody3D ↔ Area3D

Notice a pattern.

Interesting gameplay rarely comes from a single object.

It emerges from multiple simple systems working together.

This idea will continue throughout the remainder of the course, where independent systems begin combining into increasingly complex games.