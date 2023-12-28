---
icon: polytoria/NPC
weight: 5

---

# NPC

An NPC (Non-Player Character) is an object similar to a Player but that can be controlled by code. Like players, it can walk and jump, and it's body part colors can be customized.

{{ inherits("DynamicInstance") }}

## Properties

### Anchored:bool { property }
Determines whether the NPC is affected by physics or not.

### Grounded:bool { property }
Returns true if the NPC is currently standing on the ground.

### HeadColor:Color { property }
Specifies the color of the NPC's head.

### Health:int { property }
Specifies the current amount of health the NPC has.

### LeftArmColor:Color { property }
Specifies the color of the NPC's left arm.

### LeftLegColor:Color { property }
Specifies the color of the NPC's left leg.

### MaxHealth:int=100 { property }
Specifies the maximum amount of health a NPC can have.

### MoveTarget:Instance { property }
Determines the instance the NPC should walk towards.

### RightArmColor:Color { property }
Specifies the color of the NPC's right arm.

### RightLegColor:Color { property }
Specifies the color of the NPC's right leg.

### TorsoColor:Color { property }
Specifies the color of the NPC's torso.

## Methods
### LoadAppearance:int { method }
Loads the specified user ID's avatar on the NPC.

**Example**
```lua
-- Loads the appearance of willemsteller
npc:LoadAppearance(2)
```

### ClearAppearance { method }
Clears the NPC's appearance.

**Example**
```lua
-- Clears the appearance of the NPC
npc:ClearAppearance()
```