from .types import *
from .helpers import *
from luaparser.astnodes import *

class Function():
    def __init__(self):
        self.external = True
    def getReturn(self):
        return None

class HelperFunction(Function):
    def __init__(self):
        self.external = False

class PrintDefault(Function):
    def __init__(self, message: str):
        super().__init__()
        assert message, 'message should not be empty or None'
        self.message = message
    
    def __str__(self):
        return 'print "' + str(self.message) + '"\nprintflush message1\n'

class Print(Function):
    def __init__(self, target: Message, message: str):
        super().__init__()
        assert target, 'target should not be None'
        assert message, 'message should not be empty or None'
        self.target = target
        self.message = message
    
    def __str__(self):
        return 'print "' + str(self.message) + '"\nprintflush ' + str(self.target) + '\n'

class UseMessage(HelperFunction):
    def __init__(self, number: int):
        super().__init__()
        assert number > 0, 'Number must be more than 0'
        self.message = Message(number)
    
    def getReturn(self):
        return self.message

functions = [
    # Logic Functions
    ['print', PrintDefault, [str]],
    ['print', Print, [Message, str]],
    
    #Helper Functions
    ['useMessage', UseMessage, [int]],
]

def getFunction(call: Call, globalNames, localNames):
    for f in functions:
        if call.func.id == f[0] and len(call.args) == len(f[2]):
            found = True
            args = []
            for i in range(len(f[2])):
                arg = evaluate(globalNames, localNames, call.args[i])
                if isinstance(arg, Call):
                    arg = getFunction(arg, globalNames, localNames).getReturn()
                if type(arg) != f[2][i]:
                    found = False
                    break
                args.append(arg)
            if found:
                return f[1](*args)
    return None