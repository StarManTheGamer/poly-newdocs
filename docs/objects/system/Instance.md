---
title: Instance
description: Instance is the base class of all classes. Every class derives from it and has all properties, events and functions Instance has.
icon: polytoria/Instance
weight: 100
---

# Instance

{{ notnewable() }}

:polytoria-Instance: Instance is the base class of all classes. Every class derives from it and has all properties, events and functions Instance has.

{{ abstract() }}

## Events

### ChildAdded:Instance { event }
Fires when a child instance is added.

### ChildRemoved:Instance { event }
Fires when a child instance is removed.

### Clicked:Player { event }
Fires when the instance is clicked by a player.

### MouseEnter { event }
Fires when the mouse enters the instance.

### MouseExit { event }
Fires when the mouse enters the instance.

### Touched:Instance { event }
Fires when the instance was touched by another instance.

!!! note "There must be an active collider on the instance for this event to trigger ({{ classLink("Part") }}, {{ classLink("Player") }}, etc.)"

### TouchEnded { event }
Fires when the instance is no longer being touched by another instance.

!!! note "There must be an active collider on the instance for this event to trigger ({{ classLink("Part") }}, {{ classLink("Player") }}, etc.)"

## Methods

### New

### Clone { method }
Clones the instance

### Destroy { method }
Destroys the instance (same as Delete method)

### Delete { method }
Deletes the instance (same as Destroy method)

### GetParent:Instance { method }
Returns the parent of the instance (same as accessing the `.Parent` property).

### SetParent(newParent;Instance)
Sets the parent of the instance (same as setting the `.Parent` property)

### IsA(className;string):bool { method }
Returns whether or not the instance is the specified class.

### IsDescendantOf(other;Instance):bool { method }
Returns whether or not the instance is a descendant (child, child of child, etc) of the specified instance.

### FindChild(name;string):Instance { method }
Attempts to find the first child instance with the specified name (`nil` if not found).

### FindChildByClass(className;string):Instance { method }
Attempts to find the first child instance with the specified class (`nil` if not found).

### GetChildren:Instance[] { method }
Returns an array of all the children instances parented to the instance.

### GetChildrenOfClass(className;string):Instance[] { method }
Returns an array of all the children instances with the specified class.

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

### Shared:array { property }

An empty table you can use to hold metadata about anything on any object or player you want.

!!! note "Shared doesn't sync from the client to the server, or from the server to the client."

**Example**

```lua
-- Script 1
local players = game.Players.GetChildren()
local lucky = players[math.random(1, #players)]

lucky.Shared.IsZombie = true
```

```lua
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
