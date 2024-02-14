---
title: Achievements
description: Achivements is a static class, that is used to award place achivements to a player.
icon: polytoria/Achievements
---

# Achievements

{{ staticclass("Achievements") }}

:polytoria-Achievements: Achievements is a static class, that is used to award place achievements to a player.

## Methods

### Award(playerUserID;number,achievementId;number,callback;function):callback { method }

Awards the specified player's userID the specified achievement.

The callback function has the parameters "success", indicating if the award succeded, and "errormsg", which contains the error message if the award failed.