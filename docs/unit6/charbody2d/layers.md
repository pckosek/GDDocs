# 6.1.6 Collision Layers

## Classification

**Type:** Engineering Technique

**Category:** 2D Character Movement

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine a platformer containing:

- the player
- enemies
- coins
- platforms
- projectiles
- hazards

Should every object collide with every other object?

Probably not.

For example:

- Coins should be collected, not block movement.
- Bullets may hit enemies but pass through the player.
- Players should stand on platforms but ignore background decorations.

The engine needs a way to decide which objects should interact.

Godot solves this using **Collision Layers** and **Collision Masks**.

---

# Why This Matters

Collision Layers allow us to organize objects into categories.

Collision Masks determine which categories an object will detect or collide with.

Together, they answer two questions.

> **Which group am I in?**

and

> **Which groups do I care about?**

This makes collision systems flexible and much easier to manage.

---

# Starter Implementation

Suppose we create the following layers.

```text
Layer 1
Player

Layer 2
World

Layer 3
Enemies

Layer 4
Collectibles
```

Now configure the player.

```text
Collision Layer

Player

Collision Mask

World
Enemies
Collectibles
```

The player belongs to the **Player** layer.

The player checks collisions against the **World**, **Enemies**, and **Collectibles** layers.

---

A collectible might instead use:

```text
Collision Layer

Collectibles

Collision Mask

Player
```

Coins do not need to detect walls.

They only need to detect the player.

---

# Dissecting the System

Think of every object wearing a badge.

```text
"I am a Player."
```

That badge is the **Collision Layer**.

Now imagine the object also carries a checklist.

```text
I care about:

✓ World

✓ Enemies

✓ Collectibles
```

That checklist is the **Collision Mask**.

One identifies the object.

The other determines what it interacts with.

---

# Design Principle

## Separate identity from interaction.

Collision Layers describe **what an object is**.

Collision Masks describe **what the object responds to**.

Keeping these responsibilities separate produces collision systems that are easy to understand and extend.

---

# Example

Suppose we have these objects.

| Object | Layer | Mask |
|----------|-------|------|
| Player | Player | World, Enemies, Collectibles |
| Coin | Collectible | Player |
| Enemy | Enemy | World, Player |
| Platform | World | Player, Enemy |

Notice that not every object needs to interact with every other object.

Each object responds only to the relationships that matter.

---

# Practical Observation

Beginning programmers often leave every object on the same collision layer.

The result is usually unnecessary collisions and confusing behavior.

As projects grow...

carefully organizing collision layers becomes increasingly important.

Good layer design often prevents bugs before they occur.

Many teams establish their collision layers early in development and use them consistently throughout the project.

---

# Common Misconceptions

### "Collision Layers move objects."

No.

They only determine which objects may interact.

Movement is still controlled by your scripts and movement functions.

---

### "Every object should collide with everything."

Usually not.

Most objects interact with only a small subset of the world.

Collision Masks allow us to express those relationships clearly.

---

### "Collision Layer and Collision Mask are the same thing."

No.

The **Layer** answers:

> "What am I?"

The **Mask** answers:

> "Who do I pay attention to?"

These are different responsibilities.

---

### "Changing collision layers changes the object's behavior."

Not directly.

Changing layers changes which interactions are possible.

Your scripts still determine what happens after those interactions occur.

---

# Reflection

Imagine your platformer contains:

- Player
- Enemy
- Coin
- Bullet
- Platform
- Spikes

Which collision relationships should exist?

Which should not?

Can you explain why?

Now ask yourself:

Would adding more collision layers make your project easier to understand?

Or unnecessarily complicated?

---

# Looking Back

Our CharacterBody2D now has everything it needs to become a playable character.

We learned:

- why CharacterBody2D exists
- how velocity describes movement
- how gravity changes velocity
- how `move_and_slide()` performs movement
- when `move_and_collide()` is appropriate
- how Collision Layers organize interactions

Together, these ideas form the foundation of nearly every 2D platformer.

---

# Looking Ahead

Our character can now move safely through the world.

The next challenge is making that movement enjoyable.

How do we design jumping that feels responsive and satisfying?

We'll begin by exploring one of the defining mechanics of platform games:

> **The Jump.**