# 4.3.3 Send Data with Signals

## Classification

**Type:** Engineering Technique

**Category:** Game Architecture

**Difficulty:** Intermediate

**Estimated Time:** 20–30 minutes

---

# Design Problem

Sometimes announcing that an event happened is enough.

For example:

```text
Checkpoint Activated
```

But many events need additional information.

Imagine the player takes damage.

Should every object have to ask:

- How much damage?
- Who caused it?
- Where did it happen?

Instead, the event itself can include that information.

Signals can carry data along with the announcement.

---

# Why This Technique Matters

Signals become much more useful when they provide context.

Instead of simply announcing:

> "Something happened."

they can announce:

> "Something happened, and here's what you need to know."

This allows other systems to react immediately without searching for additional information.

---

# Starter Implementation

Suppose our player has a custom signal.

```gdscript
extends CharacterBody3D

signal health_changed(new_health)
```

The signal now expects one piece of information:

```text
new_health
```

Whenever the player's health changes, emit the signal.

```gdscript
func take_damage(amount):
	health -= amount

	health_changed.emit(health)
```

The event now communicates both:

- that health changed
- the player's new health value

---

# Dissecting the Code

When defining the signal:

```gdscript
signal health_changed(new_health)
```

the value inside the parentheses becomes information that travels with the signal.

Later:

```gdscript
health_changed.emit(health)
```

places the current value into that parameter.

Think of it like mailing a letter.

```text
Event

↓

Message

↓

Additional Information
```

Instead of saying:

> "Health changed."

the object announces:

> "Health changed to 75."

---

# Design Principle

## Events should communicate the information listeners need.

If every listener immediately has to ask for more information...

...the signal probably isn't carrying enough data.

Provide useful context whenever it makes communication simpler.

---

# Experiment

Imagine each object emits the following signal.

What information might it include?

| Signal | Possible Data |
|---------|---------------|
| `enemy_defeated` | enemy, points |
| `coin_collected` | coin_value |
| `door_opened` | door |
| `player_damaged` | remaining_health |
| `level_completed` | completion_time |

Different games may choose different information.

The goal is to send enough context for other systems to respond intelligently.

---

# Practical Observation

Not every signal needs data.

For example:

```gdscript
signal game_reset
```

already tells listeners everything they need to know.

Other events naturally require additional information.

For example:

```gdscript
signal score_changed(new_score)
```

or

```gdscript
signal item_collected(item_name)
```

Choosing the right amount of information is part of good software design.

---

# Common Misconceptions

### "Signals should send every variable."

No.

Send only the information listeners actually need.

Too much information makes events difficult to understand and maintain.

---

### "Signals replace game state."

No.

Signals communicate events.

Game state stores information.

Often a signal announces that state has changed.

---

### "Every listener must use every piece of data."

No.

Some listeners may use all of it.

Others may ignore part—or even all—of the information.

That's perfectly normal.

---

### "Sending data creates another copy of the game's state."

Not exactly.

The signal simply communicates information about the event.

The authoritative state should still belong to its proper owner.

---

# Reflection

Suppose your game contains the following events.

What information would be useful to include?

| Event | Information to Send |
|--------|---------------------|
| Player Died | |
| Enemy Defeated | |
| Coin Collected | |
| Checkpoint Activated | |
| Level Completed | |

Can you explain why each listener might need that information?

---

# Looking Ahead

Our objects can now announce meaningful events...

...and include useful information with those announcements.

The next challenge is receiving them.

> **How do we connect a signal to the code that should respond?**