class Character:
    def __init__(self, name, nickname):
        self.__name = name
        self.nickname = nickname

    def show(self):
        print("The character's name is", self.__name, "and the nickname is", self.nickname)


Z = Character("Zed", "Shadow")
Z.show()
print(Z.nickname)



# It'll give us an attribute error!

# print(Z.name)
# print(Z.__name)
