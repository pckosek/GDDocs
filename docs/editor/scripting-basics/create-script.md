# Operation 0.2.0 — Create Script

## Classification

**Type:** Operation
**Category:** Behavior Operations
**Difficulty:** Beginner
**Estimated Time:** 1 minute

---

## Purpose

Creating a script gives a node a place to store behavior written in GDScript.

In Godot, scripts are how objects become interactive.

A script can control:

* movement
* input
* timers
* scoring
* collisions
* UI updates
* game state
* debugging output

Without scripts, a scene is usually only a static arrangement of nodes.

---

## When Would I Use This?

Use this operation whenever you want a node to do something over time or respond to events.

Examples:

* Make a player move
* Make an enemy patrol
* Make a light flicker
* Make a pickup disappear
* Make a button react when pressed
* Make a system print debug information

---

## Prerequisites

Before beginning:

* Godot is open
* A scene exists
* A node exists that will receive the script

Example:

```text
Player
```

or

```text
Camera3D
```

or

```text
Main
```

---

## Procedure

### Step 1 — Select the Node

In the Scene Tree, click the node that will receive the script.

Example:

```text
Player
```

---

### Step 2 — Create the Script

One of the most common methods is:

```text
Right Click Node → Attach Script
```

If the node does not yet have a script, Godot will prompt you to create one.

You may also use the **Attach Script** button in the scene interface.

---

### Step 3 — Choose the Script Settings

Godot will show a script creation dialog.

Common settings include:

* **Language**: GDScript
* **Inheritance**: matches the selected node type
* **Path**: where the script file will be saved

Example:

```text
res://scripts/Player.gd
```

---

### Step 4 — Confirm Creation

Press:

```text
Create
```

Godot will create the script file and attach it to the selected node.

---

### Step 5 — Verify the Script Exists

The node should now show a script icon.

The script file should also appear in the FileSystem panel.

Example:

```text
res://scripts/Player.gd
```

---

## Success Check

You should now have:

✓ A script file created
✓ The script attached to a node
✓ A script icon visible on the node
✓ A place to begin writing behavior

Example scene tree:

```text
Player
```

with a script attached.

---

## Common Mistakes

### Mistake 1

Creating a script but not attaching it to the correct node.

Result:

The code exists, but the node does not use it.

Solution:

Always confirm the selected node before creating the script.

---

### Mistake 2

Saving the script in a confusing location.

Example:

```text
res://PlayerScriptFinal.gd
```

Result:

Files become hard to find later.

Solution:

Use a clear folder structure such as:

```text
res://scripts/Player.gd
```

---

### Mistake 3

Creating multiple scripts for the same job.

Result:

Behavior becomes fragmented and difficult to debug.

Solution:

Start with one clear script per responsibility unless a more advanced structure is needed.

---

### Mistake 4

Assuming the script does something by itself.

Result:

Students expect magic where there is none.

Solution:

A script must contain code before it affects the game.

---

## Why This Matters

Scripts are the bridge between scene structure and game behavior.

A scene tells Godot **what exists**.

A script tells Godot **what it should do**.

This is one of the most important distinctions in the engine.

---

## Design Insight

A useful way to think about scripts is:

> Scenes organize objects. Scripts animate intentions.

The same node can exist without behavior, but once a script is attached, it can respond to input, manage state, or drive a system.

This is the point where a static project begins becoming interactive.

---

## Professional Practice

Developers typically create scripts early and name them clearly.

Examples:

```text
Player.gd
Enemy.gd
HUD.gd
GameManager.gd
CameraController.gd
```

Good script names help communicate what a file is responsible for.

---

## Related Operations

* 0.1 Add a Child Node
* 0.2.1 Assign Script
* 0.2.2 Run Scene
* 0.2.3 Run Project
* 0.2.4 Print Debug Information

---

## Related Techniques

This operation supports the following techniques:

* Scripted Behavior
* Interactive Systems
* Scene Logic
* Game State Management
* Debugging