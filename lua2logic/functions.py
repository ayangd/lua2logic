from .types import *
from luaparser.astnodes import *

def getFunction(call):
    if call.func.id == 'print' and len(call.args) == 1 and type(call.args[0]) == String:
        return Print(call.args[0].s)
    print('No.')
    return None

class Function():
    pass

class Print(Function):
    def __init__(self, s):
        self.s = s
    
    def __str__(self):
        return 'print "' + str(self.s) + '"\nprintflush message1\n'