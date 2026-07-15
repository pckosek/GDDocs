# 8.1.6 Collision & Interaction

## Classification

**Type:** Engineering Technique

**Category:** Overworld

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine walking through an overworld.

The player reaches:

- a wall
- a tree
- a lake
- a movable block
- a closed door

Should every object behave the same way?

Of course not.

Some objects stop movement.

Some can be pushed.

Some begin conversations.

Some require keys.

In overworld games...

collision becomes much more than simply preventing movement.

It becomes interaction.

---

# Why This Matters

Collision helps define how players understand the world.

Different objects communicate different rules.

Examples include:

| Object | Typical Behaviour |
|----------|-------------------|
| Wall | Stop movement |
| Tree | Block movement |
| Water | Slow, block, or require an ability |
| Push Block | Move when pushed |
| NPC | Begin dialogue |
| Door | Open or remain locked |

Collision becomes one way the world communicates its rules.

---

# Mental Model

Think about walking through your school.

A wall tells you:

> You cannot go here.

A door tells you:

> You may pass.

A chair suggests:

> You might sit here.

Objects communicate through their behaviour.

Games work the same way.

```text
Player

↓

Object

↓

Response
```

Every collision becomes a conversation between the player and the world.

---

# Common Types of Interaction

Not every collision should produce the same result.

```text
Wall

↓

Stop
```

---

```text
Water

↓

Require Ability

or

Slow Movement
```

---

```text
Push Block

↓

Move Object
```

---

```text
NPC

↓

Dialogue
```

Although each interaction begins with collision...

the response depends on the object.

---

# Dissecting the System

Notice what changed from the platformer.

Earlier:

```text
Collision

↓

Movement Stops
```

Now:

```text
Collision

↓

Gameplay Decision
```

The collision becomes the beginning of an interaction rather than its conclusion.

The world starts responding.

---

# Design Principle

## Different objects teach different rules.

Players gradually learn what each object means.

Walls teach:

> You cannot pass.

Water teaches:

> You may need another solution.

Push blocks teach:

> Experiment.

NPCs teach:

> Interact.

Every object communicates part of the world's language.

---

# Practical Observation

Many beginning games give every obstacle identical behaviour.

Everything simply blocks movement.

More interesting overworlds allow different objects to create different kinds of interactions.

Examples include:

- pushing
- activating
- collecting
- unlocking
- speaking
- examining

The world becomes more expressive because different objects behave differently.

---

# Common Misconceptions

### "Collision always stops movement."

Not necessarily.

Some collisions begin interactions instead.

The response depends on the object involved.

---

### "Every solid object behaves the same."

Good level design teaches players that different objects follow different rules.

Recognizing those rules becomes part of exploration.

---

### "Interaction requires dialogue."

Many interactions involve no text at all.

Examples include:

- pushing blocks
- opening doors
- activating switches
- collecting items

Interaction simply means the world responds.

---

### "Collision belongs only to physics."

Collision is often the beginning of gameplay.

Physics determines that two objects met.

Game design determines what happens next.

---

# Reflection

Imagine exploring a dungeon.

How should the player interact with:

- a wall?
- a tree?
- water?
- a movable block?
- a locked door?

Should every object respond immediately?

Or should some require:

- items?
- abilities?
- puzzle solving?

How does each interaction teach the player something about the world?

---

# Looking Back

Earlier we explored:

- movement
- grid movement
- interpolation
- facing direction

Now we've reached another important idea.

Movement exists so the player can interact with the world.

Collision is no longer simply about stopping.

It becomes the beginning of gameplay.

The world responds differently depending on what the player discovers.

---

# Unit Reflection

Throughout this chapter we've transformed movement.

Platformers emphasized:

- gravity
- momentum
- precision

Overworld games emphasize:

- exploration
- positioning
- interaction

The player no longer asks:

> **Can I make that jump?**

Instead they begin asking:

> **What happens if I explore here?**

Movement becomes the foundation for discovery.

The world becomes something to understand rather than simply overcome.

---

# Looking Ahead

Movement and interaction now allow players to explore the overworld.

The next challenge is making the world respond intelligently.

How do we build:

- doors
- switches
- dialogue
- inventories
- quests

that allow the world to change as the player progresses?

We'll begin exploring:

> **Interaction Systems**