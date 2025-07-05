class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': "YOYO",
            'has_pets': False
        }

    def __str__(self):  # this method will override original dunder method __str__
        return f'{self.color}'

    def __len__(self):  # this method will override original dunder method __len__
        return 5

    def __call__(self):  # this method will override original dunder method __call__ AND THIS IS SPECIAL METHOD CALL
        return ('Yesssssss')

    def __getitem__(self, i):  # this method will override original dunder method __len__
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(action_figure.__len__())
print(action_figure())  # without using .__call__ it will call our __call__ method, that is the speciality
print(action_figure['name'])  # without using .__getitem__ it will call our __getitem__ method, that is the speciality

# print(str(action_figure))
