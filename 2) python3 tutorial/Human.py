class Human:

    count = 0
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        Human.count += 1

    def get_age(self, age, num):
        """[summary]
        Arguments:
            age {[type]} -- [asd asd ad]
            num {[type]} -- [description]
        Returns:
            [type] -- [description]
        """

        return "The "+ self.name + "'s age is " + str(self.age)

ali = Human(name='Ali', age=17, height=170, weight=65)
javad = Human(name ='Javad', age=27, height= 163, weight=79)







