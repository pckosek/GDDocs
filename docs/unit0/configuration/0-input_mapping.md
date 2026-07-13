# Operation 0.4.0 — Configure Input Mapping

## Classification

**Type:** Operation
**Category:** Project / Editor Configuration
**Difficulty:** Beginner
**Estimated Time:** 2 minutes

---

## Purpose

Input Mapping allows you to create named actions that connect player inputs to game behavior.

Rather than checking specific keyboard keys, mouse buttons, or controller buttons directly, Godot encourages developers to create actions such as:

```text
move_left
move_right
jump
shoot
interact
pause
```

The game then responds to the action rather than the physical input device.

A useful mental model is:

> The player presses a key.
>
> The key triggers an action.
>
> The game responds to the action.

---

## When Would I Use This?

Use this operation whenever your project needs player input.

Examples:

* Character movement
* Jumping
* Shooting
* Opening menus
* Interacting with objects
* Pausing the game
* Controller support

Most interactive games require input mapping.

---

## Why Not Check Keys Directly?

Beginning programmers often write:

```gdscript
if Input.is_key_pressed(KEY_W):
```

While this works, it creates problems later.

Input Mapping allows:

* Multiple keys for the same action
* Controller support
* Easier customization
* Cleaner code
* Rebinding controls

Instead, Godot encourages:

```gdscript
if Input.is_action_pressed("move_forward"):
```

The game cares about the action, not the physical key.

---

## Prerequisites

Before beginning:

* A Godot project exists
* The project is open

No scene is required.

Input Maps are configured at the project level.

---

## Procedure

### Step 1 — Open Project Settings

Select:

```text
Project
→ Project Settings
```

The Project Settings window will appear.

---

### Step 2 — Open the Input Map Tab

At the top of the window, select:

```text
Input Map
```

You should see:

* Existing actions
* Action creation field
* Assigned inputs

---

### Step 3 — Create a New Action

In the Add New Action field, enter a name.

Examples:

```text
move_left
move_right
jump
shoot
interact
```

Press:

```text
Add
```

The action now exists.

---

### Step 4 — Assign an Input

Locate the newly created action.

Press:

```text
+
```

to add an event.

A dialog will appear.

Press the desired key.

Example:

```text
A
```

or

```text
Space
```

or

```text
Left Mouse Button
```

Press:

```text
OK
```

The key is now mapped to the action.

---

### Step 5 — Repeat as Needed

Most movement systems require multiple actions.

Example:

```text
move_left
move_right
move_forward
move_backward
```

Each action should receive one or more inputs.

---

## Success Check

You should now have:

✓ A named action

✓ One or more assigned inputs

✓ An entry in the Input Map

Example:

```text
move_left
└── A

move_right
└── D

jump
└── Space
```

---

## Common Examples

### Basic WASD Movement

```text
move_left
└── A

move_right
└── D

move_forward
└── W

move_backward
└── S
```

---

### Platformer Controls

```text
move_left
└── A

move_right
└── D

jump
└── Space
```

---

### First Person Controls

```text
move_forward
└── W

move_backward
└── S

move_left
└── A

move_right
└── D

interact
└── E
```

---

## Common Mistakes

### Mistake 1

Using different action names in code and Input Map.

Example:

Input Map:

```text
move_left
```

Code:

```gdscript
Input.is_action_pressed("left")
```

Result:

The input never works.

Solution:

Action names must match exactly.

---

### Mistake 2

Adding actions but forgetting to assign inputs.

Result:

The action exists but cannot be triggered.

Solution:

Verify each action has at least one input event.

---

### Mistake 3

Using spaces in action names.

Example:

```text
Move Left
```

Result:

Inconsistent naming and harder-to-read code.

Solution:

Use:

```text
move_left
```

instead.

---

### Mistake 4

Checking physical keys directly.

Example:

```gdscript
KEY_W
```

Result:

Less flexible code.

Solution:

Use Input Actions whenever possible.

---

### Mistake 5

Creating too many actions.

Example:

```text
move_forward_fast
move_forward_slow
move_forward_medium
```

Result:

Complex and difficult-to-maintain projects.

Solution:

Keep actions focused and meaningful.

---

## Why This Matters

Input Mapping separates:

### Physical Input

What the player presses.

Examples:

```text
W
Space
Left Mouse Button
Gamepad A
```

---

### Intent

What the player wants to do.

Examples:

```text
move_forward
jump
shoot
interact
```

This separation makes projects easier to maintain and expand.

---

## Design Insight

Imagine you decide later that:

```text
Jump = Space
```

should become:

```text
Jump = J
```

If you use Input Mapping:

Only the Input Map changes.

The code remains identical.

This is one of the major reasons game engines use action systems.

---

## Professional Practice

Most professional projects define all major player actions before significant gameplay programming begins.

Examples:

```text
move_left
move_right
move_forward
move_backward
jump
shoot
reload
interact
pause
inventory
```

This creates a common language between designers and programmers.

Rather than saying:

> "Press W"

developers think:

> "Trigger move_forward"

---

## Relationship to Scripting

Input Maps become most useful when combined with code.

Example:

```gdscript
if Input.is_action_pressed("move_forward"):
    velocity.z -= speed
```

Notice that the code never references a keyboard key directly.

The action acts as an intermediary.

---

## Related Operations

* 0.2.0 Create Script
* 0.2.1 Attach Script
* 0.2.2 Run Scene
* 0.2.4 Print Debug Information
* 0.4.1 Configure Project Settings

---

## Related Techniques

This operation supports the following techniques:

* Input Handling
* Character Movement
* User Interaction
* Controller Support
* Event-Driven Design