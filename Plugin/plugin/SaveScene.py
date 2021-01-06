import os, sys
import ix


userDir = os.environ["USERPROFILE"]
prismDir = os.path.join(userDir, "Documents", "clarisse", "4.0", "prism")
sys.path.append(prismDir)

from PrismInit import *
print pcore

project_name = ix.application.get_factory().get_vars().get("PNAME").get_string()
dir_name = ix.application.get_factory().get_vars().get("PDIR").get_string()

filename = os.path.join(dir_name, project_name)

ix.save_project(filename)
