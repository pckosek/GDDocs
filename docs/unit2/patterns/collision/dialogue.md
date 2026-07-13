# Pattern 2.11.6 — Start a Dialogue

## Classification

**Type:** Gameplay Pattern

**Category:** Area Detection

**Difficulty:** Intermediate

**Prerequisites:**

- Area3D
- Signals
- CanvasLayer (optional)

---

# Problem

Many games need to communicate information to the player.

Examples include:

- NPC conversations
- tutorial prompts
- warning messages
- story events
- signposts

Often, these messages should appear only when the player enters a particular location.

Area3D provides a simple way to trigger these events.

---

# Starter Implementation

Create the following scene.

```text
World
├── Player (CharacterBody3D)
└── DialogueTrigger (Area3D)
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
Player

↓

Enter Area

↓

Signal

↓

Dialogue Starts
```

Notice that the Area does not contain the dialogue system.

It simply begins the interaction.

---

# Anatomy

## Area3D

Detects the player.

---

## body_entered()

Determines when the conversation begins.

---

## dialogue

Stores the text associated with this trigger.

---

# Design Principle

## Triggers begin experiences.

The Area is not responsible for displaying dialogue.

It is responsible for deciding **when** the dialogue should begin.

Keeping those responsibilities separate makes systems easier to expand.

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

Give each trigger different dialogue.

Walk through both.

Observe.

---

### Experiment C

Move the trigger.

Observe.

How does location affect storytelling?

---

### Experiment D

Make the trigger very large.

Observe.

Does the dialogue begin too early?

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

The gameplay event stays exactly the same.

Only the presentation changes.

---

# Practical Applications

This pattern appears throughout games.

Examples include:

- NPC conversations
- tutorial zones
- warning signs
- narration
- environmental storytelling
- quest updates
- cutscene triggers

The Area determines **when** information is presented.

---

# Common Misconceptions

### "The Area is the dialogue system."

No.

The Area simply triggers the event.

---

### "Dialogue belongs inside the player."

Usually not.

Dialogue is often associated with a location or an NPC.

---

### "The text should always be printed."

Printing is useful for learning.

Larger projects usually forward the dialogue to a dedicated UI or dialogue manager.

---

# Workbench Habit

Whenever gameplay asks:

> **"When should this information appear?"**

consider using an Area3D.

The Area controls **timing**.

Another system controls **presentation**.

---

# Challenge

Create three dialogue regions.

Each one displays a different message.

For example:

- "Welcome!"
- "Danger Ahead!"
- "You found a secret."

Walk through the level.

Notice how the environment itself begins telling a story without requiring any interaction from the player.