---
icon: polytoria/Datastore
weight: 11
---

# Datastore

:polytoria-Datastore: Datastore (not to be confused with the Datastore data type) is a service used for storing data between sessions.

## Limits

There is a limit placed on the Datastore functions per server instance. Requests that exceed this limit will be canceled and return an error. Read and write functions both have their own rate limit of `(30 + (10 * [amount of players]))` requests per minute. This limit is reset every minute.

You can create as many datastores as you want, however each datastore is limited to 65,535 bytes and it's key cannot be longer than 32 characters. Creating a datastore will also count towards the rate limit.

<div data-search-exclude markdown>
!!! note "If you are testing your place locally through Polytoria Creator, no requests will be made to the server and your data will not be saved after the session ends. You will need to upload your place to the website to test the datastore."
</div>

## Methods

### GetDatastore { method }

Gets a Datastore object from the Datastore service.

**Example**

```lua
local ds = Datastore:GetDatastore("Player_" .. player.UserID)

while ds.Loading do
    wait()
end

ds:Get("Coins", function(value, success, error)
    if not success then
        print(error)
    else
        print(player.Name .. " has " .. value .. " coins.")
    end
end)
```
