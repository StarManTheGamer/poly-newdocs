---
icon: polytoria/Decal
---

# Decal

Decals are objects that can have an image texture and are placed in the world.

{{ inherits("DynamicInstance") }}

## Properties

### ImageType:ImageType { property }

The type of image to be used.

### ImageID:int { property }

Specifies the image asset ID of the decal.

**Example**

```lua
game["Environment"]["Decal"].ImageID = 11643
```
