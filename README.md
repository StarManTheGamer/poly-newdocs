> GitHub Pages Deployment: [here](https://starmanthegamer.github.io/poly-newdocs/)

# Revamped Polytoria Documentation

This is a fork of the new-docs branch on the Polytoria Scripting Documentation GitHub repository which you can find [here](https://github.com/Polytoria/Docs/tree/new-docs). That branch has been unmaintained for a while so this is a maintained version as it would be a shame to let such an improved documentation experience just collect dust. We hope to have all of this documentation filled out soon.

## Macros

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
