class SQLJNGList(list):
    def __init__(self, data):
        self.data = data
        super().__init__([data])



# Provide an initial data value when creating an instance
a = Data(0)

# Use append method to add more data
a.append(1)
a.append(2)
print(type(a))

