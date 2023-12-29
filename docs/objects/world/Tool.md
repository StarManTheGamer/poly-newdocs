---
icon: polytoria/Tool
weight: 7
---

# Tool

Tools are objects that can be held by players.

{{ inherits("Instance") }}

## Events

### Activated { event }

Gets fired when the user clicks while holding the tool.

**Example**

```lua
tool.Activated:Connect(function()
    print("Tool has been activated!")
end)
```

## Methods

### Play:void { method }

Plays an animation on the tool or the player that is currently holding the tool.

<div data-search-exclude markdown>
!!! tip "You can use the following emotes on these tools: `slash`, `eat`, and `drink`."
</div>

## Properties

### Droppable:bool { property }

Determines whether the tool can be dropped by the player or not.
