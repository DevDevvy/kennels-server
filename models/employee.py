class Employee():

    # Class initializer.
    # needs as the first parameter.
    def __init__(self, id, name, location_id, address):
        self.id = id
        self.name = name
        self.location_id = location_id
        self.address = address
        self.location = None
