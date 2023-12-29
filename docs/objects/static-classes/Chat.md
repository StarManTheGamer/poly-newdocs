---
icon: polytoria/Chat
weight: 10
---

# Chat

:polytoria-Chat: Chat is a static class used for various actions regarding the chat.

## Methods

### BroadcastMessage { method }

Sends a chat message to all users.

### UnicastMessage { method }

Sends a chat message to a specific user.

**Example**

```lua
Chat:UnicastMessage("Hello, world!", game["Players"]["willemsteller"])
```
