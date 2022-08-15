

class SchoolAppForm:

    def __init__(self, name, age, cls):
        self.name = name
        self.age = age
        self.cls = cls
        # print('this is init method')



    def info_print(self):
        if self.cls>=8:
            amount='Rs.1000'
        elif self.cls>=5 and self.cls<=7:
            amount='RS.500'
        else:
            amount='Rs.200'
        print(f'Hello {self.name} , your application form is approved and as per class you have pay {amount}')



puja=SchoolAppForm('puja',15,9)
puja.info_print()

sambit=SchoolAppForm('sambit',8,2)
sambit.info_print()