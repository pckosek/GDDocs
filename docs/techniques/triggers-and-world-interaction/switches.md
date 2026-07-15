---
tags: [technique, trigger]
---

# 8.3.4 Switches & Events

## Classification

**Type:** Engineering Technique

**Category:** Interaction

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Problem

Imagine the player steps onto a pressure plate.

Immediately...

a bridge lowers across the room.

The player never touched the bridge.

So why did it move?

The answer is that the pressure plate did not directly move the bridge.

Instead...

it announced that something had happened.

Other systems responded.

Adventure games are filled with these kinds of events.

---

# Why This Matters

Many gameplay objects exist to change the world.

Examples include:

- buttons
- pressure plates
- levers
- switches
- crystals
- floor triggers

Although they appear different...

...they often follow exactly the same pattern.

An event occurs.

The world responds.

---

# Mental Model

Think about a light switch.

Flipping the switch does not create light.

It changes the electrical circuit.

The light responds.

Games work similarly.

```text
Player Action

↓

Event

↓

World Changes
```

The switch begins the event.

Other systems decide how to respond.

---

# Starter Workflow

A typical interaction might follow this sequence.

```text
Player

↓

Pressure Plate

↓

Signal

↓

Bridge

↓

Lower
```

Or:

```text
Player

↓

Lever

↓

Signal

↓

Door

↓

Unlock
```

The objects remain independent.

They communicate through events.

---

# Dissecting the System

Notice the separation.

The switch does not know:

- how bridges work
- how doors open
- how traps activate

It simply announces:

```text
Activated
```

Other gameplay systems decide what that means.

```text
Switch

↓

Signal

↓

Interested Objects
```

This keeps every object focused on one responsibility.

---

# State Changes

Events often change world state.

For example:

```text
Lever

↓

Activated

↓

Bridge

↓

Lowered
```

The event is temporary.

The new state persists.

Future interactions now behave differently because the world has changed.

---

# Design Principle

## Trigger events.

Don't control the world directly.

Interactive objects should communicate that something happened.

Other systems decide how to respond.

This separation makes worlds much easier to expand and maintain.

---

# Practical Observation

Many adventure games build surprisingly complex puzzles from very small interactions.

Examples include:

- one switch opens several doors
- two pressure plates activate one bridge
- one key unlocks many different doors
- one puzzle changes multiple parts of the world

The complexity comes from connecting simple events rather than creating complicated individual objects.

---

# Common Misconceptions

### "The switch opens the door."

Usually not.

The switch emits an event.

The door chooses how to respond.

---

### "Every object needs to know about every other object."

Not at all.

Signals allow independent systems to communicate without becoming tightly connected.

---

### "Events disappear immediately."

The event is temporary.

The world state it creates may persist long afterwards.

---

### "Only puzzles use events."

Events appear throughout games.

Examples include:

- quests
- dialogue
- combat
- achievements
- checkpoints

Any meaningful change in the game often begins with an event.

---

# Reflection

Imagine creating a dungeon.

One lever should:

- lower a bridge
- disable spikes
- open a hidden passage

How would you organize these interactions?

Would the lever directly control every object?

Or would it simply announce:

```text
Activated
```

What advantages does that provide?

---

# Looking Back

Earlier we explored:

- interaction
- dialogue
- keys and doors

Now we've discovered another powerful idea.

The world does not change because objects directly control one another.

It changes because independent systems communicate through events.

Small interactions can now produce surprisingly large changes throughout the world.

---

# Looking Ahead

The world now responds to the player's actions.

The next challenge is giving players tools they can carry with them.

How can games allow players to:

- collect items
- store resources
- use objects later

We'll begin exploring:

> **Inventory**