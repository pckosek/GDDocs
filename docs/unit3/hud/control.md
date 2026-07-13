# Technique 3.2 — Create a Control Node

## Classification

**Type:** Engineering Technique

**Category:** Heads-Up Display (HUD)

**Difficulty:** Beginner

**Estimated Time:** 15–20 minutes

---

# Design Scenario

In the previous technique, we created a **CanvasLayer**.

Our interface now exists in screen space.

But there is still a problem.

Where should interface elements actually go?

How do we position:

- score
- health
- minimap
- inventory
- dialogue

Unlike the game world, interface elements are not positioned using meters.

They are arranged using **Control** nodes.

---

# Why This Technique Matters

Everything we have built so far has existed in **3D space**.

Objects have:

- position
- rotation
- scale

User interfaces behave differently.

Instead of existing inside a world, interface elements occupy portions of the screen.

A **Control** node provides the foundation for organizing that screen.

Nearly every visible interface element in Godot inherits from **Control**.

---

# Mental Model

Think of a blank sheet of graph paper.

The paper already exists.

But before drawing anything useful, you decide where different information belongs.

Perhaps:

- a title at the top
- instructions on the left
- a score in the corner

The sheet becomes organized before anything is written.

A **Control** node performs a similar role.

It establishes an area where interface elements can be arranged.

---

# Starter Implementation

Begin with the CanvasLayer created previously.

```text
CanvasLayer
└── Control
```

Run the project.

Nothing visible appears.

The Control node does not display anything by itself.

Instead, it provides a region where interface elements can be placed.

---

# Anatomy

## CanvasLayer

Responsible for:

> Creating a coordinate system attached to the screen.

---

## Control

Responsible for:

> Organizing interface elements within that screen space.

Control nodes can contain other Control nodes, forming interface hierarchies much like Node3D creates scene hierarchies.

---

# Design Principle

## Layout is separate from content.

Consider a classroom bulletin board.

The board defines where information can be displayed.

The announcements themselves change every week.

Likewise:

```text
CanvasLayer
    ↓
Control
    ↓
Labels
Buttons
Panels
Progress Bars
Images
```

The Control node defines **where** things belong.

Its children define **what** is displayed.

Keeping these responsibilities separate makes interfaces easier to understand and modify.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Create:

```text
CanvasLayer
└── Control
```

Run the project.

Observe.

What appears?

---

### Experiment B

Select the Control node.

Resize it.

Observe the outline displayed in the editor.

How much of the screen does it occupy?

---

### Experiment C

Create a Label beneath the Control node.

```text
CanvasLayer
└── Control
    └── Label
```

Change the label text.

Run the project.

Observe where the text appears.

---

### Experiment D

Move the Label beneath a different Control node.

Observe.

Did the displayed information change?

Or only where it belonged?

---

# Practical Observation

Many interface elements inherit from **Control**, including:

- Label
- Button
- TextureRect
- Panel
- ProgressBar
- ColorRect
- LineEdit
- OptionButton

Learning Control means learning the foundation shared by nearly every interface component in Godot.

---

# Common Misconceptions

### "Control is the interface."

No.

Control usually does not display meaningful information.

It provides the structure that other interface elements use.

---

### "Control is just another Node."

Not quite.

Node3D organizes objects in the game world.

Control organizes objects in screen space.

Although they both build hierarchies, they solve different problems.

---

### "I should position my HUD like I position my player."

Not usually.

World objects use transforms.

Interface elements use layout systems.

Trying to treat one like the other quickly becomes frustrating.

---

# Reflection

Complete the sentence.

> CanvasLayer creates...

Complete the sentence.

> Control organizes...

Now answer:

Why might it be useful to separate the layout of an interface from the information displayed inside it?

---

# Self Check

Before moving on, ask yourself:

✓ I understand why Control exists.

✓ I can explain the difference between CanvasLayer and Control.

✓ I know that most UI elements inherit from Control.

✓ I understand that layout and content are separate ideas.

---

# Looking Ahead

A Control node gives us a place to build an interface.

The next question becomes:

> **How do we position interface elements reliably on different screen sizes?**

We'll begin exploring **anchors**, which allow interfaces to remain organized regardless of the player's resolution.