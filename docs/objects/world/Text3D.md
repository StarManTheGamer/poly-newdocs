---
title: Text3D
description: Text3D allows placement of text in the world.
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

### FontSize:int { property }

Specifies the size of the font.

### HorizontalAlignment:HorizontalAlignment { property }

Specifies the horizontal alignment of the text.

### Text:string { property }

Specifies the text to display.

### VerticalAlignment:VerticalAlignment { property }

Specifies the vertical alignment of the text.
