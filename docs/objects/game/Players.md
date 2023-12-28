---
icon: polytoria/Players
weight: 4
---

# Players

{{ ambiguous("Player", "the object that represents a single player.") }}

{{ service() }}

{{ notnewable() }}

:polytoria-Players: Players is the container class for all Player instances.

{{ inherits("Instance") }}

## Properties
### LocalPlayer:Player { property }
Returns the local player currently playing.

{{ clientexclusive() }}

### PlayerCollisionEnabled:bool { property }
Determines whether or not collisions between players are enabled.

## Events
### PlayerAdded:Player { event }
Fires when a player joins the server.

### PlayerRemoved:Player { event }
Fires when a player leaves the server.

## Methods
### GetPlayer:Player { method }
Returns the player instance from their username.

### GetPlayerByID:Player { method }
Returns the player instance from their user ID.

### GetPlayers:array { method }
Returns all players in the game as an array.