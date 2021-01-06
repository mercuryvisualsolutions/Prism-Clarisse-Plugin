import sys, os

userDir = os.environ["USERPROFILE"]
prismDir = os.path.join(userDir, "Documents", "clarisse", "4.0", "prism")
sys.path.append(prismDir)

from PrismInit import *

print "prismSettings " + str(pcore)

pcore.prismSettings()