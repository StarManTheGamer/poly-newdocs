---
icon: polytoria/UIImage
weight: 100

---

# UIImage

{{ inherits("UIField") }}

## Properties

### Color:Color { property }
Specifies the color of the image.

### ImageID:Int32 { property }
Specifies the image ID of the UIImage.

### Loading:bool { property }
True if the image is loading.

**Example**

```lua
while image.Loading do
    wait(0)
end
print("Image loaded")
```

### Visible:bool { property }
Specifies if the image is visible.
