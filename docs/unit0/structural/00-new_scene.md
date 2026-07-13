# Operation 0.0 — Create a New Scene

## Classification

**Type:** Operation

**Category:** Project Setup

**Difficulty:** Beginner

**Estimated Time:** 2 minutes

---

## Purpose

Before you can build anything in Godot, you must create a scene.

Scenes are the fundamental building blocks of every Godot project. A scene can represent:

* A complete game level
* A player
* An enemy
* A user interface
* A camera rig
* A reusable object

Nearly everything you create in Godot begins as a scene.

---

## When Would I Use This?

Use this operation whenever you want to:

* Create a new game object
* Start a new level
* Build a reusable component
* Begin a new project

---

## Prerequisites

Before beginning:

* Godot is installed
* Godot is open
* A project has been created or opened

---

## Procedure

### Step 1 — Open the Scene Menu

From the top menu bar select:

```
Scene → New Scene
```

Alternatively, press:

```
Ctrl + N
```

A new empty scene will appear.

---

### Step 2 — Select a Root Node

Godot requires every scene to begin with a root node.

Click:

```
Other Node
```

Choose an appropriate root node.

For most beginning projects:

| Purpose          | Recommended Root                  |
| ---------------- | --------------------------------- |
| General 3D Scene | Node3D                            |
| General 2D Scene | Node2D                            |
| User Interface   | Control                           |
| Player Character | CharacterBody2D / CharacterBody3D |

For this course, most Unit 1 projects should begin with:

```
Node3D
```

Press:

```
Create
```

---

### Step 3 — Rename the Root Node

The default node name is often generic.

Example:

```
Node3D
```

Rename it to something meaningful.

Examples:

```
World
Main
SolarSystem
FlyingMachine
StillLife
```

To rename:

* Select the node
* Press F2

OR

* Double-click the node name

---

### Step 4 — Save the Scene

Select:

```
Scene → Save Scene
```

or press:

```
Ctrl + S
```

Create a folder structure if necessary.

Example:

```
scenes/
```

Save the file with a descriptive name.

Examples:

```
Main.tscn
SolarSystem.tscn
FlyingMachine.tscn
```

---

## Success Check

You should now have:

✓ A new scene

✓ A root node

✓ A meaningful node name

✓ A saved .tscn file

Your Scene panel should look similar to:

```
World
```

or

```
Main
```

with a small Node3D icon next to it.

---

## Common Mistakes

### Mistake 1

Creating a scene but never saving it.

Result:

Work may be lost if Godot closes unexpectedly.

Solution:

Save immediately after creating the root node.

---

### Mistake 2

Leaving the node named:

```
Node3D
```

Result:

Projects become difficult to navigate later.

Solution:

Rename nodes to reflect their purpose.

---

### Mistake 3

Choosing the wrong root node type.

Example:

Using a Control node for a 3D world.

Solution:

Think about the purpose of the scene before creating it.

---

## Why This Matters

Scenes are the primary organizational structure in Godot.

As projects become larger, good scene organization makes it easier to:

* Find objects
* Reuse systems
* Debug problems
* Collaborate with others

Every major project in this course begins with a well-organized scene.

---

## Related Operations

* 0.1 Add a Child Node
* 0.2 Save a Scene
* 0.3 Create Folders in the FileSystem
* 0.4 Rename Nodes
* 0.5 Instantiate a Scene

---

## Related Techniques

This operation supports the following techniques:

* Scene Construction
* Scene Organization
* Reusable Scene Design
* World Building