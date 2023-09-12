import os

def getClassLink(className):
    # Find the actual link for the input classname by searching for the markdown file
    search_path = "docs/objects/"
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.endswith(".md"):
                if file[:-3] == className:
                    filePath = os.path.join(root, file)
                    filePath = filePath[len(search_path):]
                    filePath = filePath[:-3]
                    icon = className
                    if (filePath.startswith("enums/")):
                        icon = "Enum"
                    return "[:polytoria-%s: %s](/objects/%s)" % (icon, className, filePath)
    return "?"

"Define macros"
def define_env(env):
     
                        
    """
    Used to generate the "Inherited from" links in the documentation.
    This runs custom logic to find the correct link for a given class name,
    as the class name is not always equvilent to the markdown file's path.

    This assumes that the class is correctly placed in the docs/objects/ folder
    """
    @env.macro
    def inherits(className):
        return "Inherits %s" % (getClassLink(className))

   
    @env.macro
    def ambiguous(className, description):
        return "!!! note \"Not to be confused with %s, %s\"" % (getClassLink(className), description)
    
    # Classes is an array of pairs of class names and descriptions
    @env.macro
    def ambiguousMultiple(classes):
        text = "!!! note \"Not to be confused with:\""
        for i in range(len(classes)):
            text += "\n    - %s (%s)\n" % (getClassLink(classes[i][0]), classes[i][1])
        return text
        

    


    @env.macro
    def notnewable():
        return """!!! warning "Not newable"
    This object cannot be created by scripts using `Instance.New()`"""

    @env.macro
    def abstract():
        return """!!! danger "Abstract object"
    This object exists only to serve as a foundation for other objects. It cannot be accessed directly, but its properties are documented below."""

    @env.macro
    def service():
        return """!!! example "Service object"
    This object is automatically created by Polytoria. Additionally, scripts cannot change its parent."""

    @env.macro
    def nosync():
        return """!!! failure "Does not sync!"
    This object does not sync across the server and client. It is recommended to avoid changing its properties from %ss, as the changes will not be visible to players.""" % (getClassLink("Script"))

    @env.macro
    def serverproperty():
        return "!!! warning \"This property is only available to the server. It can only be accessed with server scripts\"" 
    
    @env.macro
    def clientproperty():
        return "!!! warning \"This property is only available to the client. It can only be accessed with server scripts\"" 


    """
    !!! NOT SAFE FOR PRODUCTION USE !!!
    """
    @env.macro
    def doc_env():
        "Document the environment"
        return {name:getattr(env, name) for name in dir(env) if not name.startswith('_')}
    
def property(name):
    value = name[3:] # in form "name:type=value"
    name = value.split(":")[0].strip()
    property_type = value.split(":")[1].strip()
    default_value = ""
    type_text = property_type
    has_link = False
    if (getClassLink(property_type) != "?"):
        property_type = getClassLink(property_type)
        has_link = True
    else:
        property_type = "%s" % (property_type)
        
    if "=" in property_type:
        split = property_type.split("=")
        property_type = split[0]
        default_value = split[1]
        if not has_link:
            property_type = "`%s`" % (property_type)
        type_text = "%s = `%s`" % (property_type, default_value)
    else:
        type_text = "%s" % (property_type)



    return "### %s : %s { #%s data-toc-label=\"%s\" }" % (name, type_text, name, name)

def method(name):
    value = name[3:] # in form "name:type"
    name = value.split(":")[0]
    property_type = value.split(":")[1]
    return "### %s → `%s` { #%s data-toc-label=\"%s\" }" % (name, property_type, name, name)
def on_pre_page_macros(env):
    #find headers with { property } at the end and replace with the property macro
    markdown_text = env.markdown
    lines = markdown_text.split("\n")
    for i in range(len(lines)):
        if lines[i].endswith("{ property }"):
            lines[i] = property(lines[i][:-12])
    markdown_text = "\n".join(lines)
    env.markdown = markdown_text