class Kettle(object):
    # initialize
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
# print(kenwood.make)
# print(kenwood.price)
print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)

kenwood.price = 12.75
# print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
# print(hamilton.make)
# print(hamilton.price)
# print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
# Same thing
# print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))
# unlike the first switch on
# we can use this other way to turn on kettle
# this time we feed parameter

print(hamilton.on)
Kettle.switch_on(hamilton)
print(hamilton.on)

hamilton.power = 1.5
print(hamilton.power)
"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: Create an instance of a class
Method: a function defined in a class
Attribute: a variable bound to an instance of a class
"""
