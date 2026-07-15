# 6.7 Editor Automation

## Classification

**Type:** Engineering Technique

**Category:** Editor Automation

**Difficulty:** Intermediate

**Estimated Time:** 30–40 minutes

---

# Design Problem

Imagine building a level.

You repeatedly perform the same task.

Perhaps you need to:

- populate a TileMap
- place hundreds of trees
- create checkpoints
- rename nodes
- generate decorations

The work is repetitive.

Instead of repeating it yourself...

...could the editor do it for you?

Godot allows us to write scripts that run **inside the editor**.

These are called **Editor Scripts**.

---

# Why This Matters

Editor Scripts automate repetitive tasks.

Rather than modifying the running game...

...they modify your project while you are building it.

Examples include:

- generating TileMaps
- placing scenes automatically
- organizing nodes
- batch editing resources
- procedural level construction

The editor itself becomes programmable.

---

# Starter Implementation

Create a new script.

```gdscript
@tool
extends EditorScript
```

Inside the script:

```gdscript
@tool
extends EditorScript

func _run():

    print("Running inside the editor!")
```

Right-click the script.

Choose:

```text
Run
```

The script executes immediately inside the editor.

---

# Making Changes Visible

When an Editor Script creates or modifies nodes, Godot does not automatically mark the scene as changed.

To ensure your modifications appear correctly in the Scene Tree and can be saved, assign the edited scene as the current edited scene.

For example:

```gdscript
@tool
extends EditorScript

func _run():

    var root = get_scene()

    # Make changes...

    get_editor_interface().edit_node(root)
```

If you are creating an entirely new scene or replacing the edited root, explicitly assign it:

```gdscript
get_editor_interface().set_edited_scene_root(root)
```

This ensures the editor recognises the modified scene and updates the Scene Tree appropriately.

---

# Example

Suppose we have generated a Gridworld.

Our Editor Script might perform:

```text
Grid

↓

Read Cell

↓

Choose Tile

↓

Paint TileMap
```

The game has not started.

The editor simply builds the level for us.

When we press Play...

the generated level already exists.

---

# Dissecting the Workflow

Notice the difference.

A normal script affects:

```text
Running Game
```

An Editor Script affects:

```text
Project

↓

Scenes

↓

Resources

↓

TileMaps
```

The script becomes another development tool.

It helps build the game rather than becoming part of the game.

---

# Design Principle

## Automate repetitive work.

Whenever you find yourself repeating the same editing task many times...

ask yourself:

> **Could the editor perform this automatically?**

Good tools allow developers to spend more time designing and less time repeating mechanical work.

---

# Practical Observation

One of the most powerful uses of Editor Scripts in this course is generating TileMaps.

For example:

```text
Procedural Image

↓

Editor Script

↓

TileMapLayer

↓

Playable Level
```

Rather than painting thousands of tiles by hand...

the editor performs the work automatically.

The resulting TileMap can still be edited normally afterwards.

Automation becomes part of the creative workflow.

---

# Common Misconceptions

### "Editor Scripts run during gameplay."

No.

Editor Scripts execute inside the editor.

Their purpose is to help build the project.

---

### "Editor Scripts replace gameplay code."

Not at all.

Gameplay scripts control the running game.

Editor Scripts help create the game's resources before it runs.

---

### "Automation removes creativity."

Usually the opposite.

Automation removes repetitive work.

The designer remains free to experiment, iterate, and refine ideas much more quickly.

---

### "Only large projects benefit from Editor Scripts."

Even small projects often contain repetitive tasks.

Automating those tasks quickly becomes worthwhile.

---

# Reflection

Think about the work you've completed while building your platformer.

Which tasks did you repeat many times?

- placing decorations?
- populating TileMaps?
- creating checkpoints?
- renaming nodes?

Could one Editor Script perform those tasks automatically?

What new kinds of projects might become possible if the editor became another programmable tool?

---

# Unit Reflection

Throughout this unit we've built an interactive 2D game.

We learned how to:

- move characters
- create satisfying platforming
- communicate through animation
- construct TileMaps
- build gameplay objects
- present the world through the camera

Finally...

we learned that the editor itself can also be programmed.

Games are not built only by writing gameplay code.

Professional developers also build tools that help create games more efficiently.

The engine becomes more than a place to play the game.

It becomes a workbench for creating it.

---

# Looking Ahead

Our platformer now contains:

- movement
- interaction
- animation
- world construction
- gameplay systems
- automation

The next challenge is moving beyond platformers.

How do these same ideas apply to:

- top-down games
- procedural worlds
- larger game systems

We'll continue building upon the same principles in increasingly sophisticated projects.