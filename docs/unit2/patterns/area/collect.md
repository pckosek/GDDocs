# Pattern 2.11.3 — Collect an Item

## Classification

**Type:** Gameplay Pattern

**Category:** Area Detection

**Difficulty:** Beginner

**Prerequisites:**

- Area3D
- body_entered()
- CharacterBody3D

---

# Problem

Many games contain collectible objects.

Examples include:

- coins
- gems
- keys
- health packs
- ammunition
- power-ups

When the player reaches the object, it should:

- detect the player
- perform some gameplay action
- disappear

This pattern forms the basis of nearly every collectible system.

---

# Starter Implementation

Create the following hierarchy.

```text
Coin (Area3D)
├── CollisionShape3D
└── MeshInstance3D
```

Connect:

```text
body_entered(body)
```

Attach the following script.

```gdscript
extends Area3D

func _on_body_entered(body):

	if body is CharacterBody3D:

		print("Collected!")

		queue_free()
```

Run the scene.

Walk through the coin.

Observe.

The player passes through it.

The message appears.

The coin disappears.

---

# How It Works

```text
Player Enters

↓

Area Detects

↓

Signal Fires

↓

Gameplay Logic

↓

Coin Removed
```

The player never "collects" the coin directly.

The Area detects the player.

The Area decides what happens next.

---

# Anatomy

## Area3D

Detects the player.

---

## CollisionShape3D

Defines the pickup volume.

---

## MeshInstance3D

Provides the visible object.

---

## queue_free()

Removes the collected object from the scene.

---

# Design Principle

## Collectibles are events.

A collectible usually exists in one of two states.

```text
Available

↓

Collected

↓

Removed
```

The Area exists only to detect the moment of transition.

---

# Experiment

Only change one thing.

---

### Experiment A

Comment out:

```gdscript
queue_free()
```

Observe.

Can the coin be collected repeatedly?

---

### Experiment B

Replace:

```gdscript
print("Collected!")
```

with:

```gdscript
print(body.name)
```

Observe.

Who actually collected the item?

---

### Experiment C

Resize the CollisionShape3D.

Observe.

How forgiving does the collection become?

---

### Experiment D

Duplicate the coin.

Collect several in succession.

Observe.

Each Area operates independently.

---

### Experiment E

Replace:

```gdscript
queue_free()
```

with:

```gdscript
visible = false
```

Observe.

How does hiding differ from deleting?

---

# Practical Applications

This pattern appears throughout games.

Examples include:

- coins
- gems
- health packs
- ammunition
- keys
- puzzle pieces
- experience orbs
- collectibles

Many gameplay systems begin with this exact interaction.

---

# Common Misconceptions

### "The player collects the coin."

Not exactly.

The Area detects the player.

The Area removes itself.

---

### "queue_free() only hides the object."

No.

It removes the node from the Scene Tree.

The object no longer exists.

---

### "Collectibles must collide."

Usually not.

Players typically move directly through collectibles.

Area3D is designed for this style of interaction.

---

# Workbench Habit

Most collectible systems follow the same sequence.

```text
Detect

↓

Respond

↓

Remove
```

Later, you may also:

- increase score
- play a sound
- spawn particles
- update the HUD

But the core interaction usually remains the same.

---

# Challenge

Create three collectible objects.

When the player collects each one:

- print a different message
- remove the object

Then ask yourself:

How could this pattern become:

- a key?
- a health pickup?
- a power-up?

Notice that only the gameplay response changes.

The collection pattern remains almost identical.