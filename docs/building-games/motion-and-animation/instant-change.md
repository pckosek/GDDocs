# Technique 6.1 — Instant Motion

## Classification

**Type:** Motion Refinement Technique

**Category:** Motion Refinement

**Difficulty:** Beginner

**Estimated Time:** 15–20 minutes

---

# Design Problem

Not every movement should be visible.

Sometimes an object should travel smoothly across the world.

Other times...

it should simply appear somewhere else.

This is called **Instant Motion**.

The object does not travel between two positions.

Instead, its transform changes immediately.

---

# Why This Technique Matters

As developers, we often think:

> "Can I animate this?"

A more useful question is:

> **"Should the player experience this movement?"**

Sometimes the answer is yes.

Sometimes the answer is no.

Choosing between instant and animated motion is one of the first decisions that influences how a game feels.

---

# Starter Implementation

Attach the following script to any **Node3D**.

```gdscript id="h9dt2x"
extends Node3D

func _input(event):

	if event.is_action_pressed("ui_accept"):
		position = Vector3(5, 0, 0)
```

Run the scene.

Press **Space**.

Notice that the object does not travel.

It immediately appears in its new position.

---

Now try:

```gdscript id="0ksn0t"
extends Node3D

func _input(event):

	if event.is_action_pressed("ui_accept"):
		position = Vector3.ZERO
```

The object now instantly returns to the origin.

Again...

No travel.

Only a new position.

---

# Dissecting the Code

Notice the assignment:

```gdscript id="9zwnmf"
position =
```

There is no:

```gdscript id="zhw8qo"
+=
```

There is no:

```gdscript id="cjlwm2"
_process()
```

There is no interpolation.

We simply replace one transform with another.

The previous position no longer matters.

---

# Design Principle

## Motion communicates time.

Instant motion communicates:

> "The journey isn't important."

Smooth motion communicates:

> "Watch this happen."

Neither is inherently better.

The appropriate choice depends on what the player should experience.

---

# Experiment

Modify only one thing at a time.

---

### Experiment A

Change:

```gdscript id="jlwmr5"
Vector3(5,0,0)
```

to:

```gdscript id="jlwmr6"
Vector3(20,0,0)
```

Observe.

Does distance matter?

---

### Experiment B

Replace:

```gdscript id="jlwmr7"
position =
```

with:

```gdscript id="jlwmr8"
position +=
```

Press the key repeatedly.

How does the interaction change?

---

### Experiment C

Instead of changing:

```gdscript id="jlwmr9"
position
```

change:

```gdscript id="jlwmra"
rotation
```

What happens?

---

### Experiment D

Instead of using:

```gdscript id="jlwmrb"
ui_accept
```

trigger the reposition using:

* a Timer
* a Signal
* another Event

Notice that the motion itself does not change.

Only the event that causes it changes.

---

# Practical Applications

Instant Motion appears throughout games.

Examples include:

### Respawning

A player immediately returns to a checkpoint.

---

### Teleportation

Characters instantly change location.

---

### Procedural Generation

Objects are positioned before the player ever sees them.

---

### Scene Initialization

Objects begin in their starting locations.

---

### Resetting Objects

Training environments, puzzle games, and simulations frequently reposition objects instantly.

---

# Common Misconceptions

### "Instant motion is unrealistic."

Sometimes.

But realism is not always the goal.

Clarity and responsiveness are often more important.

---

### "Everything should move smoothly."

Many systems become frustrating if every action is animated.

Sometimes immediate feedback is the better design choice.

---

### "The object traveled."

No.

It simply occupies a different transform.

Travel and repositioning are different ideas.

---

# Challenge

Create two identical cubes.

Cube A

Moves instantly when Space is pressed.

Cube B

Moves continuously using `_process()`.

Observe the difference.

Now ask another student:

Which cube felt more responsive?

Which felt more believable?

Discuss why.

---

# Reflection

Complete the sentence:

> Instant motion is appropriate when...

Now answer:

Can you think of three games where teleportation or instant repositioning improves the experience?

Can you think of three where it would feel completely wrong?

---

# Self Check

Before moving on, ask yourself:

✓ Can I distinguish between repositioning and movement?

✓ Can I explain why instant motion is sometimes preferable?

✓ Can I identify situations where animation would actually reduce clarity?

✓ Can I recognize that motion quality is a design decision rather than a technical limitation?

---

# Looking Ahead

Instant motion is only one way to change an object's transform.

In the next technique, we'll begin asking a different question:

> **What if the object should travel between two positions?**

Rather than replacing one transform with another, we'll explore interpolation—the process of gradually approaching a destination over time.

That single idea will become one of the most useful tools for creating movement that feels smooth and natural.
