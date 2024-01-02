---
icon: polytoria/UI
---

# (Deprecated) UI

<div data-search-exclude markdown>
!!! danger "Deprecated"
    The UI static class was removed in Version 1.2.0, and is currently noted for documentation purposes.
</div>

{{ staticclass("UI")}}

UI is a static class used for creating User Interface elements through LocalScripts. While it is possible to create UI elements in normal scripts, it will only work in local playtesting and not on server.

## Methods

### CreateButton:UIButton { method }

Creates a GUI Button

### CreateEmpty:UIField { method }

Creates an empty UIField

### CreateImage:UIImage { method }

Creates an UI image.

### CreateLabel(text;string):UILabel { method }

Creates a text label.

### CreateHorizontalLayout:UIHorizontalLayout { method }

Creates a horizontal UI layout.

### CreateVerticalLayout:UIVerticalLayout { method }

Creates a horizontal UI layout.

## Properties

### ScreenHeight:int { property }

Get current user's screen height

### ScreenWidth:int { property }

Get current user's screen width
