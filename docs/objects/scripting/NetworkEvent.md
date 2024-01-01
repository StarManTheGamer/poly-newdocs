---
icon: polytoria/NetworkEvent
weight: 5
---

# NetworkEvent

:polytoria-NetworkEvent: NetworkEvents are events that can be called to communicate between server and client. {{ classLink("NetMessage") }} are the class used for sharing data between server and client when sending NetworkEvents.

{{ inherits("Instance") }}

## Events

### InvokedClient:Sender=nil:NetMessage { event }

Fires when the client receives a message from the server.

**Example**

```lua
netEvent.InvokedClient:Connect(function (sender, message)
    local value = message:GetString("key")
end)
```

{{ clientexclusive() }}

### InvokedServer:Sender=Player:NetMessage { event }

Fires when the server receives a message from the client.

**Example**

```lua
netEvent.InvokedServer:Connect(function (sender, message)
    local value = message:GetString("key")
end)
```

{{ serverexclusive() }}

## Methods

### InvokeClient:void { method }

Sends a network event to a specific player from the server.

**Example**

```lua
local message = NetMessage.New()
message.AddString("key", "value")
netEvent.InvokeClient(message, game["Players"]["willemsteller"])
```

{{ serverexclusive() }}

### InvokeClients:void { method }

Sends a network event to all players from the server.

**Example**

```lua
local message = NetMessage.New()
message.AddString("key", "value")
netEvent.InvokeClients(message)
```

{{ serverexclusive() }}
