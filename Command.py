class Command:
    def __init__(self, function, *args):
        self.function = function
        self.args = list(args)
    def execute(self):
        self.function(*self.args)
