# 6.5.3 Enemy States

## Classification

**Type:** Engineering Technique

**Category:** Gameplay Objects

**Difficulty:** Intermediate

**Estimated Time:** 30–40 minutes

---

# Design Problem

Imagine an enemy standing in the level.

What should it do?

Perhaps:

- wait
- patrol
- chase the player
- attack
- die

Should all of these behaviors happen at the same time?

Probably not.

An enemy should perform one behavior at a time.

As the situation changes...

...its behavior changes.

This is exactly the kind of problem that **State Machines** were designed to solve.

---

# Why This Matters

Enemies are one of the first gameplay objects that must make decisions.

Different situations require different behaviors.

For example:

- waiting for the player
- following a patrol route
- noticing the player
- attacking
- reacting to damage

State Machines organize these behaviors into clear, manageable systems.

Instead of asking dozens of unrelated questions...

...the enemy asks one.

> **What state am I currently in?**

---

# Starter Implementation

Begin by defining the possible states.

```gdscript
enum State {
    IDLE,
    PATROL,
    ALERT,
    ATTACK,
    DEAD
}

var current_state = State.IDLE
```

Each physics frame:

```gdscript
match current_state:

    State.IDLE:
        idle()

    State.PATROL:
        patrol()

    State.ALERT:
        alert()

    State.ATTACK:
        attack()

    State.DEAD:
        dead()
```

Each behavior remains separate.

The state determines which one runs.

---

# Dissecting the System

Notice the flow.

```text
Gameplay

↓

Current Situation

↓

Choose State

↓

Perform Behavior
```

The enemy does not continuously evaluate every behavior.

Only the current state executes.

This makes behavior much easier to understand and extend.

---

# Example State Flow

One possible enemy might behave like this.

```text
Idle

↓

Player Detected

↓

Alert

↓

Player Close

↓

Attack

↓

Player Escapes

↓

Patrol

↓

Health Reaches Zero

↓

Dead
```

Different enemies may use different states.

The underlying system remains the same.

---

# Design Principle

## One state.

One responsibility.

Each state should describe one clear mode of behavior.

Rather than mixing patrol, attack, and death logic together...

...allow each state to focus on a single responsibility.

State changes become much easier to reason about.

---

# Practical Observation

Notice that enemies often combine many systems.

For example:

```text
Area2D

↓

Player Detection

↓

State Change

↓

Animation

↓

Movement

↓

Sound
```

The State Machine coordinates these systems.

It does not replace them.

Each system continues performing its own responsibility.

---

# Common Misconceptions

### "State Machines create enemy intelligence."

Not exactly.

They organize behavior.

The intelligence comes from the rules that determine when states change.

---

### "Every enemy needs the same states."

No.

Different enemies require different behaviors.

Some enemies may never patrol.

Others may never attack.

Choose states that match the gameplay.

---

### "States should constantly switch."

Usually not.

Enemies should remain in one state until something meaningful changes.

Frequent unnecessary transitions often make behavior difficult to understand.

---

### "Death is not a state."

It usually is.

Dead enemies often:

- stop moving
- stop attacking
- stop detecting the player
- play an animation

Treating death as another state keeps behavior organized.

---

# Reflection

Imagine creating the following enemies.

| Enemy | Possible States |
|--------|-----------------|
| Slime | |
| Skeleton | |
| Flying Bat | |
| Turret | |
| Boss | |

Would every enemy need:

- Patrol?
- Alert?
- Attack?
- Dead?

Why?

Now ask yourself:

Which behaviors belong inside a state...

...and which events should cause state changes?

---

# Looking Back

Earlier in this course we introduced State Machines as a way of organizing behavior.

Now we've applied that idea to one of the most common gameplay objects.

The enemy does not perform every behavior simultaneously.

Instead...

it responds to the current situation by changing state.

The same architectural idea now controls:

- gameplay
- animation
- enemy behavior

---

# Looking Ahead

Enemies can now decide **what** to do.

The next challenge is interacting with the player.

How can enemies:

- detect attacks?
- receive damage?
- lose health?
- knock the player back?

We'll begin exploring one of the most common gameplay systems in action games:

> **Damage Systems**