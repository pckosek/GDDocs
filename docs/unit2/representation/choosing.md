# Technique 2.1 — Choosing a Physical Representation

## Classification

**Type:** Design / Engineering Guide

**Category:** Physical Interaction

**Difficulty:** Beginner

**Estimated Time:** 10–15 minutes

---

# Design Problem

In Unit 1, nearly every object was simply a **Node3D** with a mesh.

Objects existed.

They moved.

They looked interesting.

But they did not truly interact.

In Unit 2, every interactive object begins with a new question:

> **What kind of physical object am I building?**

Choosing the correct body type is one of the first architectural decisions you make when building a game.

The answer determines:

* who controls movement
* how collisions are handled
* how other objects interact with it
* what programming techniques become available

---

# Why This Technique Matters

Many beginning developers think:

> "I need a collision."

Experienced developers usually think:

> "What behavior should this object have?"

Body types are not simply different nodes.

They represent different kinds of physical behavior.

Understanding those differences makes the rest of Unit 2 much easier to understand.

---

# Field Guide

When beginning a new object, start by asking:

> **What is this object supposed to do?**

| If I am building...             | Consider...          | Why?                                                       |
| ------------------------------- | -------------------- | ---------------------------------------------------------- |
| Wall, Floor, Ramp               | **StaticBody3D**     | It never moves.                                            |
| Elevator, Door, Moving Platform | **AnimatableBody3D** | Your script controls the movement.                         |
| Barrel, Ball, Crate             | **RigidBody3D**      | Physics controls the movement.                             |
| Player, NPC                     | **CharacterBody3D**  | Your script controls movement while respecting collisions. |
| Coin, Trigger, Checkpoint       | **Area3D**           | Detects overlap without physically blocking objects.       |

These are not absolute rules.

They are good starting points.

---

# Mental Model

Think about ownership.

Every physical object answers one question:

> **Who is responsible for moving me?**

| Owner                 | Typical Body Type                  |
| --------------------- | ---------------------------------- |
| Nobody                | StaticBody3D                       |
| My Script             | CharacterBody3D / AnimatableBody3D |
| The Physics Engine    | RigidBody3D                        |
| Nobody—I only observe | Area3D                             |

Thinking about ownership often makes the correct choice obvious.

---

# Design Principle

## Choose behavior first.

Choose implementation second.

Beginning developers often start by asking:

> Which node should I use?

A more productive question is:

> What behavior do I want?

The body type should emerge naturally from the design problem.

---

# Comparison

## StaticBody3D

Immovable.

Examples:

* walls
* floors
* buildings
* terrain

---

## AnimatableBody3D

Moves because **you** move it.

Examples:

* elevators
* moving platforms
* doors
* rotating obstacles

---

## RigidBody3D

Moves because the **physics engine** moves it.

Examples:

* barrels
* balls
* crates
* debris

---

## CharacterBody3D

Moves because your **gameplay code** moves it.

Examples:

* players
* enemies
* NPCs

The physics engine helps resolve collisions, but it does not decide where the character wants to go.

---

## Area3D

Usually does **not** physically block anything.

Instead, it watches.

Examples:

* checkpoints
* pickups
* finish lines
* damage zones
* interaction volumes

---

# Studio Exercise

For each object below, decide which body type you would choose.

Do **not** build anything yet.

Instead, explain your reasoning.

| Object                 | My Choice | Why? |
| ---------------------- | --------- | ---- |
| Castle Wall            |           |      |
| Soccer Ball            |           |      |
| Elevator               |           |      |
| Player                 |           |      |
| Treasure Chest Trigger |           |      |
| Rolling Boulder Trap   |           |      |
| Finish Line            |           |      |

Discuss your answers with another student.

Notice that some scenarios may have more than one reasonable solution.

---

# Common Misconceptions

### "Every object should be a RigidBody."

Most objects in a game are **not** simulated by physics.

Physics is expensive.

Use it when the simulation is valuable.

---

### "AnimatableBody3D is just a moving StaticBody."

Not quite.

It is specifically designed to move while interacting correctly with other physical bodies.

---

### "Area3D is another kind of collider."

Area3D detects interaction.

It usually does not physically stop movement.

---

### "CharacterBody3D is just a player node."

CharacterBody3D is useful for anything whose movement is primarily controlled by gameplay logic.

Players are only one example.

---

# Reflection

Complete the sentence:

> Before choosing a body type, I should first ask...

Now answer:

Why do you think Godot provides several different physical body types instead of one universal "physics object"?

---

# Self Check

Before moving on, ask yourself:

✓ Can I explain the purpose of each body type?

✓ Can I identify who owns the movement of each object?

✓ Can I choose an appropriate body type for a simple gameplay scenario?

✓ Can I explain my reasoning rather than simply memorizing node names?

---

# Looking Ahead

This guide provides the map.

The remaining techniques in this section will explore each body type individually.

For each one, you will learn:

* how to build it
* how it behaves
* when it is appropriate
* common mistakes
* practical design patterns

By the end of this unit, choosing a physical representation should become a design decision rather than a guessing game.
