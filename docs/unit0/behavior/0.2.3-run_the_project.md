# Operation 0.2.3 — Run the Project

## Classification

**Type:** Operation
**Category:** Behavior Operations
**Difficulty:** Beginner
**Estimated Time:** 5 seconds

---

## Purpose

Running the project launches the entire game starting from the project's designated Main Scene.

Unlike **Run Scene**, which only tests the currently open scene, **Run Project** simulates the actual experience a player will have when launching your game.

This allows you to test:

* menus
* scene transitions
* global systems
* autoloads
* game flow
* interactions between multiple scenes

---

## When Would I Use This?

Use this operation whenever:

* You want to test the complete game
* You want to verify scene transitions
* You want to test menus
* You want to test autoload systems
* You want to experience the project as a player would

Examples:

* Start from the title screen
* Test level progression
* Verify save systems
* Test global game managers
* Confirm that scene loading works correctly

---

## Prerequisites

Before beginning:

* A project exists
* A Main Scene has been assigned

Example:

```text
Project Settings
└── Application
    └── Run
        └── Main Scene
```

A valid Main Scene might be:

```text
res://scenes/Main.tscn
```

or

```text
res://scenes/TitleScreen.tscn
```

---

## Procedure

### Step 1 — Save Your Work

Before running the project:

```text
Ctrl + S
```

or

```text
Scene → Save Scene
```

Save any modified scenes or scripts.

---

### Step 2 — Run the Project

Choose one of the following methods:

**Method 1**

Press:

```text
F5
```

**Method 2**

Click:

```text
Run Project
```

at the top-right of the Godot editor.

The icon appears as a large play button.

---

### Step 3 — Observe Project Behavior

Godot will launch the project's Main Scene.

The game should behave exactly as it would for a player.

Examples:

* Title screen appears
* Player loads correctly
* Audio begins playing
* UI becomes visible
* Autoload systems initialize

---

### Step 4 — Test the Experience

Interact with the project.

Examples:

* Navigate menus
* Move the player
* Trigger events
* Change scenes
* Verify progression systems

Pay attention to both expected and unexpected behavior.

---

### Step 5 — Close the Project

When testing is complete:

```text
Esc
```

or close the game window.

You will return to the editor.

---

## Success Check

You should now have:

✓ A running game window

✓ The project's Main Scene loaded

✓ All global systems active

✓ The ability to interact with the project as a player

---

## Common Mistakes

### Mistake 1

No Main Scene is configured.

Result:

Godot displays a message asking which scene should be used.

Solution:

Assign a Main Scene in:

```text
Project Settings
→ Application
→ Run
→ Main Scene
```

---

### Mistake 2

Expecting the currently open scene to run.

Result:

Godot launches the Main Scene instead.

Solution:

Use **Run Scene (F6)** if you want to test only the current scene.

---

### Mistake 3

Testing features in isolation but never testing the full game.

Result:

Individual scenes work correctly, but scene transitions fail.

Solution:

Regularly test the complete project.

---

### Mistake 4

Ignoring startup errors.

Result:

Global systems may fail silently.

Solution:

Review the Output panel whenever the project launches.

---

### Mistake 5

Assuming a working scene guarantees a working game.

Result:

Integration problems go unnoticed.

Solution:

Test both individual scenes and the complete project.

---

## Why This Matters

As projects grow, problems increasingly occur between systems rather than within individual systems.

A player does not experience:

```text
Player.tscn
```

They experience:

```text
Title Screen
    ↓
Main Menu
    ↓
Game World
    ↓
Pause Menu
    ↓
Game Over Screen
```

Run Project allows you to test the entire experience.

---

## Design Insight

A useful distinction is:

### Run Scene

Tests a component.

---

### Run Project

Tests a system.

---

For example:

```text
Player.tscn
```

might work perfectly when run alone.

However:

```text
Main.tscn
```

may reveal:

* missing references
* broken scene transitions
* autoload issues
* camera problems
* UI conflicts

Running the project helps identify integration issues.

---

## Professional Practice

Professional developers frequently alternate between:

```text
F6
```

for rapid testing

and

```text
F5
```

for full-system testing.

A common workflow is:

```text
Develop Feature
    ↓
Run Scene (F6)
    ↓
Fix Problems
    ↓
Run Project (F5)
    ↓
Verify Integration
```

Both types of testing are important.

---

## Run Scene vs Run Project

| Operation        | Purpose                       |
| ---------------- | ----------------------------- |
| Run Scene (F6)   | Test the currently open scene |
| Run Project (F5) | Test the entire game          |

Think of Run Scene as testing a single part.

Think of Run Project as testing the complete machine.

---

## Related Operations

* 0.2.0 Create Script
* 0.2.1 Attach Script
* 0.2.2 Run Scene
* 0.2.4 Print Debug Information
* 0.4.0 Configure a Main Scene

---

## Related Techniques

This operation supports the following techniques:

* System Testing
* Integration Testing
* Game Flow Design
* Debugging
* Iterative Development