# 6.3.4 State-Driven Animation

## Classification

**Type:** Engineering Technique

**Category:** Visual Representation

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Problem

Our player can now:

- move
- jump
- fall

Our sprite can now:

- play animations
- change appearance

How do we decide **which animation should play?**

One possibility is to check the keyboard.

```gdscript
if Input.is_action_pressed("left"):
    sprite.play("walk")
```

This works...

...until the game becomes more complicated.

What if:

- an enemy controls the character?
- the player is knocked back?
- a cutscene begins?
- movement is disabled?

Animations should not respond directly to input.

They should respond to **gameplay**.

---

# Why This Matters

The player sees animations.

The game understands states.

If those two systems become disconnected...

...the character quickly begins looking incorrect.

Examples include:

- running while standing still
- walking during a jump
- attacking while playing the idle animation

Instead of asking:

> **What button is being pressed?**

we should ask:

> **What is the player currently doing?**

---

# Starter Implementation

Suppose our player already has a state machine.

```gdscript
enum State {
    IDLE,
    WALK,
    JUMP,
    FALL
}
```

Now choose the animation using the current state.

```gdscript
match current_state:

    State.IDLE:
        sprite.play("idle")

    State.WALK:
        sprite.play("walk")

    State.JUMP:
        sprite.play("jump")

    State.FALL:
        sprite.play("fall")
```

The animation now reflects gameplay.

Not keyboard input.

---

# Dissecting the Code

Notice the flow.

```text
Player Input

↓

Movement

↓

State Changes

↓

Animation Changes
```

Animation is no longer making decisions.

It simply visualizes decisions that have already been made.

The gameplay remains the source of truth.

---

# Design Principle

## Gameplay drives animation.

Animation should communicate what the game already knows.

It should not determine what the game does.

The gameplay state remains authoritative.

The animation represents that state visually.

---

# Mental Model

Think of a stage actor.

The script determines:

- whether the character is running
- jumping
- falling

The costume and body language communicate that information to the audience.

Animation works the same way.

```text
Gameplay State

↓

Animation

↓

Player Understanding
```

The animation tells the player what the game already knows.

---

# Practical Observation

One of the easiest ways to recognize growing projects is this.

Beginning projects often ask:

```text
What key is being pressed?
```

Larger projects ask:

```text
What state is the object in?
```

Once animations become state-driven...

many other systems naturally become easier to manage as well.

Enemies.

NPCs.

Doors.

Collectibles.

The same pattern appears repeatedly.

---

# Common Misconceptions

### "Animations control gameplay."

Usually not.

Gameplay determines the current state.

Animations visualize that state.

---

### "The keyboard should choose the animation."

Not directly.

Input changes gameplay.

Gameplay changes state.

State changes animation.

Keeping these responsibilities separate produces more reliable systems.

---

### "Every state needs an animation."

Not necessarily.

Some states may intentionally reuse the same animation.

The important idea is that animations communicate gameplay clearly.

---

### "Animation is only cosmetic."

Not at all.

Animations communicate information to the player.

A good animation helps players understand what is happening before they consciously think about it.

---

# Reflection

Imagine the following player states.

| State | Animation |
|--------|-----------|
| Idle | |
| Walk | |
| Jump | |
| Fall | |
| Attack | |
| Hurt | |

Now ask yourself:

If the player stopped using a keyboard entirely...

would your animations still work?

Why?

---

# Looking Back

Earlier in the course we introduced **State Machines**.

At the time...

they organized gameplay.

Now we've discovered something more.

The same state machine also organizes animation.

Instead of checking many different conditions...

the sprite simply visualizes the player's current state.

One representation.

Two different systems.

---

# Looking Ahead

Animations help communicate what the player is doing.

Sometimes, however, the artwork itself must change direction.

Should the character have separate artwork for:

- left
- right

Or is there a simpler solution?

The next lesson explores one of the simplest and most useful animation techniques in 2D games:

> **Sprite Orientation**