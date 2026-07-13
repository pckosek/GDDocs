# Technique 5.3 — Timer Events

## Classification

**Type:** Event Systems Technique

**Category:** Event Systems

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Many game events should happen...

...but not immediately.

Examples include:

* A door opens after two seconds.
* An explosion occurs after a countdown.
* An enemy attacks once every second.
* A power-up expires after ten seconds.
* A message disappears after three seconds.

These systems are not responding to:

* continuous updates
* player input

Instead they are responding to **time itself**.

---

# Why This Technique Matters

A timer allows your code to wait.

Instead of constantly asking:

> "Has enough time passed?"

Godot keeps track of time for you.

When the timer finishes...

it notifies your object.

This allows your code to remain simple and event-driven.

---

# Mental Model

Imagine baking cookies.

You don't stand beside the oven asking every second:

> "Are they finished yet?"

Instead...

You set a timer.

When the timer rings...

you act.

Game timers work exactly the same way.

---

# Starter Implementation

Create a **Timer** node.

Configure:

```text
Wait Time = 2.0

One Shot = Off

Autostart = On
```

Connect the Timer's:

```text
timeout()
```

signal to your script.

Your script should look similar to:

```gdscript
extends Node3D

func _on_timer_timeout():
	print("Two seconds passed!")
```

Run the scene.

Observe.

Every two seconds the message appears.

Notice that no code inside `_process()` was required.

 ---------------------
Starter Implementation B — Runtime Timer

Sometimes you don't want to permanently place a Timer node in the scene.

Instead, you can create one entirely through code.

extends Node3D

func _ready():

	var timer := Timer.new()

	timer.wait_time = 2.0
	timer.one_shot = false
	timer.autostart = true

	timer.timeout.connect(_on_timer_timeout)

	add_child(timer)

func _on_timer_timeout():
	print("Two seconds passed!")

Run the scene.

The behavior should be identical to the previous implementation.

The only difference is how the Timer was created.


---

# Dissecting the Code

Unlike:

```gdscript
_process(delta)
```

the timeout function never executes continuously.

Instead, Godot waits.

When the timer reaches zero...

it emits the:

```text
timeout
```

signal.

Only then does your callback execute.

---

Notice that your script never asks:

> "Has two seconds passed?"

The Timer keeps track of time.

Your object simply responds.

---

# Design Principle

## Let systems specialize.

Timers are good at measuring time.

Your scripts are good at making decisions.

Allow each system to perform the task it was designed for.

Good software often comes from allowing different systems to specialize.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Change:

```text
Wait Time

2.0

↓

0.5
```

Observe.

---

### Experiment B

Change:

```text
One Shot

Off

↓

On
```

Observe.

How does the behavior change?

---

### Experiment C

Instead of:

```gdscript
print("Two seconds passed!")
```

rotate the object.

```gdscript
rotation.y += PI / 4
```

Observe.

Now the object rotates every two seconds.

---

### Experiment D

Instead of rotating...

change the material.

Or change the object's position.

Or spawn another object.

Notice:

The timer doesn't care **what** happens.

It simply decides **when** it happens.

---

# Practical Applications

Timers appear throughout game development.

Examples include:

### Enemy Attacks

Attack every three seconds.

---

### Particle Effects

Destroy after five seconds.

---

### Cooldowns

Prevent repeated actions.

---

### Delayed Doors

Open after a short pause.

---

### Power-Ups

Expire after a fixed duration.

---

Many game systems become dramatically simpler once timers are introduced.

---

# Common Misconceptions

### "Timers replace `_process()`."

No.

Timers execute occasionally.

`_process()` executes continuously.

---

### "Timers are only for clocks."

Any delayed behavior can often be expressed using a timer.

---

### "I should count frames myself."

Usually not.

Godot already provides robust timing systems.

Use them.

---

### "A timer controls the behavior."

Not exactly.

The timer controls **when** the behavior begins.

Your callback determines **what** happens.

---

# Challenge

Create three timers.

Timer A

Prints a message every second.

---

Timer B

Rotates an object every half second.

---

Timer C

Changes the object's color every three seconds.

Before running the scene...

Predict:

Will the three timers interfere with one another?

Now test your prediction.

---

# Reflection

Complete the sentence:

> A timer is useful when...

Now answer:

Can you think of three situations where using a timer would be simpler than checking the elapsed time every frame?

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain why timers are event-driven?

✓ Can I distinguish between `_process()` and `timeout()`?

✓ Can I configure a repeating timer?

✓ Can I decide when a timer is more appropriate than continuous updates?

---

# Looking Ahead

So far, we have explored three different ways that code begins executing.

| Cause        | Callback        |
| ------------ | --------------- |
| Every frame  | `_process()`    |
| Player input | `_input(event)` |
| Time elapsed | `timeout()`     |

Next, we'll explore one of the most powerful ideas in Godot:

Objects can notify one another when something interesting happens.

That mechanism is called a **Signal**, and it forms the backbone of communication between independent systems.
