class Customer():
    def __init__(self, id, name, business, location_id, customer_id):
        self.id = id
        self.name = name
        self.business = business
        self.location_id = location_id
        self.customer_id = customer_id

    def __repr__(self):
        return f"{self.name} of {self.business}"

customer = Customer(1, 'Hannah Hall', 'NSS', 1, 4)
