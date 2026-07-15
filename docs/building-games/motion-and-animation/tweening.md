# Technique 6.3 — Tweening

## Classification

**Type:** Motion Refinement Technique

**Category:** Motion Refinement

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Problem

In the previous technique, we created smooth motion by updating an object every frame.

That worked well.

But sometimes we don't actually want to manage the movement ourselves.

Instead, we'd like to tell Godot:

> **"Move this object over there."**

…and then let the engine handle the animation.

This is the purpose of **Tweens**.

---

# Why This Technique Matters

Tweening allows developers to describe **what** should happen instead of **how** it should happen every frame.

Instead of writing continuous update code, we define:

* where the object should go
* how long it should take
* what kind of easing should be used

Godot performs the animation automatically.

---

# Starter Implementation

Attach the following script to any **Node3D**.

```gdscript
extends Node3D

func _ready():

	var tween = create_tween()

	tween.tween_property(
		self,
		"position",
		Vector3(5, 0, 0),
		2.0
	)
```

Run the scene.

Observe.

The object smoothly moves to its destination.

Notice:

There is **no** `_process()` function.

---

# Dissecting the Code

The important line is:

```gdscript
var tween = create_tween()
```

This asks Godot to create an animation controller.

Next:

```gdscript
tween.tween_property(...)
```

describes the animation.

We provide:

* the object
* the property
* the destination
* the duration

Godot handles everything else.

---

Notice what is missing.

There is no:

```gdscript
position += ...
```

There is no:

```gdscript
position.lerp(...)
```

There is no frame-by-frame movement code.

The engine performs the interpolation for us.

---

# Design Principle

## Describe the destination, not every step.

There are two ways to animate.

### Continuous Control

Every frame you decide where the object should go.

---

### Tweening

You decide:

* where it begins
* where it ends
* how long it should take

The engine determines the intermediate positions.

Neither approach is universally better.

Each solves different design problems.

---

# Experiment

Modify only one thing at a time.

---

### Experiment A

Change the duration.

```gdscript
2.0

↓

0.5
```

Observe.

---

### Experiment B

Change the destination.

```gdscript
Vector3(5,0,0)

↓

Vector3(-5,3,-2)
```

Observe.

---

### Experiment C

Chain another tween.

```gdscript
tween.tween_property(
	self,
	"rotation",
	Vector3(0, PI, 0),
	1.5
)
```

Observe.

The object first moves.

Then rotates.

---

### Experiment D

Experiment with easing.

For example:

```gdscript
tween.set_trans(Tween.TRANS_SINE)
tween.set_ease(Tween.EASE_IN_OUT)
```

Observe.

How does the movement feel?

---

# Practical Applications

Tweens appear throughout games.

Examples include:

### Doors

Smoothly opening.

---

### Menus

Sliding onto the screen.

---

### Collectibles

Floating upward when collected.

---

### Cameras

Transitioning between viewpoints.

---

### UI

Buttons growing when hovered.

---

### Cutscenes

Objects moving between key positions.

---

# Common Misconceptions

### "Tweening replaces `_process()`."

No.

Tweens automate specific animations.

Continuous simulation still belongs inside `_process()`.

---

### "Tweens are only for movement."

Any property can often be tweened.

Examples include:

* rotation
* scale
* transparency
* color
* camera zoom

---

### "Tweening always looks the same."

Different easing functions produce dramatically different motion.

Choosing the easing curve is part of the design process.

---

### "Tweening is always better."

Not necessarily.

Objects that respond continuously to changing information often require `_process()` instead.

---

# Challenge

Create three identical cubes.

Cube A

Uses:

```gdscript
position = target
```

---

Cube B

Uses:

```gdscript
position.lerp(...)
```

---

Cube C

Uses:

```gdscript
Tween
```

Now compare them.

Discuss:

* Which required the least code?
* Which gave the greatest control?
* Which would you use for:

  * a door?
  * a camera?
  * a moving platform?
  * a menu animation?

Support your reasoning.

---

# Reflection

Complete the sentence:

> Tweening is useful because...

Now answer:

When would you choose a Tween instead of writing `_process()` code?

Can you think of situations where a Tween would actually make your code more difficult?

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain what a Tween automates?

✓ Can I distinguish between Tweening and interpolation?

✓ Can I change a Tween's duration?

✓ Can I explain why easing affects how motion feels?

---

# Looking Ahead

You now know three different ways to move an object.

| Technique      | Best For              |
| -------------- | --------------------- |
| Instant Motion | Immediate changes     |
| Interpolation  | Continuous adjustment |
| Tweening       | Planned animations    |

All three produce motion.

None is universally "correct."

One of the defining skills of a game developer is choosing the technique that best supports the player's experience.

In the final technique of this section, we'll step back from implementation and ask a broader question:

> **Why do some movements simply feel better than others?**

That question leads us into one of the most subjective—and most rewarding—aspects of game development: **Motion Feel**.
