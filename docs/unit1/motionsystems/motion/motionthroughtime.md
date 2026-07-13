# Technique 4.1 — Motion Through Time

## Classification

**Type:** Motion Systems Technique

**Category:** Motion Systems

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Until now, every object we have created has been static.

It has:

* a position
* a rotation
* a scale

But nothing changes.

Games are different.

Objects move.

Not once.

Continuously.

The question is no longer:

> **"Where is this object?"**

The question becomes:

> **"How does this object change over time?"**

---

# Why This Technique Matters

Motion is one of the defining characteristics of an interactive world.

The same scene can feel:

* lifeless
* mechanical
* playful
* dynamic

simply because objects begin changing over time.

Understanding continuous motion is the foundation for nearly every system that follows in this course.

---

# Starter Implementation

Attach the following script to any **Node3D** or **MeshInstance3D**.

```gdscript
extends Node3D

@export var speed : float = 2.0

func _process(delta):
	position.x += speed * delta
```

Run the scene.

Your object should move continuously along the positive X-axis.

Congratulations.

You have created your first continuously moving object.

---

# Dissecting the Code

Let's examine one line at a time.

---

### The Process Function

```gdscript
func _process(delta):
```

Godot automatically calls this function once every rendered frame.

This means your code is executed:

```
Frame
↓

Frame

↓

Frame

↓

Frame

↓

...
```

As long as the game is running.

---

### The Speed Variable

```gdscript
@export var speed = 2.0
```

This controls:

> **How much movement occurs each second.**

Try changing:

```gdscript
2
```

to:

```gdscript
10
```

Observe the result.

---

### Changing Position

```gdscript
position.x +=
```

This tells Godot:

> Every frame, increase the X position a little.

The object is not "moving."

It is being placed in a slightly different position every frame.

Motion emerges from those repeated changes.

---

### Delta

```gdscript
speed * delta
```

Delta represents the amount of time that has passed since the previous frame.

Multiplying by delta keeps movement approximately consistent across different computers.

For now, you do not need to fully understand delta.

Simply recognize that it allows motion to happen **over time**, rather than **per frame**.

We will revisit this idea repeatedly throughout the course.

---

# Experiment

Run the script several times.

Only change one thing each time.

---

### Experiment A

Change:

```gdscript
position.x
```

to:

```gdscript
position.z
```

What changes?

---

### Experiment B

Change:

```gdscript
position.x
```

to:

```gdscript
position.y
```

What changes?

---

### Experiment C

Set:

```gdscript
speed = 20
```

Observe.

---

### Experiment D

Set:

```gdscript
speed = 0.2
```

Observe.

---

### Experiment E

Comment out:

```gdscript
* delta
```

Observe what happens.

Does the movement still feel the same?

Why might this become a problem?

---

# Design Principle

## Motion is many small changes.

Beginning programmers often imagine motion as:

```
Position A

↓

Position B
```

Game engines think differently.

```
Position

↓

Small Change

↓

Small Change

↓

Small Change

↓

...
```

Smooth motion emerges from hundreds or thousands of tiny updates.

---

# Challenge

Create three cubes.

Cube A

Moves along:

```gdscript
position.x
```

Cube B

Moves along:

```gdscript
position.y
```

Cube C

Moves along:

```gdscript
position.z
```

Before running the scene:

Predict how each cube will move.

Now test your prediction.

---

# Reflection

Complete the following sentence.

> Motion is created because...

Now answer:

What would happen if `_process()` only executed once?

---

# Common Mistakes

### Forgetting Delta

Movement speed changes dramatically depending on frame rate.

For now:

Always include:

```gdscript
* delta
```

unless you have a specific reason not to.

---

### Changing Multiple Variables At Once

When experimenting, change one thing.

Observe.

Then change another.

Small experiments make cause and effect easier to understand.

---

### Thinking the Object Is "Moving"

The object is actually being repositioned repeatedly.

Motion is the result of those repeated updates.

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain why `_process()` creates continuous motion?

✓ Can I predict how changing `position.x` to `position.z` changes behavior?

✓ Can I explain what the `speed` variable controls?

✓ Can I explain why changing something every frame produces motion?

---

# Looking Ahead

This script moved because **you** told it exactly where to go.

In the next techniques, we'll begin asking a different question.

What if the movement should respond to:

* the player?
* another object?
* its own internal behavior?

Those different sources of motion all build upon the same idea you explored here:

> Motion is simply the continuous modification of an object's transform over time.
