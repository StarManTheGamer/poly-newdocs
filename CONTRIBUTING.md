# Contributing

Thanks for waiting to contribute to the new unofficial Polytoria documentation! If you can't contribute at this time please notify one of our contributers and tell them the change that should be made and they can do it for you. Otherwise, you can open a pull request and we'll either accept it or request changes depending on what the pull request is about.

## Notes

1. When creating a page make sure if it is a class it should have the corresponding icon at the start of the description
2. When creating a page it is recommended that if it is an abstract object (one that can't be created using `Instance.New()` and is only used a base/inheriting class for other parts) there is no description

## Page Order
Pages should be ordered like this:
1. Events
2. Methods
3. Properties

## How-To Write

### How-To: Write Events

> Events will be slightly updated in a few days so this will be written after that.

### How-To: Write Methods

> To be written

### How-To: Write Properties

`PropertyName:Type { property }`
PropertyName is the name of the property
Type is the type that is returned when reading the property and that the property is set to when set
The last part is a macro, that stays the same for all properties to make sure the code knows it's a property

## Lists

### Macros List

Macros are short commands you can put in documentation pages that will be replaced with notes.

| Name                                      | Text                                                                                                                                                                                                                                             |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `{{ inherits(className) }}`               | **Text:** "Inherits className". "?" if no classLink exists under that className                                                                                                                                                                  |
| `{{ ambiguous(className, description) }}` | **Note:** "Not to be confused with className, description"                                                                                                                                                                                       |
| `{{ ambiguousMultiple(classes) }}`        | **Note:** "Not to be confused with [classes]"                                                                                                                                                                                                    |
| `{{ notnewable() }}`                      | **Note (warning):** "This object cannot be created by scripts using `Instance.New()`"                                                                                                                                                            |
| `{{ abstract() }}`                        | **Note (danger):** "This object exists only to serve as a foundation for other objects. It cannot be accessed directly, but its properties are documented below. Additionally, it cannot be created in the creator menu or with `Instance.New()" |
| `{{ service() }}`                         | **Note (example):** "This object is automatically created by Polytoria. Additionally, scripts cannot change its parent."                                                                                                                         |
| `{{ staticclass(className) }}`            | **Note (tip):** "This object is a static class. It can be accessed by using it's name as a keyword like this `className`. Additionally, it cannot be created in the creator menu or with `Instance.New()`"                                       |
| `{{ serverexclusive() }}`                 | **Note (warning):** "This is only available to the server. It can only be accessed within server scripts."                                                                                                                                       |
| `{{ clientexclusive() }}`                 | **Note (warning):** "This is only available to the client. It can only be accessed within local scripts."                                                                                                                                        |
| `{{ nosync() }}`                          | **Note (failure):** "This object does not sync across the server and client. It is recommended to avoid changing its properties from Scripts, as the changes will not be visible to players."                                                    |
| `{{ readonly() }}`                        | **Note (warning):** "This property is read-only and cannot be modified."                                                                                                                                                                         |
| ~~`{{ comingsoon() }}`~~                  | NOT CURRENTLY USED ANYWHERE                                                                                                                                                                                                                      |
| `{{ classlink(className) }}`              | **Returns:** The class specified as a link with the corresponding icon next to it. "?" if no classLink exists under that className                                                                                                               |
