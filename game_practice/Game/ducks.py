class Duck(object):

    def walk(self):
        print("waddle, waddle, waddle")

    def swim(self):
        print("Come on in the waters lovely")

    def quack(self):
        print("Quack Quack")


class Penguin(object):
    def walk(self):
        print("waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but the waters chilly this far south")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)