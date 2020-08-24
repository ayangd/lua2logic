from lua2logic.types import * # pylint: disable=unused-wildcard-import
from luaparser.astnodes import * # pylint: disable=unused-wildcard-import

class LogicFunction():
    def __init__(self):
        self.external = True
    def call(self):
        pass

class HelperFunction(LogicFunction):
    def __init__(self):
        self.external = False

class PrintDefault(LogicFunction):
    def call(self, message: str):
        assert message, 'message should not be empty or None'
        return 'print "' + str(message) + '"\nprintflush message1\n'

class Print(LogicFunction):
    def call(self, target: Message, message: str):
        assert target, 'target should not be None'
        assert message, 'message should not be empty or None'
        return 'print "' + str(message) + '"\nprintflush ' + str(target) + '\n'

class UseMessage(HelperFunction):
    def call(self, number: int):
        assert number > 0, 'Number must be more than 0'
        return Message(number)

def getFunctions():
    return {'print': Print(), 'printi': PrintDefault(), 'useMessage': UseMessage()}