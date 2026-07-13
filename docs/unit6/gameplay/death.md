# 6.5.5 Death & Destruction

## Classification

**Type:** Engineering Technique

**Category:** Gameplay Objects

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Problem

Suppose an enemy's health reaches zero.

Should the enemy disappear immediately?

Perhaps not.

Before the enemy is removed...

the game may need to:

- play a death animation
- play a sound effect
- award points
- notify the GameManager
- spawn particles
- drop an item

If we remove the object too early...

none of these systems have time to finish.

Destroying gameplay objects is often more complicated than simply calling:

```gdscript
queue_free()
```

---

# Why This Matters

Gameplay objects often communicate with many different systems.

For example:

- animation
- audio
- particles
- score
- achievements
- enemy counters
- level progression

Those systems frequently need time to respond before the object disappears.

Understanding an object's lifecycle prevents many subtle bugs.

---

# Mental Model

Think about a stage performance.

When an actor finishes a scene...

they do not instantly disappear.

They:

- deliver the final line
- receive the audience's attention
- leave the stage

Only then is the scene complete.

Gameplay objects work similarly.

```text
Alive

↓

Defeated

↓

Communicate

↓

Cleanup

↓

Removed
```

Removal is the final step.

Not the first.

---

# Starter Implementation

A beginner might write:

```gdscript
func die():

    queue_free()
```

This certainly removes the object.

Unfortunately...

any animation or sound that belonged to the object also disappears immediately.

A better approach is:

```gdscript
func die():

    $AnimatedSprite2D.play("death")

    await $AnimatedSprite2D.animation_finished

    queue_free()
```

Now the animation completes before the object is removed.

---

Likewise, sounds may need to finish before cleanup occurs.

Sometimes this means:

- delaying `queue_free()`
- playing sounds from another object
- using a dedicated audio manager

The important idea is that gameplay systems are allowed to finish their work.

---

# Dissecting the Lifecycle

Notice the sequence.

```text
Health

↓

Zero

↓

Dead State

↓

Animation

↓

Sound

↓

Signal

↓

queue_free()
```

The object continues participating in the game for a short time.

Only after completing its responsibilities is it removed.

---

# Design Principle

## Cleanup should happen last.

Gameplay objects often have important work to complete before they disappear.

Removing an object too early interrupts the systems that depend on it.

Allow the object to finish communicating before cleaning it up.

---

# Practical Observation

One of the most common beginner bugs looks like this.

```gdscript
$AudioStreamPlayer2D.play()

queue_free()
```

No sound plays.

The audio player belonged to the object.

Removing the object immediately also removed the sound.

The problem is not the AudioStreamPlayer.

The problem is the object's lifecycle.

Thinking in terms of lifecycles often makes these bugs much easier to understand.

---

# Common Misconceptions

### "`queue_free()` should happen immediately."

Not always.

Objects often need to:

- finish animations
- finish sounds
- emit signals
- update other systems

before they are removed.

---

### "Dead objects should continue behaving normally."

Usually not.

Many games introduce a dedicated:

```text
Dead
```

state.

The object stops participating in gameplay while finishing its remaining responsibilities.

---

### "Animations control destruction."

Not exactly.

Animations communicate destruction.

Gameplay still decides **when** the object has died.

---

### "The sound system is broken."

Often it is not.

If the sound belongs to an object that has already been removed...

there is nothing left to continue playing.

---

# Reflection

Imagine an enemy dies.

In what order should these events happen?

| Step | Order |
|------|-------|
| Lose Health | |
| Enter Dead State | |
| Play Animation | |
| Play Sound | |
| Update GameManager | |
| Remove Object | |

Can you explain why that order matters?

---

# Looking Back

Earlier we learned that gameplay objects detect interactions, receive damage, and change state.

Now we've discovered that those objects also have lifecycles.

Birth.

Interaction.

Communication.

Cleanup.

Removal.

Thinking about objects as lifecycles rather than isolated scripts often produces much more reliable gameplay systems.

---

# Looking Ahead

Enemies.

Collectibles.

Projectiles.

Hazards.

Although they appear different...

they all communicate with the rest of the game.

The final lesson explores how these independent gameplay objects become part of one larger system through:

> **Signals and the GameManager**