from .functions import *
from luaparser import ast
from luaparser.astnodes import *

class Compiler():
    def __init__(self):
        pass
    
    def compile(self, src):
        buffer = ''
        parsed = ast.parse(src)
        block = parsed.body.body
        for l in block:
            if type(l) == Call:
                buffer = buffer + str(getFunction(l))
        return buffer
    
    def printChunk(self, src):
        tree = ast.parse(src)
        print(ast.to_pretty_str(tree))
        return tree
        