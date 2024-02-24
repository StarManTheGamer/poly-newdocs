---
title: Environment
description: Environment is the primary object intended for storing active objects in the place.
icon: polytoria/Environment
weight: 2
---

# Environment

{{ service() }}

{{ notnewable() }}

:polytoria-Environment: Environment is the primary object intended for storing active objects in the place.

{{ inherits("Instance") }}

## Methods

### CreateExplosion(Position;Vector3,Radius;int=10,Force;int=5000,affectAnchored;bool=true,callback;function=nil) { method }

Creates a deadly explosion killing players and applying force to parts at the given position.

**Example**

```lua
game["Environment"]:CreateExplosion(Vector3.New(0, 0, 0), 30, 5000, false)
```

<div data-search-exclude markdown>
!!! note "When set to true, AffectAnchored will unanchor parts within the explosion radius."
</div>

<div data-search-exclude markdown>
!!! note "Callback gets called for each part within explosion radius."
</div>

### Raycast(origin;Vector3,direction;Vector3,maxDistance;int=infinite,ignoreList;array=Instance[]):RayResult { method }

Casts a ray from origin with a specified direction and returns a RayResult for the first hit object.

**Example**

```lua
local hit = game["Environment"]:Raycast(barrel.Position, barrel.Forward)

if hit and hit.Instance:IsA("Player") then
    hit.Instance.Health = 0
end
```

### RaycastAll(origin;Vector3,direction;Vector3,maxDistance;int=infinite,ignoreList;array=Instance[]):RayResult { method }

Casts a ray from origin with a specified direction and returns a RayResult array for all hit objects.

**Example**

```lua
local hits = game["Environment"]:RaycastAll(Vector3.New(0, 10, 0), Vector3.New(0, -1, 0), 100)

for i, hit in pairs(hits) do
    print("Hit at " .. hit.Position .. "!")
end
```

## Properties

### FogColor:Color { property }

The color of the fog. Fog is a visual effect that makes the world look like it is covered in a colored mist.

**Example**

Change the fog color to white:

```lua
game["Environment"].FogColor = Color.New(1, 1, 1, 1)
```

### FogEnabled:boolean { property }

Whether or not fog is enabled.

### FogStartDistance:float { property }

The distance from the camera at which fog starts to appear

### FogEndDistance:float { property }

The distance from the camera at which fog is fully opaque

### Gravity:Vector3=Vector3.New(0, -75, 0) { property }

The direction and strength of gravity in the world

### PartDestroyHeight:int { property }

The height at which unanchored parts are destroyed when they fall below it.

**Example**

```lua
game["Environment"].PartDestroyHeight = -2000
```

### Skybox:SkyboxPreset { property }

The default skybox preset to use for the world, if no ImageSky is present.
