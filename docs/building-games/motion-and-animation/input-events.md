# Technique 5.2 — Input Events

## Classification

**Type:** Event Systems Technique

**Category:** Event Systems

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Not every system needs to ask the player what they are doing every frame.

Sometimes it is more efficient to wait.

Instead of repeatedly asking:

> **"Did the player press a key?"**

the engine can simply tell us:

> **"A key was just pressed."**

This is called an **Input Event**.

---

# Why This Technique Matters

Input Events introduce one of the central ideas of event-driven programming.

Instead of continuously checking the outside world, your object waits.

When something interesting happens, Godot immediately notifies it.

This allows your code to react rather than constantly poll.

---

# Mental Model

Imagine standing at your front door waiting for a package.

One strategy would be:

Every second...

Open the door.

Look outside.

Close the door.

Repeat forever.

A much better strategy is:

Wait.

When the doorbell rings...

Answer it.

Input Events work much like the doorbell.

---

# Starter Implementation

Attach the following script to any **Node3D**.

```gdscript
extends Node3D

func _input(event):

	if event.is_action_pressed("ui_accept"):
		print("Jump!")

	if event.is_action_pressed("ui_cancel"):
		print("Cancel!")
```

Run the scene.

Press the configured actions.

Observe the Output panel.

Notice that nothing happens until an input event occurs.

---

# Dissecting the Code

Unlike:

```gdscript
func _process(delta):
```

which executes continuously,

Godot only calls:

```gdscript
func _input(event):
```

when an input event occurs.

The parameter:

```gdscript
event
```

contains information about what the player just did.

Your object simply decides whether that event is interesting.

---

# Design Principle

## Wait until something happens.

Continuous updates are useful when a system must evolve constantly.

Events are useful when a system should remain inactive until something changes.

Choosing the appropriate model often produces cleaner, simpler programs.

---

# Experiment

Modify one thing at a time.

---

### Experiment A

Replace:

```gdscript
print("Jump!")
```

with:

```gdscript
rotation.y += 0.25
```

Now each key press rotates the object.

---

### Experiment B

Replace:

```gdscript
rotation.y
```

with:

```gdscript
position.x += 1
```

The object now jumps one meter each time the key is pressed.

Notice the difference from continuous motion.

---

### Experiment C

Add another action.

Example:

```text
interact
```

Configure it in the Input Map.

Add another branch to your script.

Observe.

---

### Experiment D

Hold the key down.

Does the behavior feel continuous?

Why or why not?

---

# Practical Applications

Input Events are commonly used for actions that happen once.

Examples include:

* opening doors
* firing a weapon
* jumping
* interacting with an object
* opening menus
* pausing the game

Many of these actions should occur once per button press rather than continuously.

---

# Common Misconceptions

### "Everything belongs in `_process()`."

Not necessarily.

Many actions occur only when an event happens.

---

### "Input Events replace `_process()`."

No.

Both systems are useful.

They solve different problems.

---

### "Events are continuously checking the keyboard."

They are not.

Godot delivers the event to your object only when something changes.

---

### "`_input()` is only for keyboards."

Input Events can also represent:

* mouse buttons
* mouse movement
* game controllers
* touch events

The same programming model applies.

---

# Challenge

Build a simple object.

Implement two behaviors.

Behavior A

The object rotates continuously using:

```gdscript
_process()
```

Behavior B

The object changes color whenever the player presses Space using:

```gdscript
_input()
```

Before running the scene, ask yourself:

Why do these two behaviors belong in different functions?

---

# Reflection

Complete the sentence:

> Input Events are different from Continuous Updates because...

Now answer:

Can you think of three situations where waiting for an event is preferable to checking every frame?

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain the difference between `_process()` and `_input()`?

✓ Can I identify behaviors that should only happen once?

✓ Can I configure a new Input Action?

✓ Can I decide whether a problem is better solved with continuous updates or an input event?

---

# Looking Ahead

Player input is only one kind of event.

Soon you'll discover that games respond to many other events as well.

Examples include:

* timers finishing
* objects colliding
* buttons being pressed
* signals being emitted

The programming pattern remains the same:

Wait.

React.

Continue.
