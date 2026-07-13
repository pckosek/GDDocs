# Pattern 2.11.6 — Start a Dialogue

## Classification

**Type:** Gameplay Pattern

**Category:** Area Detection

**Difficulty:** Beginner

**Prerequisites:**

- Area3D
- Signals
- CharacterBody3D

---

# Problem

Many games communicate with the player through dialogue.

Examples include:

- NPC conversations
- tutorial prompts
- warning messages
- story narration
- signposts
- quest updates

Often, dialogue should begin automatically when the player reaches a particular location.

Area3D provides a simple way to trigger these interactions.

---

# Starter Implementation

Create the following hierarchy.

```text
DialogueTrigger (Area3D)
├── CollisionShape3D
└── MeshInstance3D (Optional)
```

Attach the following script.

```gdscript
extends Area3D

@export_multiline var dialogue := "Welcome to the village!"

func _on_body_entered(body):

	if body is CharacterBody3D:

		print(dialogue)
```

Run the scene.

Walk into the Area.

Observe.

The message appears immediately.

---

# How It Works

```text
Player Enters

↓

Area Detects

↓

Signal Fires

↓

Dialogue Begins
```

Notice that the Area does **not** display dialogue itself.

It simply decides **when** dialogue should begin.

---

# Anatomy

## Area3D

Detects the player's presence.

---

## body_entered()

Starts the interaction.

---

## dialogue

Stores the message associated with this trigger.

Different Areas can display different dialogue.

---

# Design Principle

## Gameplay decides timing.

Presentation decides appearance.

The Area determines:

> **When should the dialogue begin?**

Another system determines:

> **How should the dialogue appear?**

Keeping these responsibilities separate makes projects much easier to expand later.

---

# Experiment

Only change one thing.

---

### Experiment A

Change:

```gdscript
dialogue
```

to a different message.

Observe.

---

### Experiment B

Duplicate the trigger.

Give each Area a different message.

Walk through both.

Observe.

---

### Experiment C

Move the trigger.

Observe.

How does changing its location affect the player's experience?

---

### Experiment D

Resize the CollisionShape3D.

Observe.

Does the dialogue begin too early?

Too late?

---

### Experiment E

Replace:

```gdscript
print(dialogue)
```

with:

```gdscript
$CanvasLayer/Label.text = dialogue
```

(or your preferred UI element)

Observe.

The gameplay trigger remains exactly the same.

Only the presentation changes.

---

# Practical Applications

This pattern appears throughout games.

Examples include:

- NPC conversations
- tutorial regions
- warning signs
- environmental storytelling
- quest updates
- cutscene triggers
- narration
- discovery messages

Many narrative systems begin with a simple Area.

---

# Common Misconceptions

### "The Area is the dialogue system."

No.

The Area only determines **when** dialogue begins.

---

### "Dialogue belongs inside the player."

Usually not.

Dialogue is often tied to:

- a location
- an NPC
- an event

---

### "Printing text is the final solution."

Printing is useful for learning.

Larger projects usually send the dialogue to a dedicated UI or Dialogue Manager.

---

# Workbench Habit

Whenever gameplay asks:

> **When should this information appear?**

consider using an Area3D.

The Area controls the timing.

Another system controls the presentation.

---

# Challenge

Create three dialogue regions.

Give each one a different message.

For example:

```
Welcome!

Danger Ahead!

You Found a Secret!
```

Walk through the level.

Notice that the environment itself begins communicating with the player.

Nothing about the player's movement changed.

Only the information being presented changed.

Now ask yourself:

How might a dedicated Dialogue Manager improve this system as your project grows?