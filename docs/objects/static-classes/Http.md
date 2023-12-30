---
icon: polytoria/Http
weight: 11
---

# Http

:polytoria-Http: Http is a static class used for HTTP communications.

<div data-search-exclude markdown>
!!! note "Http requests can only be called from the server."
</div>

<div data-search-exclude markdown>
!!! note "The request sends the current game ID as a header (PT-Game-ID)"
</div>

!!! warning "There is a limit of 15 requests per minute when using the Http static class."

## Methods

### Delete { method }

Sends a DELETE request to the specified url.

**Example**

```lua
Http:Delete("https://example.com/api/delete", "id=1" , function (data, error, errmsg)
    if not error then
        script.Parent.Color = Color.New(1, 1, 1)
        script.Parent.Text = data
    else
        script.Parent.Color = Color.New(1, 0, 0)
        script.Parent.Text = errmsg
    end
end)
```

<div data-search-exclude markdown>
!!! note "Params are in query form: `(key1=value&key2=value)`"
</div>

### Get { method }

Sends a GET request to the specified url.

**Example**

```lua
Http:Get("https://api.polytoria.com/v1/store/25272", function (data, error, errmsg)
    if not error then
        script.Parent.Color = Color.New(1, 1, 1)
        script.Parent.Text = data
    else
        script.Parent.Color = Color.New(1, 0, 0)
        script.Parent.Text = errmsg
    end
end,{})
```

### Post { method }

Sends a POST request to the specified url.

**Example**

```lua
Http:Post("https://example.com/api/post", "id=1&name=Hello" , function (data, error, errmsg)
    if not error then
        script.Parent.Color = Color.New(1, 1, 1)
        script.Parent.Text = data
    else
        script.Parent.Color = Color.New(1, 0, 0)
        script.Parent.Text = errmsg
    end
end)
```

<div data-search-exclude markdown>
!!! note "Params are in query form: `(key1=value&key2=value)`"
</div>

### Put { method }

Sends a PUT request to the specified URL

**Example**

```lua
Http:Put("https://example.com", "id=1&content=Hello" , function (data, error, errmsg)
    if not error then
        script.Parent.Color = Color.New(1, 1, 1)
        script.Parent.Text = data
    else
        script.Parent.Color = Color.New(1, 0, 0)
        script.Parent.Text = errmsg
    end
end)
```

<div data-search-exclude markdown>
!!! note "Params are in query form: `(key1=value&key2=value)`"
</div>
