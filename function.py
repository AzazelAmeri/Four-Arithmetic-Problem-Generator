import random

class Number:
    '''Generate proper fractions, whole numbers, mixed fractions.
    1 stands for proper fractions, 2 stands for mixed fractions,
    others stand for whole numbers.'''

    def __init__(self,ntype,max):
        self.integer=0
        self.numerator=0
        self.denominator=0
        self.ntype=ntype
        if self.ntype==1:
            if max<3:
                self.ntype=3
                self.integer=random.randint(0,max-1)
                return
            else:
                self.denominator=random.randint(2,max-1)
                self.numerator=random.randint(1,self.denominator-1)
        elif self.ntype==2:
            if max<3:
                self.ntype=3
                self.integer=random.randint(0,max-1)
                return
            else:
                self.integer=random.randint(1,max-1)
                self.denominator=random.randint(2,max-1)
                self.numerator=random.randint(1,self.denominator-1)
        else:
            self.ntype=3
            self.integer=random.randint(0,max-1)

    def generate_string(self):
        if self.ntype==1:
            return str(self.numerator)+'/'+str(self.denominator)
        elif self.ntype==2:
            return str(self.integer)+'\''+str(self.numerator)+'/'+str(self.denominator)
        else:
            return str(self.integer)

    def get_value(self):
        if self.denominator:
            return self.integer+self.numerator/self.denominator
        else:
            return self.integer

class Expression:
    '''processing four arithmetic formulas'''

    def __init__(self,max):
        self.nums=[]
        self.syboms=[]
        self.brackets=[]
        self.expression=''
        self.max=max
        self.sybom_num=random.randint(1,3)

    def randomly_generated_brackets(self):
        if self.sybom_num==1:
            self.brackets=[]
        if self.sybom_num==2:
            self.brackets=[(0,4),(2,6)]
        

    def randomly_generated_syboms(self):
        for _ in range(self.sybom_num):
            pass

    def randomly_generated_expression(self):
        pass

    def reduction_of_a_fraction(numerator,denominator):
        if numerator>denominator:
            integer=numerator/denominator
        elif numerator==denominator:
            result=1
        else:
            pass
        return result

    def processing_string(string):
        pass




