---
icon: polytoria/Seat
weight: 3

---

# Seat

Seats are parts the player can sit on.

{{ inherits("Part") }}

## Properties

### Occupant:Player { property }
The player that is currently sitting in this seat.

**Example**
```lua
seat.Occupant:Unsit()
```