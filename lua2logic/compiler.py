from lua2logic.functions import * # pylint: disable=unused-wildcard-import
from lua2logic.helpers import * # pylint: disable=unused-wildcard-import
from luaparser import ast
from luaparser.astnodes import * # pylint: disable=unused-wildcard-import

class Compiler():
    def __init__(self):
        pass
    
    def compile(self, src: str):
        globalNames = getFunctions()
        localNames = []
        parsed = ast.parse(src)
        return self._compile(parsed.body, globalNames, localNames)
    
    def _compile(self, block: Block, globalNames: dict, localNames: list):
        buffer = ''
        localNames.append({})
        blockBody = block.body
        for l in blockBody:
            if type(l) == Assign or type(l) == LocalAssign:
                for i in range(len(l.targets) - 1, -1, -1):
                    if len(l.values) - 1 <= i:
                        val = l.values[i]
                        if type(val) == Call:
                            val = evaluate(globalNames, localNames, val)
                            if val == None:
                                raise Exception(f'Function {l.values[i].func.id} doesn\'t exist.')
                        if type(l) == Assign:
                            globalNames[l.targets[i].id] = val
                        else:
                            localNames[-1][l.targets[i].id] = val
            elif type(l) == Call:
                if l.func.id in globalNames.keys():
                    func = globalNames[l.func.id]
                    if (func.external):
                        buffer = buffer + str(func.call(*tuple(map(lambda x: evaluate(globalNames, localNames, x), l.args))))
        localNames = localNames[:-1]
        return buffer
    
    def printChunk(self, src: str):
        tree = ast.parse(src)
        print(ast.to_pretty_str(tree))
        return tree
        