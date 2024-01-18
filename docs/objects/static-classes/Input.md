---
title: Input
description: Input is a class used for retrieving user input data, such as the mouse and keyboard.
icon: polytoria/Input
---

# Input

{{ staticclass("Input")}}

:polytoria-Input: Input is a class used for retrieving user input data, such as the mouse and keyboard.

## Events

### KeyDown:string { event }

Fires when a key is pressed.

**Example**

```lua
Input.KeyDown:Connect(function (key)
    print(key .. " was pressed!")

    if key == "P" then
        print("The 'P' key was pressed!")
    end
end)
```

### KeyUp:string { event }

Fires when a key is released.

```lua
Input.KeyUp:Connect(function (key)
    print(key .. " was pressed!")

    if key == "P" then
        print("The 'P' key was pressed!")
    end
end)
```

## Methods

### GetMouseWorldPoint { method }

### GetMouseWorldPosition { method }

### ScreenPointToRay { method }

### ScreenToViewportPoint(screenPosition;Vector3):Vector3 { method }

Transforms `screenPosition` parameter from screen space into viewport space.

### ScreenToWorldPoint(screenPosition;Vector3):Vector3 { method }

Transforms `screenPosition` from screen space into world space.

!!! note "World space coordinates can still be calculated even when provided as an off-screen coordinate."

### ViewportPointToRay { method }

TO-DO

### ViewportToScreenPoint(viewportPosition;Vector3):Vector3 { method }

Transforms `viewportPosition` from viewport space into screen space.

### ViewportToWorldPoint(viewportPosition;Vector3):Vector3 { method }

Transforms `viewportPosition` from viewport space into world space.

!!! note "ViewportToWorldPoint transforms an x-y screen position into a x-y-z position in 3D space."

### WorldToScreenPoint(worldPosition;Vector3):Vector3 { method }

Transforms `worldPosition` from world space into screen space.

### WorldToViewportPoint(worldPosition;Vector3):Vector3 { method }

Transforms `worldPosition` from world space into viewport space.

## Properties

### MousePosition:Vector2 { property }

Returns the current mouse position.
