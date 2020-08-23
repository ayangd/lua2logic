class Message():
    def __init__(self, number: int):
        assert number > 0, 'Number must be more than 0'
        self.number = number
    
    def __str__(self):
        return f'message{self.number}'