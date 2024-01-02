---
icon: polytoria/UITextInput
weight: 100
---

# UITextInput

:polytoria-UITextInput: UITextInput is a class that allows the user to enter text.

{{ inherits("UIView") }}

## Properties

### AutoSize:bool { property }

Whether the text should be automatically sized to fit the label's size.

### Font:TextFontPreset { property }

The font of the label.

### FontSize:int { property }

The font size of the label.

### IsMultiline:bool { property }

Set if the text input can be multiline.

### IsReadOnly:bool { property }

Set if the text input can be edited or not.

### JustifyText:TextJustify { property }

Determines how the text is justified.

### MaxFontSize:int { property }

The maximum font size of the UI element if AutoSize is set to true.

### Placeholder:string { property }

The placeholder of the text input.

### PlaceholderColor:Color { property }

The color of the placeholder text.

**Example**

```lua
element.PlaceholderColor = Color.New(0, 0, 0, 0.5)
```

### Text:string { property }

The text of the label.

### TextColor:Color { property }

The color of the text.

### VerticalAlign:TextVerticalAlign { property }

The vertical alignment of the text.
