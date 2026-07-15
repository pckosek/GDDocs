# Technique 4.3 — Autonomous Motion

## Classification

**Type:** Motion Systems Technique

**Category:** Motion Systems

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Problem

Not everything in a game moves because of the player.

Some objects move simply because that is what they do.

Examples include:

* ceiling fans
* rotating collectibles
* orbiting satellites
* moving platforms
* floating pickups
* blinking lights

These objects are not reacting to input.

They are following their own rules.

This is called **autonomous motion**.

---

# Why This Technique Matters

Autonomous motion makes worlds feel alive.

A completely static environment often feels artificial.

Small, continuous behaviors suggest that the world exists independently of the player.

Many of the most memorable game environments contain objects that quietly animate themselves.

---

# Starter Implementation

Attach the following script to any **Node3D**.

```gdscript
extends Node3D

@export var rotation_speed := 1.5

func _process(delta):
	rotation.y += rotation_speed * delta
```

Run the scene.

The object should rotate continuously around its Y-axis.

Notice that no keyboard input is required.

The object simply continues moving.

---

# Dissecting the Code

Compare this script to the previous technique.

Previously we asked:

```gdscript
Input.is_action_pressed(...)
```

This script asks nothing.

Every frame it simply performs:

```gdscript
rotation.y += rotation_speed * delta
```

The object decides its own behavior.

No player interaction is required.

---

# Design Principle

## Some systems should act independently.

Games become more believable when the world continues functioning without the player's involvement.

Autonomous systems suggest that the world has its own rules.

The player enters that world rather than creating it.

---

# Experiment

Only modify one thing at a time.

---

### Experiment A

Change:

```gdscript
rotation.y
```

to:

```gdscript
rotation.x
```

Observe.

---

### Experiment B

Change:

```gdscript
rotation.y
```

to:

```gdscript
rotation.z
```

Observe.

How does rotating around different axes change the feeling?

---

### Experiment C

Reverse the direction.

```gdscript
rotation_speed = -1.5
```

Observe.

---

### Experiment D

Increase the speed dramatically.

```gdscript
rotation_speed = 10
```

Does it still feel believable?

---

### Experiment E

Replace rotation with movement.

```gdscript
position.y += sin(Time.get_ticks_msec() / 500.0) * delta
```

Observe.

The object now appears to float rather than spin.

Notice that the object is still autonomous.

Only the behavior changed.

---

# Investigation

Build three autonomous objects.

Object A

Continuously rotates.

---

Object B

Moves slowly upward and downward.

---

Object C

Orbits another object using a transform hierarchy.

Observe all three together.

Ask yourself:

Do they feel like they belong to the same world?

Why?

---

# Common Patterns

Autonomous motion appears everywhere.

Examples include:

### Rotation

Fans

Coins

Satellites

---

### Oscillation

Floating pickups

Elevators

Platforms

---

### Orbiting

Planets

Moons

Magic effects

---

### Continuous Translation

Moving walkways

Conveyor belts

Scrolling backgrounds

---

Although these systems look different, they all share one idea:

The object controls itself.

---

# Reflection

Complete the sentence:

> Autonomous motion differs from responsive motion because...

Now answer:

What kinds of objects in the real world move without waiting for someone to interact with them?

Can you think of three examples that would make interesting game objects?

---

# Common Mistakes

### Giving Every Object Motion

Not everything needs to move.

Autonomous motion is most effective when used intentionally.

---

### Moving Too Fast

Small motions often feel more believable than dramatic ones.

Experiment before deciding.

---

### Forgetting Delta

As before, autonomous systems should generally include:

```gdscript
* delta
```

to remain frame-rate independent.

---

### Combining Too Many Behaviors

Start with one simple behavior.

Once it feels correct, consider combining multiple forms of motion.

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain the difference between responsive and autonomous motion?

✓ Can I create an object that moves without player input?

✓ Can I identify examples of autonomous motion in games?

✓ Can I imagine ways to make an environment feel more alive?

---

# Looking Ahead

So far, we have explored three sources of motion:

| Source | Example             |
| ------ | ------------------- |
| Time   | Continuous movement |
| Player | Responsive movement |
| Object | Autonomous movement |

Next, we'll explore a different question.

Not:

> **Who controls the motion?**

Instead:

> **How should the motion feel?**

Sometimes objects should move instantly.

Sometimes they should ease into place.

Sometimes they should accelerate naturally.

Those choices lead us into interpolation, tweening, and motion refinement.
