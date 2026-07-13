# 8.3.1 Interact

## Classification

**Type:** Engineering Technique

**Category:** Interaction

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine standing beside a treasure chest.

The player presses:

```text
Interact
```

What should happen?

Perhaps the chest opens.

Now imagine standing beside:

- an NPC
- a door
- a switch
- a sign

The same button performs a completely different action.

The player has not changed.

Only the object has.

Interaction is one of the defining ideas of adventure games.

---

# Why This Matters

Movement allows players to explore the world.

Interaction allows them to change it.

Common interactive objects include:

- NPCs
- treasure chests
- doors
- switches
- signs
- levers

Although these objects behave differently...

...they often begin exactly the same way.

The player enters an interaction area.

---

# Mental Model

Think about walking through a museum.

You may stand beside many exhibits.

Nothing happens automatically.

Only when you choose to interact does something occur.

Games work similarly.

```text
Player

↓

Nearby Object

↓

Interact

↓

Response
```

The player decides when the interaction begins.

---

# Starter Implementation

A typical interactive object might look like this.

```text
Chest (Node2D)

├── Sprite2D
├── CollisionShape2D
└── Area2D
```

The Area2D detects when the player is nearby.

```gdscript
func _on_area_2d_body_entered(body):

    if body.is_in_group("player"):

        player_nearby = true
```

Later...

when the player presses the interaction button:

```gdscript
if player_nearby and Input.is_action_just_pressed("interact"):

    open_chest()
```

Detection and interaction remain separate systems.

---

# Dissecting the System

Notice the sequence.

```text
Approach Object

↓

Area2D Detects

↓

Player Presses Button

↓

Object Responds
```

Standing nearby is not enough.

The player makes a deliberate decision to interact.

---

# Design Principle

## Detect first.

Interact second.

Area2D determines **whether** interaction is possible.

The interaction button determines **whether** the player chooses to perform it.

Separating these responsibilities creates interactions that feel deliberate rather than automatic.

---

# Practical Observation

Many different gameplay objects share exactly the same interaction pattern.

Examples include:

```text
NPC

↓

Talk
```

```text
Chest

↓

Open
```

```text
Door

↓

Enter
```

```text
Switch

↓

Activate
```

Although the responses differ...

the interaction system remains remarkably similar.

One input.

Many behaviours.

---

# Common Misconceptions

### "Walking into an object should activate it."

Sometimes.

More often...

players appreciate choosing when to interact.

This prevents accidental conversations, unwanted doors, and unintended actions.

---

### "Every object needs a different interaction system."

Usually not.

Most interactive objects share the same workflow.

Only the final response changes.

---

### "Area2D performs the interaction."

No.

Area2D simply detects that interaction is possible.

The player's input begins the interaction.

---

### "Interaction belongs inside the player."

The player begins interactions.

Individual objects usually decide how they respond.

Keeping those responsibilities separate makes the system much easier to extend.

---

# Reflection

Imagine the player walks beside:

- a treasure chest
- an NPC
- a sign
- a locked door
- a switch

What should happen immediately?

What should wait until the player presses:

```text
Interact
```

Why?

---

# Looking Back

Earlier we explored:

- movement
- collision
- world interaction

Now we've taken another step.

The player no longer affects the world simply by touching it.

Instead...

they intentionally choose when to interact.

This creates a much richer relationship between the player and the world.

Exploration becomes conversation.

---

# Looking Ahead

Interaction allows the player to communicate with the world.

One of the most common forms of interaction is conversation itself.

How can games allow players to:

- read dialogue
- advance conversations
- communicate with NPCs

We'll begin exploring:

> **Dialogue**