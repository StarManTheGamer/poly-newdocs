---
icon: polytoria/BaseScript
weight: 4

---

# BaseScript

{{ ambiguousMultiple([["Script", "which runs your Lua scripts on the server."],["LocalScript", "which runs your Lua scripts on the client."]]) }}

{{ abstract() }}

{{ inherits("Instance") }}

## Methods
### Call:void { property }
Calls a function on another script

**Example**
```lua
game["ScriptService"]["Script"]:Call("Foo", "Bar")
```

!!! warning "Local Functions"
    Local Functions cannot be ran using the Call function.