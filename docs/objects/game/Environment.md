---
icon: polytoria/Environment
weight: 2
---

# Environment

{{ service() }}

{{ notnewable() }}

{{ inherits("Instance") }}

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

### FogStartDistance:number { property }
The distance from the camera at which fog starts to appear

### FogEndDistance:number { property }
The distance from the camera at which fog is fully opaque

### Gravity:Vector3=Vector3.New(0, -75, 0) { property }
The direction and strength of gravity in the world

### Skybox:SkyboxPreset { property }
The default skybox preset to use for the world, if no ImageSky is present.