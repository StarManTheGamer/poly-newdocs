---
title: Players
description: Players is the container class for all Player instances.
icon: polytoria/Players
weight: 4
---

# Players

{{ ambiguous("Player", "the object that represents a single player.") }}

{{ service() }}

{{ notnewable() }}

:polytoria-Players: Players is the container class for all Player instances.

{{ inherits("Instance") }}

## Events

### PlayerAdded:Player { event }

Fires when a player joins the server.

### PlayerRemoved:Player { event }

Fires when a player leaves the server.

## Methods

### GetPlayer(username;String):Player { method }

Returns the player instance from their username.

### GetPlayerByID(userID;int):Player { method }

Returns the player instance from their user ID.

### GetPlayers:array { method }

Returns all players in the place as an array.

## Properties

### LocalPlayer:Player { property }

Returns the local player currently playing.

{{ clientexclusive() }}

### PlayerCollisionEnabled:bool { property }

Determines whether or not collisions between players are enabled.
