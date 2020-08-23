from .functions import *
from .helpers import *
from luaparser import ast
from luaparser.astnodes import *

class Compiler():
    def __init__(self):
        pass
    
    def compile(self, src):
        globalNames = {}
        localNames = []
        parsed = ast.parse(src)
        return self._compile(parsed.body, globalNames, localNames)
    
    def _compile(self, block: Block, globalNames, localNames):
        buffer = ''
        localNames.append({})
        blockBody = block.body
        for l in blockBody:
            if type(l) == Assign or type(l) == LocalAssign:
                for i in range(len(l.targets) - 1, -1, -1):
                    if len(l.values) - 1 <= i:
                        val = l.values[i]
                        if type(val) == Call:
                            val = getFunction(val, globalNames, localNames)
                            if val == None:
                                raise Exception(f'Function {l.values[i].func.id} doesn\'t exist.')
                        if type(l) == Assign:
                            globalNames[l.targets[i].id] = evaluate(globalNames, localNames, val.getReturn())
                        else:
                            localNames[-1][l.targets[i].id] = evaluate(globalNames, localNames, val.getReturn())
            elif type(l) == Call:
                buffer = buffer + str(getFunction(l, globalNames, localNames))
        localNames = localNames[:-1]
        return buffer
    
    def printChunk(self, src):
        tree = ast.parse(src)
        print(ast.to_pretty_str(tree))
        return tree
        