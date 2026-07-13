# Technique 3.7 — Connect Using Signals

## Classification

**Type:** Engineering Technique

**Category:** Heads-Up Display (HUD)

**Difficulty:** Beginner

**Estimated Time:** 25–30 minutes

---

# Design Scenario

Your interface looks complete.

You have:

- a score display
- a health bar
- a timer

But there is a problem.

The score never changes.

The health bar never moves.

The timer never updates.

The interface exists...

…but it doesn't know when the game changes.

To solve this problem, different parts of the game must communicate with one another.

Godot provides a built-in communication system called **Signals**.

---

# Why This Technique Matters

Games consist of many independent systems.

For example:

- the player collects a coin
- the score increases
- the score display updates

Notice that three different parts of the game are involved.

Rather than constantly checking whether something has changed, Godot allows one object to **announce** that an event has occurred.

Other objects can choose to listen.

This keeps different parts of the game independent while still allowing them to work together.

---

# Mental Model

Imagine a school bell.

When the bell rings, it doesn't tell every student exactly what to do.

It simply announces:

> "Something happened."

Students who care about the bell respond.

Teachers respond.

Administrators respond.

Visitors may ignore it entirely.

A signal works the same way.

One object broadcasts an event.

Any interested object can react.

---

# Starter Implementation

Create a simple Button.

```text
CanvasLayer
└── Control
    └── Button
```

Double-click the Button.

Navigate to the **Node** tab.

Notice the list of available signals.

Connect the **pressed()** signal to a script.

Inside the generated function:

```gdscript
func _on_button_pressed():
    print("Button pressed!")
```

Run the project.

Press the button.

Observe the Output panel.

The Button announced an event.

The script responded.

---

# Anatomy

## Signal

A notification that an event has occurred.

Examples include:

- button pressed
- timer finished
- body entered
- animation completed

---

## Emitter

The object that sends the signal.

For example:

A Button emits the **pressed()** signal.

---

## Receiver

The object that listens for the signal.

When the signal arrives, the connected function executes.

---

## Connection

The relationship between the emitter and the receiver.

Without a connection, the signal is simply ignored.

---

# Design Principle

## Announce events instead of asking continuously.

Imagine checking every second whether someone has knocked on your front door.

Instead...

The visitor simply rings the doorbell.

Signals eliminate unnecessary checking.

Objects communicate only when something important actually happens.

This makes programs easier to understand and often more efficient.

---

# Experiment

Only change one thing at a time.

---

### Experiment A

Connect the Button's **pressed()** signal.

Print a message.

Observe.

When does the function execute?

---

### Experiment B

Connect the same signal.

This time, change the Label's text instead of printing.

Observe.

The interface now reacts to player input.

---

### Experiment C

Disconnect the signal.

Run the project again.

Observe.

What changed?

---

### Experiment D

Connect multiple Buttons.

Give each one a different message.

Observe how each signal triggers a different response.

---

### Experiment E

Connect one Button to update several interface elements.

Observe.

One event can notify multiple listeners.

---

# Practical Observation

Signals are used throughout Godot.

Common examples include:

- buttons being clicked
- timers completing
- players entering trigger areas
- enemies being defeated
- animations finishing
- health changing
- inventory updates

As projects grow larger, Signals become one of the primary ways different systems communicate.

---

# Common Misconceptions

### "Signals are only for buttons."

No.

Nearly every major node in Godot emits signals.

Buttons are simply one of the easiest examples.

---

### "Signals move information."

Not exactly.

Signals announce that something happened.

If information needs to be shared, it can be sent along with the signal.

---

### "Signals create dependencies."

Usually the opposite.

Signals allow objects to communicate without tightly depending on one another.

The emitter often doesn't even know who is listening.

---

# Reflection

Complete the sentence.

> A signal announces...

Complete the sentence.

> The receiver...

Now answer:

Why might announcing an event be better than constantly checking whether something has changed?

---

# Self Check

Before moving on, ask yourself:

✓ I understand what a signal represents.

✓ I can connect a signal to a function.

✓ I know the difference between the object sending a signal and the object receiving it.

✓ I understand that signals help different parts of the game communicate.

---

# Looking Ahead

Signals allow objects to communicate.

The next question becomes:

> **What information should the interface display?**

We'll begin with **Labels**, which update dynamically to communicate scores, timers, player names, objectives, and many other pieces of information.