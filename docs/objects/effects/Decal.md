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

### TextureOffset:Vector2 { property }

The offset of the texture on the decal.

### TextureScale:Vector2 { property }

The scale of the texture on the decal.

**Example**

```lua
game["Environment"]["Decal"].ImageID = 11643
```
