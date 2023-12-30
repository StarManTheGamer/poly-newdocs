---
icon: polytoria/ModuleScript
weight: 2
---

# ModuleScript

:polytoria-ModuleScript: ModuleScripts are a kind of script, that is specialized to hold data inside a table. In the future, they may support functions as well.

It is important to define and return a table in a ModuleScript. When the game starts, the server and the client will run the ModuleScript once and store the result for other scripts to retrieve with `require()`.

{{ inherits("BaseScript") }}

Example:

ModuleScript named `Structures` located in `game["ScriptService"]`
```lua
local Structures = {
    ["Tower"] = {
        ["Description"] = "This tower will obliterate any enemies on the way to the castle!",
        ["Price"] = 95,
        ["AttackDamage"] = 5
    }
}

return Structures -- THIS IS IMPORTANT! DO NOT FORGET TO RETURN THE TABLE AT THE END!
```

In a Script/LocalScript:
```lua
wait(0.1) -- The ModuleScript might only start running after this Script/LocalScript began running and thus this wait() is necessary
local Structures = require(game["ScriptService"]["Structures"])

print(Structures["Tower"]["Description"]) -- Prints out "This tower will obliterate any enemies on the way to the castle!" like how it was defined in the ModuleScript above.
```