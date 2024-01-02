---
icon: polytoria/NPC
weight: 5
---

# NPC

An NPC (non-player character) is an object similar to a Player but that can be controlled by code. Like players, it can walk and jump, and it's body part colors can be customized.

{{ inherits("DynamicInstance") }}

## Events

### Died { event }

Fires when the NPC dies.

**Example**

```lua
game["Environment"]["NPC"].Died:Connect(function ()
    print("NPC died!")
end)
```

## Methods

### LoadAppearance(userID;int) { method }

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

## Properties

### Anchored:bool { property }

Determines whether the NPC is affected by physics or not.

### FaceID:int { property }

The face ID of the NPC's face.

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

### PantsID:int { property }

The pants ID of the NPC's pants.

### RightArmColor:Color { property }

Specifies the color of the NPC's right arm.

### RightLegColor:Color { property }

Specifies the color of the NPC's right leg.

### ShirtID:int { property }

The shirt ID of the NPC's shirt.

### TorsoColor:Color { property }

Specifies the color of the NPC's torso.

### WalkSpeed:int { property }

The walkspeed of the NPC.
