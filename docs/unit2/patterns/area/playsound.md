# Pattern 2.11.7 — Play a Sound

## Classification

**Type:** Gameplay Pattern

**Category:** Audio

**Difficulty:** Beginner

**Prerequisites:**

- AudioStreamPlayer3D
- Area3D
- Signals

---

# Problem

Many gameplay events should provide immediate audio feedback.

Examples include:

- collecting a coin
- opening a door
- reaching a checkpoint
- pressing a button
- activating a trigger

Rather than printing a message, we often want to play a sound.

---

# Starter Implementation

Create the following hierarchy.

```text
Checkpoint (Area3D)
├── CollisionShape3D
├── MeshInstance3D
└── AudioStreamPlayer3D
```

Select the **AudioStreamPlayer3D**.

In the Inspector:

1. Locate **Stream**
2. Click **<empty>**
3. Choose **Load**
4. Select a sound file (`.wav`, `.ogg`, or `.mp3`)
5. Leave **Autoplay** disabled

The AudioStreamPlayer3D is now ready to play sounds.

---

# Starter Code

Attach the following script to the Area3D.

```gdscript
extends Area3D

@onready var sound := $AudioStreamPlayer3D

func _on_body_entered(body):

	if body is CharacterBody3D:

		sound.play()
```

Run the scene.

Walk into the checkpoint.

Observe.

The sound plays once when the player enters.

---

# How It Works

```text
Player

↓

Area Detects

↓

Signal

↓

AudioStreamPlayer3D.play()
```

Notice that the Area does not contain the sound.

It simply tells the AudioStreamPlayer3D to play.

---

# Anatomy

## AudioStreamPlayer3D

Responsible for:

> Playing sounds in three-dimensional space.

---

## Audio Stream

Responsible for:

> The actual sound file.

Examples:

- footsteps
- music
- dialogue
- sound effects

---

## play()

Starts playback.

The AudioStreamPlayer3D manages the rest.

---

# Design Principle

## Separate the event from the presentation.

The gameplay event is:

> Player entered the checkpoint.

The presentation is:

> Play a sound.

Keeping these ideas separate allows you to later:

- replace the sound
- add particles
- update the HUD

without changing the gameplay logic.

---

# Experiment

Only change one thing.

---

### Experiment A

Replace the sound file.

Observe.

How does the checkpoint feel?

---

### Experiment B

Enable:

```text
Autoplay
```

Run the scene.

Observe.

Why is this usually undesirable for trigger sounds?

---

### Experiment C

Lower:

```text
Volume dB
```

Observe.

---

### Experiment D

Enable:

```text
Loop
```

Observe.

When might looping be appropriate?

---

### Experiment E

Duplicate the checkpoint.

Assign a different sound to each.

Observe.

Each Area now communicates a different event.

---

# Practical Observation

Most gameplay sounds follow exactly the same pattern.

Examples include:

- pickups
- doors
- checkpoints
- switches
- hazards
- enemy attacks
- UI buttons

The event changes.

The AudioStreamPlayer stays the same.

---

# Common Misconceptions

### "The sound belongs in the script."

Usually not.

The AudioStreamPlayer3D owns playback.

Your script simply requests it.

---

### "Autoplay should always be enabled."

Most gameplay sounds should only play when something happens.

Leave Autoplay disabled unless the sound should begin automatically.

---

### "One AudioStreamPlayer should play every sound."

Usually not.

Many gameplay objects contain their own AudioStreamPlayer3D.

This keeps responsibilities localized.

---

### "The Area plays the sound."

The Area triggers the event.

The AudioStreamPlayer performs the playback.

---

# Workbench Habit

Whenever gameplay needs audio feedback:

Ask yourself:

> **What event should cause the sound?**

The event should trigger the AudioStreamPlayer.

The AudioStreamPlayer should handle playback.

---

# Challenge

Create three checkpoints.

Assign a different sound to each.

Examples:

- checkpoint
- warning
- success

Walk through the level.

Notice how audio begins communicating information even before the player consciously processes the visual scene.