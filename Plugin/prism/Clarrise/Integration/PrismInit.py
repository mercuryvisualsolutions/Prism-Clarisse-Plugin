import os, sys, platform

def prismInit():
    Dir = os.path.join("C:/Prism", "Scripts")

    if Dir not in sys.path:
        sys.path.append(Dir)

    import PrismCore
    pcore = PrismCore.PrismCore(app="Clarrise")
    return pcore

pcore = prismInit()