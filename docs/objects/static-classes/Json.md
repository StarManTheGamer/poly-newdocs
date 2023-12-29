---
icon: polytoria/Json
weight: 11
---

# Json

:polytoria-json: Json is a module which converts between JSON scripts and Lua tables.

<div data-search-exclude markdown>
!!! note "The json module can be called through scripts with the `json` keyword."
</div>

## Methods

### isNull:bool { method }

Returns true if the value specified is a null read from a json

### null:string { method }

Returns a special value which is a representation of a null in a json

### parse:Table { method }

Returns a table with the contents of the specified JSON string

**Example**

```lua
Http:Get("https://api.polytoria.com/v1/asset/owner?userID=1&assetID=234", function (data, error, errmsg)
    if error then
        print("Something went wrong!")
        return
    end

    print(json.parse(data)["Success"])
end)
```

### serialize:string { method }

Returns a json string with the contents of the specified table.
