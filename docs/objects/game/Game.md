---
title: Game
description: Game is the root object in the Polytoria instance tree. It is the object of which everything is descended.
icon: polytoria/Game
weight: 1
---

# Game

{{ notnewable() }}

<div data-search-exclude markdown>
!!! tip "This object can be accessed in scripts by using the `game` keyword."
</div>

:polytoria-Game: Game is the root object in the Polytoria instance tree. It is the object of which everything is descended.

{{ inherits("Instance") }}

## Properties

### GameID:int { property }

The ID of the current Polytoria place.

The value is `0` when testing locally through Polytoria Creator, which can be used as a conditional to check if the game is live or not.

### InstanceCount:int { property }

The total number of instances currently loaded

!!! note "Remarks"
    The value will differ depending on if it is being accessed through a Script or a LocalScript, as LocalScripts can only see instances that are relevant to the client.

## Events

### Rendered { event }

Called every frame after the game has been rendered

!!! warning "Notice"
    The server is incapable of rendering frames; rather, on server Scripts, the event will fire at the server's tick rate which may vary between 1-30Hz.

    It is recommended to only listen to this event on LocalScripts.
