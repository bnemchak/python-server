class Location():
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def __repr__(self):
        return f"{self.name} from {self.address}"

location = Location(1, 'Nashville North', '8422 Johnson Pike')
