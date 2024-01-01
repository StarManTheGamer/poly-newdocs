---
icon: polytoria/UIButton
weight: 100
---

# UIButton

{{ inherits("UILabel") }}

## Events

### Clicked:void { event }

Fires when the UIButton is clicked

**Example**
```lua
script.Parent.Clicked:Connect(function ()
    print("The button was clicked!")
end)
```