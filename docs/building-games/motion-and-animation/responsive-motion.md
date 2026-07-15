# Technique 4.2 — Responsive Motion

## Classification

**Type:** Motion Systems Technique

**Category:** Motion Systems

**Difficulty:** Beginner

**Estimated Time:** 25–35 minutes

---

# Design Problem

So far, every object has moved because **we** told it to move.

The object had no choice.

It simply followed instructions.

Games become interesting when movement responds to something outside the object.

The most common source of that decision is:

> **The player.**

Responsive motion allows an object to change its behavior based on external input.

---

# Why This Technique Matters

This is one of the defining characteristics of interactive software.

Until now you have been creating animations.

Now you begin creating interaction.

The world no longer changes because time passes.

The world changes because someone makes a decision.

---

# Starter Implementation

Before beginning, configure the following Input Map actions:

```text
move_left
move_right
move_forward
move_backward
```

Now attach the following script to a **Node3D**.

```gdscript
extends Node3D

@export var speed := 5.0

func _process(delta):

	if Input.is_action_pressed("move_left"):
		position.x -= speed * delta

	if Input.is_action_pressed("move_right"):
		position.x += speed * delta

	if Input.is_action_pressed("move_forward"):
		position.z -= speed * delta

	if Input.is_action_pressed("move_backward"):
		position.z += speed * delta
```

Run the scene.

You should now be able to move the object using the configured input actions.

---

# Dissecting the Code

Unlike the previous technique, movement is no longer automatic.

Instead, every frame the script asks a question.

```gdscript
Input.is_action_pressed(...)
```

This asks:

> **"Is the player currently requesting this action?"**

If the answer is yes...

movement occurs.

If the answer is no...

nothing happens.

---

Notice that motion still occurs inside:

```gdscript
_process(delta)
```

The object is still updated every frame.

The difference is that movement now depends on player input.

---

# Design Principle

## Motion is often a conversation.

Instead of thinking:

> Move.

Think:

> Should I move?

Responsive systems constantly ask questions about the outside world.

Examples include:

* Is the player pressing a key?
* Is the mouse moving?
* Has a button been clicked?
* Has another object entered a trigger?

Interaction begins when an object starts responding rather than simply acting.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Double the speed.

```gdscript
speed = 10
```

How does the object feel?

---

### Experiment B

Reduce the speed.

```gdscript
speed = 1
```

How does that change the experience?

---

### Experiment C

Reverse one direction.

Example:

```gdscript
position.x +=
```

becomes

```gdscript
position.x -=
```

Predict what will happen.

Now test it.

---

### Experiment D

Disable one movement direction.

Comment out:

```gdscript
move_backward
```

How does limiting movement change the interaction?

---

### Experiment E

Remap the controls.

Without changing the code, change the Input Map.

For example:

```text
move_forward

↓

Up Arrow
```

Does the script still work?

Why?

---

# Practical Observation

Notice that the script never checks:

```gdscript
KEY_W
```

or

```gdscript
KEY_A
```

Instead it asks for:

```gdscript
move_forward
```

The code describes **intentions**, not keys.

This separation allows controls to change without rewriting the movement system.

---

# Challenge

Add one additional action.

Examples:

```text
move_up
```

or

```text
move_down
```

or

```text
boost
```

Implement it using the same pattern as the starter implementation.

Before running the scene, predict how the object will behave.

Then test your prediction.

---

# Reflection

Complete the sentence:

> Responsive motion differs from automatic motion because...

Now answer:

What part of the code is responsible for making the object "listen" to the player?

---

# Common Mistakes

### Using Keyboard Keys Directly

Prefer:

```gdscript
Input.is_action_pressed()
```

rather than checking specific keyboard keys.

This makes projects easier to maintain and supports multiple input devices.

---

### Forgetting Delta

Movement should almost always include:

```gdscript
* delta
```

to remain consistent across different frame rates.

---

### Forgetting the Input Map

If an action has not been created in the Project Settings, the script cannot respond to it.

Always verify that the Input Map and the code use the same action names.

---

### Changing Multiple Things At Once

During exploration, modify one variable at a time.

Observe.

Think.

Then continue.

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain why movement only occurs while an input is active?

✓ Can I add a new movement direction?

✓ Can I explain why Input Actions are better than checking keyboard keys directly?

✓ Can I predict how changing one line of movement code changes the behavior?

---

# Looking Ahead

In this technique, the player controlled the object's motion.

Next, we'll explore a different question:

> **What if the object decides how it should move?**

Many systems—including patrols, orbiting planets, rotating fans, and floating platforms—move continuously without any player input at all.

The underlying motion is the same.

Only the source of the decision changes.
