from lua2logic.types import * # pylint: disable=unused-wildcard-import
from lua2logic.functions import * # pylint: disable=unused-wildcard-import
from luaparser.astnodes import * # pylint: disable=unused-wildcard-import

def varCheck(globalNames, localNames, varName):
    s = varName
    if isinstance(s, Name):
        s = s.id
    for localName in localNames[::-1]:
        if s in localName.keys():
            return True
    if s in globalNames.keys():
        return True
    raise Exception(s + ' is undefined.')

def varConsume(globalNames, localNames, varName):
    s = varName
    if isinstance(s, Name):
        s = s.id
    for localName in localNames[::-1]:
        if s in localName.keys():
            localName.remove(s)
            return True
    if s in globalNames.keys():
        globalNames.remove(s)
        return True
    raise Exception(s + ' is undefined.')

def getLiteral(o):
    if type(o) == String:
        return o.s
    if type(o) == Number:
        return o.n
    return o

def varResolve(globalNames, localNames, varName):
    s = varName
    if isinstance(s, Name):
        s = s.id
    for localName in localNames[::-1]:
        if s in localName.keys():
            return localName[s]
    if s in globalNames.keys():
        return globalNames[s]
    raise Exception(s + ' is undefined.')

def evaluate(globalNames, localNames, o):
    if isinstance(o, Call):
        return varResolve(globalNames, localNames, o.func).call(*tuple(map(lambda x: evaluate(globalNames, localNames, x), o.args)))
    if isinstance(o, Name):
        return varResolve(globalNames, localNames, o)
    return getLiteral(o)