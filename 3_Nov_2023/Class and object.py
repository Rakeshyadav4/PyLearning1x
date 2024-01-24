class Rakesh:
    # defining constructor, so we need to make sure number of argument matches same as object
    def __init__(self, age, height, weight, ):
        self.age = age
        self.height = height
        self.weight = weight

    #  This function is to tell python that I want this output format
    def display(self, title):  # this should same as last line
        #  print(f'{tittle}:{self.age}{self.height}{self.weight}')
        print(f"{title} : age = {self.age}, height = {self.height}, weight = {self.weight}")

#  make sure argument value should match the number of argument as constructor.
Rakesh_now = Rakesh(43, 173, 78)
Rakesh_target = Rakesh(35, 173, 72)

#  here we are calling the code, and it should match the format output function created as above.
Rakesh_now.display('Rakesh_now')
Rakesh_target.display('Rakesh_target')
