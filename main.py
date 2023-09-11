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
                        return "Inherits [%s](/objects/%s)" % (className, filePath)
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
    

    """
    !!! NOT SAFE FOR PRODUCTION USE !!!
    """
    @env.macro
    def doc_env():
        "Document the environment"
        return {name:getattr(env, name) for name in dir(env) if not name.startswith('_')}