import os

"Define macros"
def define_env(env):
    """
    Used to generate the "Inherited from" links in the documentation.
    This runs custom logic to find the correct link for a given class name,
    as the class name is not always equvilent to the markdown file's path.

    This assumes that the class is correctly placed in the docs/objects/ folder

    TODO: move file searching logic to a seperate function
    """
    @env.macro
    def inherits(className):
        # Find the actual link for the input classname by searching for the markdown file
        search_path = "docs/objects/"
        for root, dirs, files in os.walk(search_path):
            for file in files:
                if file.endswith(".md"):
                    if file[:-3] == className:
                        filePath = os.path.join(root, file)
                        filePath = filePath[len(search_path):]
                        filePath = filePath[:-3]
                        return "Inherits [:polytoria-%s: %s](/objects/%s)" % (className, className, filePath)
        return "Inherits %s" % (className)

    @env.macro
    def ambiguous(className, description):
        # Find the actual link for the input classname by searching for the markdown file
        search_path = "docs/objects/"
        text = "Not to be confused with %s" % (className)
        for root, dirs, files in os.walk(search_path):
            for file in files:
                if file.endswith(".md"):
                    if file[:-3] == className:
                        filePath = os.path.join(root, file)
                        filePath = filePath[len(search_path):]
                        filePath = filePath[:-3]
                        text = "Not to be confused with [%s](/objects/%s)" % (className, filePath)

        return "!!! note \"%s, %s\"" % (text, description)
    

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
    This object is automatically created by Polytoria. Its parent cannot be changed."""

    """
    !!! NOT SAFE FOR PRODUCTION USE !!!
    """
    @env.macro
    def doc_env():
        "Document the environment"
        return {name:getattr(env, name) for name in dir(env) if not name.startswith('_')}