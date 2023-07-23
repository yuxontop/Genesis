
import sys
import types

def getallvars():
    allvars = {}
    for name in dir(sys.modules[__name__]):
        obj = getattr(sys.modules[__name__], name)
        if not name.startswith('__') and not isinstance(obj, types.ModuleType) and not str(name) == "data":
            allvars[name] = obj
    return allvars


for i in getallvars():
    print(" [GENESIS] => " + str(i), ": "+str(getallvars()[i]))
