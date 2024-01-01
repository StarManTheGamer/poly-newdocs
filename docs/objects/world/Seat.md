---
icon: polytoria/Seat
weight: 3
---

# Seat

Seats are parts the player can sit on.

{{ inherits("Part") }}

## Events

### Sat:Player { event }
This event fires when a player sits in the seat.

### Vacated:Player { event }
This event fires when a player leaves the seat.

## Properties

### Occupant:Player { property }

The player that is currently sitting in this seat.

**Example**

```lua
seat.Occupant:Unsit()
```
