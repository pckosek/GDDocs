---
tags: [technique, inventory]
---

# 6.5.2 Collectibles

## Classification

**Type:** Engineering Technique

**Category:** Gameplay Objects

**Difficulty:** Intermediate

**Estimated Time:** 25–35 minutes

---

# Design Problem

Imagine the player collects a coin.

What should happen?

Perhaps:

- increase the score
- play a sound
- play an animation
- remove the coin

Although this feels like one action...

...it is actually several gameplay systems working together.

Collectibles are one of the simplest examples of gameplay objects coordinating multiple systems.

---

# Why This Matters

Collectibles appear throughout games.

Examples include:

- coins
- gems
- keys
- health pickups
- power-ups
- ammunition

Although they provide different rewards...

...they often follow exactly the same gameplay pipeline.

Understanding that pipeline makes many later gameplay systems much easier to build.

---

# Starter Implementation

A typical collectible might look like this.

```text
Coin (Area2D)

├── CollisionShape2D
├── AnimatedSprite2D
└── AudioStreamPlayer2D
```

When something enters the area:

```gdscript
func _on_body_entered(body):

    if body.is_in_group("player"):

        GameManager.score += 1

        queue_free()
```

The collectible detects the player.

It updates the game.

Then it removes itself.

---

# Using Groups

Notice the check.

```gdscript
body.is_in_group("player")
```

Groups describe the role an object plays.

Rather than checking:

```gdscript
body.name == "Player"
```

or

```gdscript
body is Player
```

the collectible asks:

> **Is this object part of the Player group?**

Groups make gameplay systems more flexible and reusable.

---

# Dissecting the System

Notice how many systems participate.

```text
Player Enters Area

↓

Area2D Signal

↓

Group Check

↓

Update GameManager

↓

Play Feedback

↓

Remove Object
```

No single object performs every task.

Each system contributes one responsibility.

---

# Design Principle

## Gameplay objects should communicate with other systems.

Collectibles are not responsible for:

- storing the score
- updating the user interface
- managing player lives

Instead...

they communicate what happened.

Other systems respond.

Keeping responsibilities separate makes gameplay much easier to extend.

---

# Practical Observation

Many beginning programmers store the score inside the coin.

This works...

...until there are one hundred coins.

Instead...

the coin simply reports:

```text
Collected
```

The GameManager updates the score.

The UI updates automatically.

The gameplay object remains simple.

---

# A Common Bug

Suppose the collectible plays a sound.

```gdscript
$AudioStreamPlayer2D.play()

queue_free()
```

Nothing is heard.

Why?

Because the collectible is removed immediately.

Its AudioStreamPlayer2D disappears before the sound finishes playing.

This is not an audio problem.

It is an **object lifecycle** problem.

Objects often need to finish communicating before they are destroyed.

Possible solutions include:

- allowing another object to own the sound
- delaying `queue_free()`
- waiting until an animation or sound has finished

Understanding object lifecycles prevents many subtle gameplay bugs.

---

# Common Misconceptions

### "The collectible should update the score itself."

Usually not.

The collectible should communicate that it was collected.

The GameManager should own the score.

---

### "Checking the node name is enough."

Node names often change.

Groups describe the purpose of an object rather than its current name.

They make gameplay systems more reusable.

---

### "`queue_free()` should happen immediately."

Not always.

If the object still needs to:

- finish an animation
- finish a sound
- emit a signal

removing it immediately may interrupt those systems.

---

### "Collectibles are unique."

Not really.

Most collectibles follow the same interaction pattern.

Only the reward changes.

---

# Reflection

Imagine creating the following.

- coin
- key
- health pickup
- magic crystal
- extra life

What should each collectible:

- detect?
- communicate?
- update?
- play?
- remove?

Which systems should remain outside the collectible?

---

# Looking Back

Earlier we learned that Area2D detects interactions.

Now we've discovered what happens afterwards.

Gameplay objects often begin a chain of events involving:

- detection
- communication
- game state
- feedback
- object removal

The collectible itself remains surprisingly small.

Most of the work happens through cooperation between systems.

---

# Looking Ahead

Collectibles react to the player.

Enemies are more interesting.

They observe the player...

make decisions...

change state...

and react differently depending on the situation.

The next lesson explores:

> **Enemy States**