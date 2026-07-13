# 8.1.4 Tweening

## Classification

**Type:** Engineering Technique

**Category:** Overworld

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine opening a treasure chest.

One possibility is:

```text
Closed

↓

Open
```

Instantly.

Another possibility is:

```text
Closed

↓

Opening...

↓

Open
```

The gameplay is identical.

The presentation feels completely different.

How can we smoothly change values over time?

This process is called **Interpolation**.

One common way to perform interpolation in Godot is with a **Tween**.

---

# Why This Matters

Interpolation appears throughout games.

Examples include:

- movement
- rotation
- fading
- scaling
- camera motion
- user interface animation
- doors
- collectibles

Rather than instantly changing a value...

...we gradually change it over time.

The result often feels smoother, more natural, and more polished.

---

# Mental Model

Think about a sunrise.

The sky does not instantly change from night to day.

It changes gradually.

Games often work the same way.

```text
Start Value

↓

Interpolation

↓

End Value
```

The beginning and ending are already known.

Interpolation controls the journey between them.

---

# Starter Implementation

Suppose we want to move an object.

```gdscript
var tween = create_tween()

tween.tween_property(
    self,
    "position",
    target_position,
    0.25
)
```

The object gradually moves toward its destination.

Notice that the gameplay already knows where the object should end.

The Tween simply controls **how** it gets there.

---

# Common Uses

Interpolation can affect almost any property.

### Move

```text
Position A

↓

Position B
```

---

### Rotate

```text
0°

↓

90°
```

---

### Fade

```text
Opacity 1.0

↓

Opacity 0.0
```

---

### Scale

```text
100%

↓

150%
```

Although these appear different...

they all follow the same idea.

A value changes smoothly over time.

---

# Dissecting the Idea

Notice what Tweening does **not** change.

```text
Gameplay Decision
```

The gameplay already knows:

- where the object belongs
- what rotation it should reach
- what opacity it should have

Tweening changes only:

```text
Presentation
```

It interpolates between two known values.

---

# Design Principle

## Separate state from transition.

Games often know both:

- the current state
- the desired state

Interpolation defines how the object moves between those states.

Keeping these responsibilities separate creates systems that are both easier to understand and easier to reuse.

---

# Practical Observation

Many beginning projects instantly update values.

```gdscript
position = target_position
```

As projects become more polished...

interpolation begins appearing everywhere.

Examples include:

- opening doors
- moving cameras
- collecting items
- fading menus
- scaling buttons
- sliding dialogue boxes

The underlying gameplay rarely changes.

Only the player's experience becomes smoother.

---

# Common Misconceptions

### "Tweening is only for movement."

Not at all.

Almost any numerical property can be interpolated.

Examples include:

- position
- rotation
- scale
- transparency
- colors
- camera zoom

---

### "Tweening changes gameplay."

Usually not.

The gameplay determines the destination.

The Tween controls the presentation.

---

### "Every change should be animated."

No.

Some gameplay requires immediate feedback.

Good designers choose interpolation where it improves clarity or feel rather than applying it everywhere.

---

### "Tweening replaces AnimationPlayer."

Not exactly.

AnimationPlayer often coordinates many properties together.

Tweening is excellent for creating simple, programmatically controlled transitions.

Both are useful.

---

# Reflection

Think about your own games.

Which of these currently happen instantly?

- opening a door
- collecting a coin
- camera movement
- menu transitions
- scaling a button

Would interpolation improve the experience?

Why?

---

# Looking Back

Earlier we used Tweening to create smooth grid movement.

Now we've discovered something much larger.

Movement was only one example.

Interpolation appears throughout game development.

The same idea supports:

- movement
- rotation
- fading
- scaling
- interface design

Tweening is not a movement tool.

It is a way of smoothly changing values over time.

---

# Looking Ahead

Movement is no longer our only concern.

The player also needs to communicate direction.

When standing still...

which way should they face?

How should movement, interaction, and animation work together?

The next lesson explores:

> **Facing Direction**