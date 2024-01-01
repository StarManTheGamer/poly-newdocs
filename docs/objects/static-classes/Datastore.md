---
icon: polytoria/Datastore
weight: 11
---

# Datastore

{{ staticclass()}}

:polytoria-Datastore: Datastore (not to be confused with the Datastore data type) is a service used for storing data between game sessions.

{{ serverexclusive() }}

## Limits

There is a limit placed on the Datastore functions per server instance. Requests that exceed this limit will be canceled and return an error. Read and write functions both have their own rate limit of `(30 + (10 * [amount of players]))` requests per minute. This limit is reset every minute.

You can create as many datastores as you want, however each datastore is limited to 65,535 bytes and it's key cannot be longer than 32 characters. Creating a datastore will also count towards the rate limit.

!!! warning "Size Limits"
    **Rate Limit:** up to `(30 + (10 * [amount of players]))` requests per minute (for example; a server with 5 players would have a limit of 80 requests/min)

    **Datastore Size:** up to 65,535 bytes

    **Key Length:** up to 32 characters

!!! note "Local Testing" 
    If you are testing your place locally through Polytoria Creator, no requests will be made to the server and your data will not be saved after the session ends. You will need to upload your place to the website to test the requests.

## Events

### Loaded { event }

Fires when the Datastore object loads.

## Methods

### GetDatastore:Datastore { method }

Attempts to get a Datastore object from the Datastore service.

??? note "Wait till Loaded"
    Make sure to wait until the Datastore object is loaded by waiting until the `.Loaded` event on the Datastore object is fired.

**Example**

```lua
local ds = Datastore:GetDatastore("Player_" .. player.UserID)
```

### Get:callback { method }

Attempts to get the value of a key from a Datastore.

**Example**

```lua
-- Attempts to get the value of "Coins"
ds:Get("Coins", function(value, success, error)
    if not success then
        print(error)
    else
        print(player.Name .. " has " .. value .. " coins.")
    end
end)
```

### Remove:callback { method }

Attempts to remove a key from a Datastore.

**Example**

```lua
-- Attempts to remove the key "Coins"
ds:Remove("Coins", function(success, error)
    if not success then
        print(error)
    else
        print(player.Name .. "'s coins have been removed!")
    end
end)
```

### Set:callback { method }

Attempts to set the value of a key in a Datastore

**Example**

```lua
-- Attempts to set the value of "Coins" to 100
ds:Set("Coins", 100, function(success, error)
    if not success then
        print(error)
    else
        print(player.Name .. "'s coins have been set to 100!")
    end
end)
```

## Properties

### Loading:bool { property }

Returns true or false depending on if the Datastore object is loaded.

{{ readonly() }}