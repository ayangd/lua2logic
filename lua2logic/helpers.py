from .types import *
from .functions import *
from luaparser.astnodes import *

def varCheck(globalNames, localNames, varName):
    for localName in localNames[::-1]:
        if varName.id in localName.keys():
            return True
    if varName.id in globalNames.keys():
        return True
    raise Exception(varName.id + ' is undefined.')

def varConsume(globalNames, localNames, varName):
    for localName in localNames[::-1]:
        if varName.id in localName.keys():
            localName.remove(varName.id)
            return True
    if varName.id in globalNames.keys():
        globalNames.remove(varName.id)
        return True
    raise Exception(varName.id + ' is undefined.')

def getLiteral(o):
    if type(o) == String:
        return o.s
    if type(o) == Number:
        return o.n
    return o

def varResolve(globalNames, localNames, varName):
    for localName in localNames[::-1]:
        if varName.id in localName.keys():
            return localName[varName.id]
    if varName.id in globalNames.keys():
        return globalNames[varName.id]
    raise Exception(varName.id + ' is undefined.')

def evaluate(globalNames, localNames, o):
    if isinstance(o, Name):
        return varResolve(globalNames, localNames, o)
    return getLiteral(o)