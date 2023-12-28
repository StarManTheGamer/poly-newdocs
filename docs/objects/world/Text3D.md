---
icon: polytoria/Text3D
weight: 4

---

# Text3D

Text3D allows placement of text in the world.

{{ inherits("DynamicInstance") }}

## Properties

### Color:Color { property }
Specifies the color of the text.

**Example**
```lua
text.Color = Color.Random()
```

### FaceCamera:bool { property }
Specifies whether the text should always be facing the camera or not.

**Example**
```lua
text.FaceCamera = true
```

### FontSize:number { property }
Specifies the size of the font.

**Example**
```lua
text.FontSize = 64
```
