---
title: Script
description: Script runs Lua scripts on the server.

icon: polytoria/Script
weight: 1
---

# Script

:polytoria-Script: Script runs Lua scripts on the server. Any code that should be kept on the server (such as Datastores) should be kept in a script.

Some classes and functions are only callable through a ScriptInstance. You may find a server-exclusive warning with them in the Documentation.

{{ inherits("BaseScript") }}
