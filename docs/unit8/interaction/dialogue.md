# 8.3.2 Dialogue

## Classification

**Type:** Engineering Technique

**Category:** Interaction

**Difficulty:** Beginner

**Estimated Time:** 20–30 minutes

---

# Design Problem

Imagine walking up to an NPC.

The player presses:

```text
Interact
```

What should happen?

The NPC should begin a conversation.

The player should:

- read the dialogue
- advance the conversation
- return to gameplay

Dialogue is simply another interaction between the player and the world.

---

# Why This Matters

Dialogue communicates information.

Examples include:

- story
- instructions
- hints
- worldbuilding
- quests

Although conversations may appear complicated...

...their underlying structure is usually quite simple.

---

# Mental Model

Think about turning the pages of a book.

Each page contains one part of the conversation.

The reader chooses when to continue.

Games work similarly.

```text
Interact

↓

Textbox

↓

Read

↓

Advance

↓

Continue Playing
```

The player controls the pace of the conversation.

---

# Starter Implementation

A typical conversation begins with interaction.

```text
Player

↓

Area2D

↓

Interact Button

↓

Signal

↓

Dialogue Box
```

The NPC does not display dialogue directly.

Instead...

it emits a signal indicating that a conversation should begin.

The dialogue system responds by opening a textbox.

---

# Advancing Dialogue

Once the textbox is visible...

the player advances through each message.

```text
Line 1

↓

Interact

↓

Line 2

↓

Interact

↓

Close
```

Each press of the interaction button advances the conversation until no dialogue remains.

Control then returns to normal gameplay.

---

# Dissecting the System

Notice the responsibilities.

```text
NPC

↓

Signal
```

```text
Dialogue System

↓

Textbox
```

```text
Player

↓

Advance
```

Each system performs one responsibility.

The conversation remains simple because the responsibilities remain separate.

---

# Design Principle

## Keep dialogue separate from gameplay objects.

NPCs know **what** they want to say.

The dialogue system knows **how** to display it.

Separating these responsibilities allows many different NPCs to share one dialogue system.

---

# Practical Observation

Many beginning projects place textbox code inside every NPC.

As projects grow...

it becomes much easier to create:

```text
NPC

↓

Signal

↓

Shared Dialogue System
```

Now every character can use the same interface.

Only the dialogue changes.

---

# Common Misconceptions

### "NPCs should draw their own dialogue boxes."

Usually not.

A shared dialogue system keeps the project simpler and more consistent.

---

### "Dialogue requires complicated branching."

Not necessarily.

Many games begin with simple linear conversations.

More advanced systems can be added later.

---

### "Dialogue is only for stories."

Dialogue also communicates:

- tutorials
- objectives
- hints
- worldbuilding
- humour

It becomes another way the world responds to the player.

---

### "Pressing Interact should immediately close the dialogue."

Usually each press advances one message.

This gives the player control over the pace of the conversation.

---

# Reflection

Imagine creating:

- a shopkeeper
- a guard
- a villager
- a quest giver

How much of the dialogue system would each NPC actually need?

What parts could every NPC share?

---

# Looking Back

Earlier we learned how to interact with the world.

Now we've applied that interaction to conversation.

Dialogue is simply another interaction system.

The player chooses to communicate.

The world responds.

Keeping the dialogue system separate from individual NPCs makes conversations much easier to build and maintain.

---

# Looking Ahead

Dialogue allows characters to communicate.

Some interactions, however...

change the world itself.

How do we create:

- locked doors
- keys
- switches
- puzzles

that permanently alter the player's adventure?

We'll begin exploring:

> **Keys & Doors**