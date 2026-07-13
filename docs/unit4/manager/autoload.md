# 4.2.2 Configure an Autoload

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 15–20 minutes

---

# Design Problem

In the previous lesson, we created a Game Manager.

Unfortunately, it has one major limitation.

Like every other scene in Godot, it only exists when that scene is loaded.

If another scene is loaded...

...the Game Manager disappears.

That makes it a poor place to store information that should persist throughout the game.

We need a way for one object to exist for the entire lifetime of the application.

Godot provides this using **Autoloads**.

---

# Why This Technique Matters

An Autoload is created automatically when the game starts.

Unlike ordinary scenes, it is not tied to a particular level or screen.

Instead, it exists for the entire game.

This makes it an ideal place for information such as:

- player score
- current level
- game settings
- pause state
- unlocked achievements

An Autoload allows one object to be shared by every scene.

---

# Starter Implementation

Begin with the **GameManager** scene you created previously.

Open:

```text
Project
    ↓
Project Settings
        ↓
Globals
            ↓
Autoload
```

Select your GameManager scene.

Choose a name.

```text
GameManager
```

Then press:

```text
Add
```

Your Game Manager is now automatically created whenever the game starts.

---

# Verify the Result

Run your project.

Even though no scene explicitly creates the Game Manager...

...it already exists.

Every scene in your project can now access the same object.

---

# Dissecting the Technique

Normally, scenes are created when another scene instantiates them.

```text
Level
    ↓
Creates
    ↓
Enemy
```

An Autoload works differently.

Godot creates it automatically before your game begins.

```text
Game Starts

↓

GameManager Created

↓

Main Menu

↓

Level 1

↓

Level 2

↓

Credits

↓

Game Ends
```

The Game Manager exists throughout the entire process.

---

# Design Principle

## Global information needs a global lifetime.

If information should survive changing scenes, the object that owns it must also survive changing scenes.

An Autoload provides that persistent owner.

---

# Experiment

Suppose your game has three scenes.

```text
Main Menu

↓

Level 1

↓

Level 2
```

Ask yourself:

Should these values survive when moving between scenes?

| Information | Should it Persist? |
|--------------|--------------------|
| Current Score | ✓ |
| Player Lives | ✓ |
| Difficulty Setting | ✓ |
| Current Volume | ✓ |
| Enemy Health | ✗ |
| Door Open | ✗ (Usually) |

Which information belongs in the Game Manager?

Which belongs inside each individual level?

---

# Practical Observation

Autoloads are powerful because they can be accessed from anywhere.

That convenience also requires discipline.

Just because an object *can* store something doesn't mean it *should.*

A Game Manager should own only information that truly belongs to the game as a whole.

Keeping global objects focused on a clear responsibility makes projects easier to maintain.

---

# Common Misconceptions

### "Autoloads replace every other object."

No.

Most objects still belong inside individual scenes.

Autoloads solve a very specific problem: managing information that should exist throughout the game.

---

### "Everything should become global."

Usually not.

Global information is shared because many systems need it.

Most gameplay information still belongs to the individual objects that own it.

---

### "Autoloads are only for Game Managers."

No.

Any scene or script can be configured as an Autoload.

The Game Manager is simply one of the most common examples.

---

### "Changing scenes deletes the Autoload."

No.

Autoloads continue to exist until the game closes.

That persistence is what makes them useful for global state.

---

# Reflection

Think about a game you've played.

Which pieces of information should survive when changing from one level to another?

Which pieces should disappear because they belong only to that level?

Now consider your own projects.

Can you identify three variables that would make sense inside a Game Manager?

---

# Looking Ahead

Now that the Game Manager exists for the lifetime of the game, it's finally ready to do its job.

The next step is to begin storing information inside it.

> **How do we create and manage global variables?**