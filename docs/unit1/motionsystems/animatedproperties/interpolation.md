# Technique 6.2 — Interpolation

## Classification

**Type:** Motion Refinement Technique

**Category:** Motion Refinement

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Problem

In the previous technique, objects changed instantly.

Sometimes that is exactly what we want.

Other times...

instant motion feels abrupt.

Players often expect objects to:

* slide
* ease
* drift
* accelerate
* smoothly approach a destination

Interpolation provides a way to move gradually rather than immediately.

---

# Why This Technique Matters

Many objects in games are not trying to reach a destination as quickly as possible.

Instead, they are trying to move in a way that feels:

* smooth
* natural
* responsive
* satisfying

Interpolation is one of the most common techniques for improving the quality of motion.

---

# Starter Implementation

Attach the following script to any **Node3D**.

```gdscript
extends Node3D

@export var speed := 3.0

var target := Vector3(5,0,0)

func _process(delta):

	position = position.lerp(target, speed * delta)
```

Run the scene.

Notice that the object does **not** immediately jump to the target.

Instead, it continuously approaches it.

---

Now modify:

```gdscript
target = Vector3(-5,0,0)
```

Observe.

The object smoothly changes direction.

---

# Dissecting the Code

Unlike:

```gdscript
position = target
```

which immediately replaces the position,

this line:

```gdscript
position = position.lerp(target, speed * delta)
```

asks a different question.

Instead of:

> "Where should I be?"

it asks:

> **"How much closer should I become?"**

Every frame the object moves only part of the remaining distance.

The closer it gets...

the smaller each movement becomes.

---

# Design Principle

## Motion can approach rather than arrive.

Interpolation rarely says:

> "Go here."

Instead it says:

> "Move a little closer."

That tiny change produces movement that often feels significantly more natural.

---

# Experiment

Modify one thing at a time.

---

### Experiment A

Change:

```gdscript
speed = 1
```

Observe.

---

### Experiment B

Change:

```gdscript
speed = 10
```

Observe.

How does the motion feel?

---

### Experiment C

Replace:

```gdscript
position.lerp(...)
```

with:

```gdscript
position = target
```

Run the scene.

Compare the two.

Which feels better?

Why?

---

### Experiment D

Move the target while the object is still traveling.

Observe.

Notice that the object naturally redirects itself toward the new destination.

---

# Practical Applications

Interpolation appears throughout games.

Examples include:

### Cameras

Smoothly following the player.

---

### User Interface

Menus sliding into view.

---

### Doors

Opening naturally.

---

### Floating Platforms

Moving between destinations.

---

### Enemy AI

Smooth steering toward a target.

---

### Health Bars

Gradually updating rather than changing instantly.

---

# Common Misconceptions

### "Interpolation means constant speed."

Not necessarily.

Lerp moves a percentage of the remaining distance.

The object naturally slows as it approaches the target.

---

### "Interpolation replaces motion."

No.

Interpolation changes **how** motion occurs.

---

### "Interpolation is only for movement."

Any continuously changing value can often be interpolated.

Examples include:

* rotation
* scale
* color
* transparency
* camera zoom

---

### "Faster is always better."

Often the opposite.

Motion that is slightly slower frequently feels smoother and more deliberate.

---

# Challenge

Create three cubes.

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
position.move_toward(...)
```

Observe all three.

Discuss:

* Which feels most responsive?
* Which feels most natural?
* Which would you choose for:

  * a camera?
  * a teleport?
  * a sliding door?

Support your reasoning.

---

# Reflection

Complete the sentence:

> Interpolation changes...

Now answer:

Why might a game intentionally avoid instant movement?

Can you think of situations where interpolation would actually make the game feel worse?

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain what interpolation accomplishes?

✓ Can I distinguish between arriving immediately and approaching gradually?

✓ Can I adjust interpolation speed intentionally?

✓ Can I choose between instant motion and interpolation based on player experience?

---

# Looking Ahead

Interpolation gives us one way to create smooth movement.

But we are still manually updating the object every frame.

In the next technique, we'll explore **Tweens**.

Rather than writing the update loop ourselves, we'll ask Godot to animate a property for us.

The destination may be the same.

The workflow becomes very different.
