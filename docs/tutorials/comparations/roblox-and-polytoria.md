---
title: Comparing Roblox and Polytoria
description: Main difference between Polytoria and Roblox in the matters of programming
---

# Accessing objects

In Polytoria when finding objects, we use brackets([]) instead of dots(.).

Example:

Polytoria:
```lua
game['Envieronment']['Part']```

Roblox:

```lua
game.Workspace.Part```

# Callback Method

In Polytoria we use the Callback Method instead of the usual :Wait() or yield. 
Example: When you are calling services, in Roblox you need to wait until it's finished. In Polytoria you have to put the function in Callback, what's that? Here's an exaple:

Polytoria:
```lua
Tween:TweenPosition(part, Vector3.New(0, 10, 20), 100, TweenType.linear, function()
print("I have arrived!")
end)```
Roblox:
```lua
local tween1 = TweenService:Create(part, tweenInfo, {Position = Vector3.new(0, 10, 20)})
tween:Play()
tween.Completed:Wait()
print("I have arrived!")```

# Enums have names

In Roblox you do Enum.XYZ, in Polytoria we use it's name, Example:

Roblox: 
```lua
Enum.EasingStyle.Exponential```
Polytoria:
```lua
TweenType.easeOutExpo```

# Input.KeyDown does not gave you interrupt state.

In Roblox, We mostly use UserInputService.InputBegan method to see if the key are pressed or not, it returns the key that is being pressed. In Polytoria the event will not put you on interrupt state

# Static Classes instead of Services

In Roblox we get the services using game.GetService("ServiceName"), in Polytoria, there will be static classes for every service. 

<strong>Note:</strong>
You don't have to get and store it in variable, But be careful that don't name the variable same as static classes name.

Roblox:
```lua
local tweenService = game:GetService("TweenService")```
Polytoria:
```lua
local tweenService = Tween```

# Conclusion

It has some differences, and you might not copy and paste your roblox scripts, but it's pretty easy to learn, because still the same Programming Language, [Lua](https://lua.org).

Any questions? Come and talk to us on out official [DevHub server](https://discord.gg/sqVSKZRpdB)!
<strong>Note:</strong>
You have to be 13 or older to join this discord server.