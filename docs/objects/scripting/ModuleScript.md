---
icon: polytoria/ModuleScript
weight: 2
---

# ModuleScript

:polytoria-ModuleScript: ModuleScripts are a kind of script, that is specialized to hold data that can be accessed by other scripts using the `require()` function.

!!! failure "BETA Feature"
    ModuleScripts are currently in BETA. As of right now, you aren't able to run functions from ModuleScripts. However this is a planned feature in the near future.

It is important to define and return a table in a ModuleScript. When the game starts, the server and the client will run the ModuleScript once and store the result for other scripts to retrieve with `require()`.

{{ inherits("BaseScript") }}

**Example**

ModuleScript named `Structures` located in `game["ScriptService"]`

```lua
local Structures = {
    ["Tower"] = {
        ["Description"] = "This tower will obliterate any enemies on the way to the castle!",
        ["Price"] = 95,
        ["AttackDamage"] = 5
    }
}

-- Make sure to return the table to be able to access it in other scripts!
return Structures
```

In a Script/LocalScript:

```lua
wait(0.1) -- The ModuleScript might only start running after this Script/LocalScript began running and thus this wait() is necessary
local Structures = require(game["ScriptService"]["Structures"])

print(Structures["Tower"]["Description"]) -- Prints out "This tower will obliterate any enemies on the way to the castle!" like how it was defined in the ModuleScript above.
```
