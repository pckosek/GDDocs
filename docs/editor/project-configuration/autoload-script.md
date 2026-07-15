# Operation 0.4.1 — Configure an Autoload

## Classification

**Type:** Operation
**Category:** Project / Editor Configuration
**Difficulty:** Intermediate
**Estimated Time:** 2 minutes

---

## Purpose

An Autoload is a script or scene that Godot automatically loads when the project starts.

Unlike normal scenes, which are created and destroyed as the game runs, an Autoload remains available for the entire lifetime of the project.

Autoloads are commonly used for:

* global game state
* score tracking
* inventory systems
* save systems
* scene management
* settings management

A useful mental model is:

> Most objects exist somewhere in the world.
>
> An Autoload exists above the world.

---

## When Would I Use This?

Use an Autoload whenever information needs to be accessible from many different scenes.

Examples:

* Track player score
* Store collected keys
* Manage game settings
* Track current level
* Store player statistics
* Handle scene transitions

---

## Why Not Use a Regular Scene?

Consider a game with:

```text
TitleScreen
Level1
Level2
GameOver
```

When the player changes scenes:

```text
Level1
↓
Level2
```

everything in Level1 is destroyed.

If important data is stored inside Level1, it disappears.

Autoloads solve this problem by remaining active regardless of which scene is currently loaded.

---

## Prerequisites

Before beginning:

* A project exists
* A script or scene exists

Common examples:

```text
GameManager.gd
```

```text
SceneManager.gd
```

```text
Settings.gd
```

---

## Procedure

### Step 1 — Create the Script

Create a script that will act as the Autoload.

Example:

```gdscript
extends Node

var score = 0
```

Save the script.

Example:

```text
res://scripts/GameManager.gd
```

---

### Step 2 — Open Project Settings

Select:

```text
Project
→ Project Settings
```

---

### Step 3 — Open the Autoload Tab

Select:

```text
Globals
```

or

```text
Autoload
```

depending on your Godot version.

---

### Step 4 — Select the Script

Browse to the script file.

Example:

```text
res://scripts/GameManager.gd
```

---

### Step 5 — Choose a Name

Provide a name.

Example:

```text
GameManager
```

This name becomes globally accessible throughout the project.

---

### Step 6 — Add the Autoload

Press:

```text
Add
```

The Autoload should now appear in the list.

Example:

```text
GameManager
```

---

## Success Check

You should now have:

✓ An Autoload configured

✓ The Autoload listed in Project Settings

✓ Global access to the Autoload

✓ The Autoload loaded automatically when the project starts

---

## Common Example

### Global Score Manager

Autoload:

```gdscript
extends Node

var score = 0
```

Any script can access:

```gdscript
GameManager.score += 100
```

without needing to find or reference a node in the scene tree.

---

## Common Example

### Key Collection System

Autoload:

```gdscript
extends Node

var maze_key = false
var gate_key = false
```

Scene A:

```gdscript
GameManager.maze_key = true
```

Scene B:

```gdscript
if GameManager.maze_key:
```

The information persists even after changing scenes.

---

## Common Mistakes

### Mistake 1

Trying to use an Autoload before configuring it.

Result:

Errors occur because the global name does not exist.

Solution:

Verify the script appears in the Autoload list.

---

### Mistake 2

Using an Autoload for everything.

Result:

Large, difficult-to-maintain global systems.

Solution:

Only place truly global information in an Autoload.

---

### Mistake 3

Confusing Autoload with scene instancing.

Result:

Students expect Autoloads to behave like normal scene objects.

Solution:

Remember that Autoloads are initialized automatically and remain active.

---

### Mistake 4

Renaming the script but forgetting the Autoload name.

Result:

Confusion when accessing the singleton.

Solution:

Use clear and consistent naming.

---

### Mistake 5

Storing scene-specific information in an Autoload.

Result:

Global systems become cluttered.

Solution:

Ask:

> Does this information need to survive scene changes?

If not, it probably should not be in an Autoload.

---

## Why This Matters

Many games contain information that must survive scene transitions.

Examples:

* score
* collected items
* player settings
* unlocked levels
* game progress

Without Autoloads:

```text
Change Scene
↓
Lose Data
```

With Autoloads:

```text
Change Scene
↓
Keep Data
```

This makes them one of the most useful project-level tools in Godot.

---

## Design Insight

Autoloads introduce an important distinction:

### Local State

Belongs to a specific scene.

Example:

```text
Enemy Health
```

---

### Global State

Belongs to the entire game.

Example:

```text
Player Score
```

Autoloads are designed for global state.

---

## Professional Practice

Many professional projects use a small number of carefully designed Autoloads.

Common examples:

```text
GameManager
SceneManager
AudioManager
SettingsManager
SaveManager
```

Notice that these systems manage information for the entire game rather than individual objects.

---

## Relationship to Scene Changes

One of the most common reasons to use an Autoload is:

```text
Title Screen
↓
Level 1
↓
Level 2
↓
Game Over
```

Normal scene nodes disappear as scenes change.

Autoloads remain available throughout the entire process.

---

## Related Operations

* 0.2.0 Create Script
* 0.2.1 Attach Script
* 0.2.3 Run Project
* 0.4.0 Configure Input Mapping
* 0.4.2 Configure Project Settings

---

## Related Techniques

This operation supports the following techniques:

* Global State Management
* Scene Management
* Save Systems
* Game Progression
* Event Coordination