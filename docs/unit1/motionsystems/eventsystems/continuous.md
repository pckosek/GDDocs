# Technique 5.1 — Continuous Updates

## Classification

**Type:** Event Systems Technique

**Category:** Event Systems

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Not all code should execute continuously.

Some code should only run:

* when the player presses a key
* when a collision occurs
* when a timer finishes

But other systems must update **every frame**.

Examples include:

* movement
* cameras
* animations
* timers
* visual effects

How does Godot know which code should run continuously?

The answer is the **process loop**.

---

# Why This Technique Matters

Games are not executed from beginning to end like traditional programs.

Instead, they continuously update.

Every rendered frame, Godot asks every active object:

> **"Do you have anything to do?"**

Objects that implement:

```gdscript
_process(delta)
```

have an opportunity to respond.

---

# Mental Model

Imagine standing beside a river.

Every second the water flows past.

You do not decide when the river moves.

The river is already flowing.

You simply choose what to do while it passes.

The game loop works similarly.

Frames continue arriving.

Your code simply participates in that continuous flow.

---

# Starter Implementation

Attach the following script to any **Node3D**.

```gdscript
extends Node3D

var frame_count := 0

func _process(delta):

	frame_count += 1

	print(frame_count)
```

Run the scene.

Observe the Output window.

The numbers should increase continuously.

Nothing is moving.

Nothing is being animated.

Yet the code continues executing.

---

# Dissecting the Code

Notice that this script never calls:

```gdscript
_process()
```

Godot does.

Every frame, the engine automatically invokes:

```gdscript
func _process(delta):
```

This means your object participates in the continuous update loop simply by defining the function.

---

The variable:

```gdscript
frame_count
```

exists only so that we can observe the update loop in action.

It is evidence that the function continues executing.

---

# Design Principle

## Some questions must be asked continuously.

Imagine asking:

> Is the player moving?

only once.

That information would immediately become outdated.

Instead, games repeatedly ask:

* Has the player moved?
* Has enough time passed?
* Has the camera changed?
* Should this animation continue?

Continuous systems depend upon continuous observation.

---

# Experiment

Modify one thing at a time.

---

### Experiment A

Replace:

```gdscript
print(frame_count)
```

with:

```gdscript
rotation.y += delta
```

Observe.

The object now rotates continuously.

---

### Experiment B

Replace:

```gdscript
rotation.y
```

with:

```gdscript
position.x
```

Observe.

The object now moves instead.

Notice:

Only one line changed.

---

### Experiment C

Comment out the entire:

```gdscript
_process()
```

function.

Run the scene.

What happens?

---

### Experiment D

Print:

```gdscript
delta
```

instead of:

```gdscript
frame_count
```

Observe.

What kind of values appear?

Do they remain perfectly constant?

---

# Practical Applications

Continuous Updates are used for systems that must evolve every frame.

Examples include:

* player movement
* camera tracking
* enemy movement
* procedural animation
* particle systems
* UI animation

If something should appear continuous, it probably belongs inside the process loop.

---

# Common Misconceptions

### "_process() creates motion."

Not exactly.

It creates **opportunities** for motion.

What you do inside the function determines the behavior.

---

### "_process() runs once."

It runs continuously while the object is active.

---

### "Everything belongs inside _process()."

No.

Many systems should only execute when an event occurs.

Learning that distinction is one of the central ideas of event-driven programming.

---

### "The game waits for my code."

It doesn't.

The game continues updating regardless.

Your object is invited to participate each frame.

---

# Challenge

Create three independent objects.

Object A

Prints:

```gdscript
frame_count
```

---

Object B

Rotates continuously.

---

Object C

Moves continuously.

Ask yourself:

What do these three systems actually have in common?

---

# Reflection

Complete the sentence:

> `_process()` exists because...

Now answer:

Which kinds of systems should **not** use continuous updates?

Try to think of at least three examples.

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain why `_process()` executes repeatedly?

✓ Can I distinguish between continuous systems and event-driven systems?

✓ Can I predict what happens when `_process()` is removed?

✓ Can I explain why movement naturally belongs inside the update loop?

---

# Looking Ahead

Continuous Updates are only one way code can execute.

Many systems should **not** run every frame.

Instead, they should wait.

For example:

* until the player presses a key
* until a timer expires
* until another object enters an area
* until a signal is emitted

Learning when code should execute continuously—and when it should wait—is one of the defining ideas behind event-driven programming.
