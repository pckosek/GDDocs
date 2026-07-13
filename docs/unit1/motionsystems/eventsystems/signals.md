# Technique 5.4 — Signals

## Classification

**Type:** Event Systems Technique

**Category:** Event Systems

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Problem

As projects become larger, objects begin needing to communicate.

Examples include:

* A button opens a door.
* A timer starts an animation.
* A player collects a coin.
* A pressure plate activates a trap.
* An enemy dies and updates the score.

How can one object notify another that something has happened?

Godot solves this problem using **Signals**.

---

# Why This Technique Matters

Signals allow objects to communicate without needing to know how the other object works.

Instead of saying:

> "Open the door."

an object simply announces:

> **"The button was pressed."**

Any object that cares can respond.

This keeps systems:

* modular
* reusable
* easier to maintain

---

# Mental Model

Imagine a fire alarm.

The alarm does not know:

* who will evacuate
* who will call 911
* who will unlock the exits

It simply broadcasts:

> **"Fire!"**

Everyone who is listening decides what to do.

Signals work the same way.

---

# Starter Implementation A — Editor Connection

Create:

```text
Button
```

In the Node dock:

Select:

```text
pressed()
```

Press:

```text
Connect...
```

Connect the signal to a script.

Godot will generate:

```gdscript
func _on_button_pressed():
	print("Button Pressed!")
```

Run the scene.

Press the button.

Observe.

The function is never called directly.

The signal causes it to execute.

---

# Starter Implementation B — Code Connection

Signals can also be connected entirely through code.

```gdscript
extends Node

func _ready():

	$Button.pressed.connect(_on_button_pressed)

func _on_button_pressed():

	print("Button Pressed!")
```

The behavior is identical.

The only difference is where the connection was created.

---

# Dissecting the Code

Notice something unusual.

Nowhere in your script do you write:

```gdscript
_on_button_pressed()
```

Instead:

```text
Button Pressed

↓

Button emits Signal

↓

Signal reaches Listener

↓

Function executes
```

The function runs because the signal was emitted.

Not because another function called it directly.

---

# Design Principle

## Announce events.

Do not command objects.

Signals communicate:

> **Something happened.**

They do **not** communicate:

> **Do this specific thing.**

This distinction makes systems much easier to reuse.

---

# Experiment

Modify one thing at a time.

---

### Experiment A

Replace:

```gdscript
print("Button Pressed!")
```

with:

```gdscript
rotation.y += PI / 4
```

Observe.

---

### Experiment B

Connect two different objects to the same signal.

Observe.

One button press.

Two independent responses.

---

### Experiment C

Disconnect one listener.

Observe.

Does the other continue working?

---

### Experiment D

Replace the Button with another node that emits a signal.

Examples:

* Timer
* Area3D
* AnimationPlayer

Observe.

Notice that the pattern remains the same.

Only the event changes.

---

# Practical Applications

Signals appear everywhere in Godot.

Examples include:

### Buttons

```text
pressed()
```

---

### Timers

```text
timeout()
```

---

### Area3D

```text
body_entered()
```

---

### AnimationPlayer

```text
animation_finished()
```

---

### Custom Signals

Objects can even create their own signals.

As projects become larger, this becomes an increasingly common design pattern.

---

# Common Misconceptions

### "Signals call functions."

Not exactly.

Signals **emit events**.

Connected functions respond.

---

### "Signals only work with UI."

Almost every major Godot system uses signals.

---

### "Objects must know about one another."

Signals reduce coupling.

The emitter often has no knowledge of who is listening.

---

### "Signals replace function calls."

No.

Signals and function calls solve different communication problems.

---

# Challenge

Create a simple scene.

One Button.

Two Cubes.

Connect both cubes to the same signal.

When the button is pressed:

Cube A rotates.

Cube B changes color.

Before running the scene...

Predict:

How many functions will execute?

Now test your prediction.

---

# Reflection

Complete the sentence:

> Signals allow objects to...

Now answer:

Why might signals produce a cleaner design than directly calling another object's function?

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain what a signal is?

✓ Can I connect a signal using the editor?

✓ Can I connect a signal using code?

✓ Can I explain why signals reduce dependencies between objects?

---

# Looking Ahead

You now know four major ways that code can begin executing.

| Cause                | Example         |
| -------------------- | --------------- |
| Continuous Update    | `_process()`    |
| Player Input         | `_input(event)` |
| Timer                | `timeout()`     |
| Object Communication | Signals         |

As your projects become larger, these systems will begin working together.

A player presses a button.

↓

The button emits a signal.

↓

A timer begins.

↓

When the timer finishes...

↓

A door opens.

None of these systems need to know how the others work.

They simply communicate through events.

That ability to compose independent systems is one of the defining strengths of Godot's architecture.
