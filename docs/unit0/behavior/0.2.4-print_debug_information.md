# Operation 0.2.4 — Print Debug Information

## Classification

**Type:** Operation
**Category:** Behavior Operations
**Difficulty:** Beginner
**Estimated Time:** 30 seconds

---

## Purpose

Printing debug information allows you to display information in Godot's **Output** panel while a scene or project is running.

This is one of the most important debugging tools available to developers.

Debug output helps answer questions such as:

* Is this code running?
* What value does this variable contain?
* Did the player collide with the object?
* Is the function being called?
* Why isn't this system behaving correctly?

When something unexpected happens, printing information is often the fastest way to understand what the game is doing.

---

## When Would I Use This?

Use this operation whenever you need visibility into what your code is doing.

Examples:

* Verify player input is being detected
* Check a variable's value
* Confirm a collision occurred
* Track an object's position
* Test whether a function is being called
* Observe state changes

A useful rule is:

> If you are guessing, print information.

---

## Prerequisites

Before beginning:

* A script exists
* The script is attached to a node
* The scene can be run

---

## Procedure

### Step 1 — Open a Script

Open the script where you want to observe behavior.

Example:

```gdscript
extends CharacterBody3D
```

---

### Step 2 — Add a Print Statement

Use the `print()` function.

Example:

```gdscript
print("Hello World")
```

---

### Step 3 — Run the Scene or Project

Press:

```text
F6
```

or

```text
F5
```

depending on what you are testing.

---

### Step 4 — Observe the Output Panel

Look at the bottom of the Godot editor.

You should see:

```text
Hello World
```

appear in the Output window.

---

## Success Check

You should now have:

✓ A print statement in your code

✓ Output appearing in the Output panel

✓ Visibility into your program's behavior

---

## Common Examples

### Printing Text

```gdscript
print("Player spawned")
```

Output:

```text
Player spawned
```

---

### Printing a Variable

```gdscript
var health = 100

print(health)
```

Output:

```text
100
```

---

### Printing a Label and a Variable

```gdscript
var score = 250

print("Score:", score)
```

Output:

```text
Score: 250
```

---

### Printing Position Information

```gdscript
print(position)
```

Output:

```text
(3.4, 1.0, -2.1)
```

---

### Printing During Input

```gdscript
if Input.is_action_just_pressed("jump"):
    print("Jump!")
```

Output:

```text
Jump!
```

every time the player presses jump.

---

## Common Mistakes

### Mistake 1

Adding print statements but never running the project.

Result:

No output appears.

Solution:

Remember that print statements only execute when the code runs.

---

### Mistake 2

Looking in the wrong panel.

Result:

Students assume printing is broken.

Solution:

Check the Output panel at the bottom of the editor.

---

### Mistake 3

Printing too much information.

Example:

```gdscript
func _process(delta):
    print(position)
```

Result:

Thousands of lines appear every second.

Solution:

Print strategically.

---

### Mistake 4

Removing print statements too late.

Result:

Output becomes cluttered and difficult to read.

Solution:

Delete or comment out debug prints once they are no longer needed.

---

### Mistake 5

Trying to solve every problem without debugging.

Result:

Students spend excessive time guessing.

Solution:

Use print statements to gather evidence before making changes.

---

## Why This Matters

Programming is difficult because we cannot directly see what the computer is thinking.

Print statements create windows into the program's internal state.

Without debugging:

```text
Something is wrong.
```

With debugging:

```text
The position is incorrect.
The collision never happened.
The function was never called.
```

The problem becomes much easier to solve.

---

## Design Insight

Many beginning programmers approach debugging like this:

```text
Observe Bug
↓
Guess
↓
Change Code
↓
Hope
```

Experienced programmers tend to follow a different process:

```text
Observe Bug
↓
Gather Evidence
↓
Print Information
↓
Understand Cause
↓
Fix Problem
```

Print statements are one of the simplest ways to gather evidence.

---

## Professional Practice

Professional developers use debugging constantly.

Even experienced programmers regularly write:

```gdscript
print()
```

to understand behavior.

A common saying among programmers is:

> The computer is doing exactly what you told it to do.
>
> Your job is figuring out what you actually told it to do.

Debug output helps reveal that difference.

---

## Beyond Print

As projects become larger, developers often use additional debugging tools:

* Breakpoints
* Debugger panels
* Watches
* Profilers
* Logging systems

However, `print()` remains one of the fastest and most useful debugging techniques.

Many complex bugs can be solved with a few well-placed print statements.

---

## Related Operations

* 0.2.0 Create Script
* 0.2.1 Attach Script
* 0.2.2 Run Scene
* 0.2.3 Run Project
* 0.2.5 Read Error Messages

---

## Related Techniques

This operation supports the following techniques:

* Debugging
* Testing
* State Inspection
* Problem Solving
* Iterative Development