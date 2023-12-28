---
icon: polytoria/NPC
weight: 5

---

# NPC

An NPC (Non-Player Character) is an object similar to a Player but that can be controlled by code. Like players, it can walk and jump, and it's body part colors can be customized.

{{ inherits("DynamicInstance") }}

## Properties

### Anchored:bool { property }
Determines whether this NPC is affected by physics or not.

### Grounded:bool { property }
Returns true if the NPC is currently standing on the ground.

### HeadColor:Color { property }
Specifies the color of an NPC's head.

### Health:number { property }
Specifies the current amount of health an NPC has.

### LeftArmColor:Color { property }
Specifies the color of an NPC's left arm.

### LeftLegColor:Color { property }
Specifies the color of an NPC's left leg.

### MaxHealth:number { property }
Specifies the maximum amount of health a NPC can have.

### MoveTarget:Instance { property }
Determines the position the NPC should walk towards.

### RightArmColor:Color { property }
Specifies the color of an NPC's right arm.

### RightLegColor:Color { property }
Specifies the color of an NPC's right leg.

### TorsoColor:Color { property }
Specifies the color of an NPC's torso.