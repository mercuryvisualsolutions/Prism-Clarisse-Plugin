import os, sys, platform
# import dill

def prismInit():
    Dir = os.path.join("C:/Prism", "Scripts")

    if Dir not in sys.path:
        sys.path.append(Dir)

    import PrismCore
    pcore = PrismCore.PrismCore(app="Clarrise", prismArgs = ['silent'])
    return pcore

pcore = prismInit()