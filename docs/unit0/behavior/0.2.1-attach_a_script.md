# Operation 0.2.1 — Attach a Script

## Classification

**Type:** Operation
**Category:** Behavior Operations
**Difficulty:** Beginner
**Estimated Time:** 30 seconds

---

## Purpose

Attaching a script connects an existing script file to a node.

While **creating a script** generates a new `.gd` file, **attaching a script** links an existing script to a node so that the node can use its behavior.

This allows developers to:

* reuse code
* share behavior across scenes
* reconnect scripts after refactoring
* separate behavior from scene construction

---

## When Would I Use This?

Use this operation whenever:

* A script already exists
* You want a node to use existing behavior
* You are reusing a script from another scene
* A script was accidentally detached
* You are following a tutorial or class exercise that provides scripts

Examples:

* Attach `Player.gd` to a Player node
* Attach `CameraController.gd` to a Camera3D
* Attach `Enemy.gd` to an enemy scene
* Attach `HUD.gd` to a user interface

---

## Prerequisites

Before beginning:

* A node exists
* A script file already exists

Example:

```text
res://scripts/Player.gd
```

---

## Procedure

### Step 1 — Select the Target Node

In the Scene Tree, click the node that should receive the script.

Example:

```text
Player
```

---

### Step 2 — Open the Attach Script Dialog

Right-click the node and select:

```text
Attach Script
```

Alternatively, use the script button at the top of the Scene panel.

---

### Step 3 — Locate the Existing Script

In the script dialog, click the folder icon next to the script path.

Navigate to the desired script file.

Example:

```text
res://scripts/Player.gd
```

Select the file.

---

### Step 4 — Confirm the Attachment

Press:

```text
Create
```

or

```text
Attach
```

depending on your version of Godot.

The selected script is now connected to the node.

---

### Step 5 — Verify the Connection

The node should display a script icon.

Selecting the node should reveal the attached script in the Inspector.

Example:

```text
Player
```

with a script icon next to its name.

---

## Success Check

You should now have:

✓ A node

✓ An attached script

✓ A visible script icon

✓ A node capable of executing the script's behavior

---

## Common Mistakes

### Mistake 1

Attaching the wrong script.

Example:

```text
Enemy.gd
```

attached to:

```text
Player
```

Result:

Unexpected behavior or runtime errors.

Solution:

Verify both the node and script before attaching.

---

### Mistake 2

Attaching a script designed for a different node type.

Example:

A script written for:

```text
CharacterBody3D
```

attached to:

```text
Camera3D
```

Result:

Errors may occur because expected properties or functions do not exist.

Solution:

Ensure the script was designed for the selected node type.

---

### Mistake 3

Assuming the script is attached because it exists.

Result:

Students create a script file but never connect it to a node.

Solution:

Confirm the script icon appears in the Scene Tree.

---

### Mistake 4

Attaching multiple scripts to solve unrelated problems.

Result:

Behavior becomes difficult to manage.

Solution:

Think carefully about which node owns which responsibility.

---

## Why This Matters

In Godot, behavior is attached to nodes.

A script file sitting in the FileSystem does nothing by itself.

The script only becomes active when it is attached to a node that exists in a running scene.

Think of a script as a set of instructions.

Attaching the script tells Godot:

> "Use these instructions for this object."

---

## Design Insight

A useful distinction is:

### Create Script

Creates a new behavior file.

---

### Attach Script

Assigns an existing behavior file to a node.

---

Example:

```text
Player.gd
```

may already exist.

Attaching it to:

```text
Player
```

allows that node to use the behavior.

The file and the node are separate things until they are connected.

---

## Professional Practice

Many developers create reusable scripts that can be attached to multiple scenes.

Examples:

```text
HealthComponent.gd
Damageable.gd
Interactable.gd
CameraController.gd
```

The same script may be reused across many projects and scenes.

This reduces duplication and improves consistency.

---

## Connection to Reuse

One of the major goals of software development is avoiding repeated work.

Attaching scripts allows a single behavior to be reused wherever it is needed.

For example:

```text
EnemyA
EnemyB
EnemyC
```

may all use:

```text
Enemy.gd
```

rather than maintaining three separate copies.

---

## Related Operations

* 0.2.0 Create Script
* 0.2.2 Run Scene
* 0.2.3 Run Project
* 0.2.4 Print Debug Information
* 0.1.5 Instantiate a Scene

---

## Related Techniques

This operation supports the following techniques:

* Scripted Behavior
* Reusable Components
* Scene Logic
* Object-Oriented Design
* Modular Development