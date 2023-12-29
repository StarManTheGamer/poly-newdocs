---
icon: polytoria/Instance
weight: 100
---

# Instance

{{ notnewable() }}

Instance is the base class of all classes. Every class derives from it and has all properties, events and functions Instance has.

{{ abstract() }}

## Properties

### CanReparent:bool { property }

Returns whether this instance can be reparented/deleted or not.

### ClassName:string { property }

Returns the name of the class.

### Item:Instance { property }

Specifies the name of an instance.

### Name:string { property }

Specifies the name of an instance.

### Parent:Instance { property }

Specifies the parent instance of an instance.

### Shared:Table { property }

An empty table you can use to hold metadata about anything on any object or player you want.

!!! note "Doesn't sync from the client to the server, or from the server to the client."

**Example**

```lua
-- Script 1
local players = game.Players.GetChildren()
local lucky = players[math.random(1, #players)]

lucky.Shared.IsZombie = true

-- Script 2
local killBrick = game.Environment["Kill Brick"]

killBrick.Touched:Connect(function(hit)
    if hit.IsA("Player") then
        if hit.Shared.IsZombie then
            print("YOU CAN'T KILL ME, I'M ALREADY DEAD!")
        else
            hit.Health = 0
        end
    end
end
```
