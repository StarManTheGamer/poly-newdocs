---
icon: polytoria/PlayerDefaults
weight: 6
---

# PlayerDefaults

{{ service() }}

{{ notnewable() }}

:polytoria-PlayerDefaults: PlayerDefaults is a service used for storing the default values of the :polytoria-Player: Player when created.

{{ inherits("Instance") }}

## Properties
### ChatColor:Color { property }
Determines the default color of players' usernames in chat.

### JumpPower:int { property }
Determines how high the player jumps by default.

### MaxHealth:int { property }
Determines the default maximum health of players.

### MaxStamina:int { property }
Determines the default maximum stamina of players.

### RespawnTime:int { property }
Determines the default of how long it takes between player's death and respawn.

### SprintSpeed:int { property }
Determines the default sprint speed of players.

### Stamina:int { property }
Determines the default stamina of players.

### StaminaEnabled:bool { property }
Determines whether or not stamina is enabled by default for players.

### StaminaRegen:int { property }
Determines the default rate at which stamina regenerates after being depleted for players.

### WalkSpeed:int=16 { property }
Determines how fast the player walks by default.

## Methods
### LoadDefaults:Player { method }
Resets the specified player back to their default values.