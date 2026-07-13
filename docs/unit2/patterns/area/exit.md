# Pattern 2.11.2 — Exit an Area

## Classification

**Type:** Gameplay Pattern

**Category:** Area Detection

**Difficulty:** Beginner

**Prerequisites:**

- Area3D
- Signals

---

# Problem

Many gameplay systems need to know:

> **When did something leave this Area?**

Examples include:

- leaving a checkpoint
- exiting a safe zone
- stopping background music
- ending a dialogue region
- leaving a healing area
- escaping an enemy detection zone

Rather than continuously checking whether something is still inside, Area3D automatically emits a signal when an object exits its collision volume.

---

# Starter Implementation

Create an **Area3D** with a **CollisionShape3D**.

Connect:

```text
body_exited(body)
```

Attach the following script.

```gdscript
extends Area3D

func _on_body_exited(body):

	print(body.name)
	print("Object Left Area!")
```

Run the scene.

Walk into the Area.

Then walk back out.

Observe.

The signal only fires when the object leaves.

---

# How It Works

Area3D continuously monitors its collision volume.

Whenever a body exits:

```text
Body Leaves

↓

Area Detects Exit

↓

body_exited Signal

↓

Your Code Executes
```

Notice that your code never asks:

> "Is the player still here?"

The Area tells you automatically.

---

# Anatomy

## Area3D

Monitors overlap.

---

## body_exited(body)

Executes once whenever a body leaves the Area.

---

## body

Represents the object that exited.

Examples include:

- CharacterBody3D
- RigidBody3D
- AnimatableBody3D

---

# Experiment

Only change one thing.

---

### Experiment A

Print:

```gdscript
body.name
```

Observe.

---

### Experiment B

Walk into the Area.

Pause.

Walk out.

Observe.

When exactly does the signal occur?

---

### Experiment C

Roll a RigidBody into the Area.

Then roll it back out.

Observe.

Does the same signal fire?

---

### Experiment D

Create two Areas.

Walk through both.

Observe.

Can each Area independently detect when objects leave?

---

### Experiment E

Enter the Area several times.

Exit several times.

Observe.

Does every exit generate a signal?

---

# Practical Applications

Leaving an Area is often just as important as entering one.

Examples include:

- leaving a checkpoint
- exiting combat
- leaving a music region
- ending dialogue
- disabling hazards
- exiting a healing zone
- stopping particle effects

Many gameplay systems require both events.

---

# Common Uses

This pattern commonly represents:

- exiting safe zones
- ending cutscenes
- leaving trigger volumes
- ending tutorials
- resetting traps
- disabling environmental effects

Whenever gameplay changes because something **leaves** a region, this pattern is appropriate.

---

# Common Misconceptions

### "body_entered() tells me when the player leaves."

No.

Area3D provides separate signals for entering and leaving.

---

### "I should constantly check whether the player is inside."

Usually not.

The Area already provides dedicated entry and exit events.

---

### "Leaving an Area isn't important."

Many gameplay systems depend on knowing when an interaction has ended.

---

# Workbench Habit

Whenever gameplay has a clear:

> Begin

and

> End

look for both signals.

For Areas, these are usually:

```text
body_entered()

body_exited()
```

Together they describe the complete interaction.

---

# Challenge

Build a simple "safe zone."

When the player enters:

```
Safe
```

is printed.

When the player exits:

```
Danger
```

is printed.

Notice how two simple signals allow your game to understand whether the player is currently inside or outside a region.