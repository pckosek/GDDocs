# 6.2.6 One-Way Platforms

## Classification

**Type:** Engineering Technique

**Category:** Platforming

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Until now, every platform in our game has behaved the same way.

The player:

- lands on it
- walks across it
- collides with it from every direction

But many platform games include platforms that behave differently.

The player should be able to:

- jump upward through the platform
- land safely on top of it
- walk across it normally

The platform behaves differently depending on **which direction the player approaches from**.

These are called **One-Way Platforms**.

---

# Why This Matters

One-way platforms allow designers to build more interesting levels.

Examples include:

- floating platforms
- moving lifts
- drop-through platforms
- branching paths
- layered environments

They allow players to revisit lower areas without becoming trapped, while creating movement possibilities that solid platforms cannot provide.

---

# Mental Model

Imagine a trapdoor.

From below...

```text
Jump

↓

Pass Through
```

From above...

```text
Fall

↓

Stand On
```

The platform has not changed.

The player's relationship to it has.

The same object behaves differently depending on the direction of movement.

---

# Starter Implementation

Godot provides built-in support for one-way collisions.

Select the platform's:

```text
CollisionShape2D
```

Enable:

```text
One Way Collision
```

Now the platform allows movement upward through the collision shape...

while still supporting the player from above.

No additional movement code is required.

---

# Dissecting the Behavior

Notice that the platform itself is not deciding.

Instead...

the physics engine considers the direction of movement.

```text
Player Moving Up

↓

Ignore Collision

-------------------

Player Moving Down

↓

Resolve Collision
```

The interaction changes.

The object remains the same.

---

# Design Principle

## Behavior often depends on context.

Many gameplay systems are not simply:

```text
Always

or

Never
```

Instead they ask:

> **Under what conditions should this behavior occur?**

One-way platforms are one example of context-sensitive behavior.

The same object responds differently depending on the situation.

---

# Practical Observation

One-way platforms greatly influence level design.

They make it possible to create:

- stacked pathways
- secret areas
- vertical exploration
- forgiving platform layouts

Without them...

many platform levels become much more restrictive.

Good level designers think carefully about where one-way platforms improve player movement.

---

# Common Misconceptions

### "One-way platforms are not solid."

They are.

They simply become solid only under the appropriate conditions.

---

### "The player ignores the platform."

Only while approaching from below.

Once above the platform...

normal collisions occur.

---

### "One-way platforms require special movement code."

Usually not.

Godot's built-in one-way collision system handles the physics.

Your movement code often remains unchanged.

---

### "Every platform should be one-way."

Not at all.

One-way platforms are a level design tool.

Using them everywhere often removes interesting movement challenges.

---

# Reflection

Imagine designing a platformer level.

Where would one-way platforms improve the experience?

Would you place them:

- beneath difficult jumps?
- between multiple routes?
- on moving platforms?
- near collectibles?

Now ask yourself:

When should a platform behave differently depending on how the player approaches it?

---

# Looking Back

This section explored the foundations of platform movement.

We learned how to:

- jump
- control jump height
- improve responsiveness with Coyote Time
- remember player input with Jump Buffering
- move naturally across slopes
- create context-sensitive platforms

Together, these techniques transform a character that simply moves...

...into one that feels responsive, forgiving, and enjoyable to control.

The difference between a functional platformer and a satisfying platformer is often found in these small design decisions.

---

# Looking Ahead

Our player can now move confidently through the world.

The next challenge is bringing that world to life.

How do we represent the player visually?

How do we animate movement, jumping, and idle states?

We'll begin by exploring one of the most recognizable parts of every 2D game:

> **Sprites and Animation.**