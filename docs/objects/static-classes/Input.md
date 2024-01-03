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
