# Technique 3.4 — Use Containers

## Classification

**Type:** Engineering Technique

**Category:** Heads-Up Display (HUD)

**Difficulty:** Beginner

**Estimated Time:** 20–25 minutes

---

# Design Scenario

Your interface is growing.

You now have:

- a score
- a timer
- a health bar
- a lives counter

At first, arranging them is easy.

You drag each element into position.

Then you decide to add another label.

Now everything must be moved.

Later you change the font size.

Everything shifts again.

As interfaces become more complex, manually positioning every element quickly becomes frustrating.

This is the problem that **Containers** solve.

---

# Why This Technique Matters

Earlier we learned that:

- **CanvasLayer** creates screen space.
- **Control** organizes interface elements.
- **Anchors** determine what part of the screen an element follows.

But there is still an important question.

How should multiple interface elements arrange themselves?

Instead of positioning every object manually, Containers automatically organize their children according to a set of layout rules.

---

# Mental Model

Imagine arranging books on a bookshelf.

You could measure the exact position of every book with a ruler.

Or...

You could simply place each new book beside the previous one.

The shelf handles the organization.

Containers work the same way.

Rather than positioning every child yourself, you define the rules once.

The Container performs the layout automatically.

---

# Starter Implementation

Create the following hierarchy.

```text
CanvasLayer
└── Control
    └── VBoxContainer
        ├── Label
        ├── Label
        └── Label
```

Give each Label different text.

For example:

```text
Score: 100

Lives: 3

Health: 75%
```

Run the project.

Observe.

The labels are automatically arranged into a vertical list.

No manual positioning was required.

---

# Anatomy

## Container

A Control node that automatically positions its children according to specific layout rules.

---

## VBoxContainer

Arranges children from top to bottom.

```text
Item 1
Item 2
Item 3
```

---

## HBoxContainer

Arranges children from left to right.

```text
Item 1   Item 2   Item 3
```

---

## GridContainer

Arranges children into rows and columns.

Useful for:

- inventories
- icon grids
- crafting systems
- selection menus

---

# Design Principle

## Describe the layout, not the positions.

Earlier, we positioned interface elements individually.

Containers encourage a different way of thinking.

Instead of asking:

> "Where should this Label go?"

we ask:

> "How should this group be organized?"

The Container answers the second question automatically.

This shifts our attention from coordinates to relationships.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Create a VBoxContainer.

Add three Labels.

Observe.

What determines their positions?

---

### Experiment B

Swap the VBoxContainer for an HBoxContainer.

Observe.

What changed?

---

### Experiment C

Add another Label.

Observe.

Did you need to reposition the existing Labels?

---

### Experiment D

Delete the middle Label.

Observe.

How does the remaining layout change?

---

### Experiment E

Create a GridContainer.

Experiment with different numbers of children.

Observe how the layout adjusts automatically.

---

# Practical Observation

Containers are commonly used for:

- health displays
- score panels
- inventory grids
- dialogue options
- pause menus
- settings screens
- button menus
- toolbars

Many professional interfaces contain Containers nested inside other Containers to create complex layouts from simple building blocks.

---

# Common Misconceptions

### "Containers are only for menus."

No.

Any collection of related interface elements can benefit from automatic layout.

---

### "I should move the children manually."

Usually not.

The Container controls the positions of its children.

Manual positioning often has little effect or is overridden.

---

### "Containers replace Anchors."

No.

Anchors determine **where the group belongs**.

Containers determine **how the group's children are arranged**.

These systems work together.

---

# Reflection

Complete the sentence.

> Anchors determine...

Complete the sentence.

> Containers determine...

Now answer:

Why might automatically arranging interface elements be easier than positioning each one individually?

---

# Self Check

Before moving on, ask yourself:

✓ I understand why Containers exist.

✓ I can explain the difference between Anchors and Containers.

✓ I can use a VBoxContainer to organize interface elements.

✓ I know when an HBoxContainer or GridContainer might be more appropriate.

---

# Looking Ahead

Containers organize interface elements into meaningful layouts.

The next question becomes:

> **How do we display information that changes while the game is running?**

We'll begin with one of the simplest and most useful interface elements:

**Labels**, which allow the game to communicate information such as scores, health, timers, and player status.