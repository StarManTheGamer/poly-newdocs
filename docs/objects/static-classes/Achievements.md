---
title: Achievements
description: Achivements is a static class, that is used to award place achivements to a player.
icon: polytoria/Achievements
---

# Achievements

{{ staticclass("Achievements") }}

{{ serverexclusive() }}

:polytoria-Achievements: Achievements is a static class, that is used to award place achievements to a player.

## Methods

### Award(playerUserID;number,achievementId;number,callback;function):callback { method }

Awards the specified player's userID the specified achievement.

**Example**

```lua
game["Players"].PlayerAdded:Connect(function(plr)
    wait(2)
    Achievements:Award(plr.UserID, 31472, function(success, errormsg)
        if success then
            print("Awarded achievement")  
        else
            print("Error awarding achievement: " .. errormsg)
        end
    end)
end)
```

The callback function has the parameters "success", indicating if the award succeded, and "errormsg", which contains the error message if the award failed.