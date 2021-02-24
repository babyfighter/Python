class Dog:
    def __init__(self, name):
        self.name = name

    @classmethod
    def dogs_count(cls):
        pass

    def game(self):
        print("%s playing" %self.name)


class XTDog(Dog):
    def game(self):
        print("%s flying" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s and %s playing" % (self.name, dog.name))

        dog.game()


# wc = Dog("wc")
wc = XTDog("wc")
xiaoming = Person("xiaoming")
xiaoming.game_with_dog(wc)
