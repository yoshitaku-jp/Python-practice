class Gate:
    def __init__(self, name):
        self.name = name

    def enter(self, ticket):
        ticket.stamp(self.name)

    def exit(self, ticket):
        return True
