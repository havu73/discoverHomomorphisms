class Letter:
    def __init__(self, l, e):
        self.letter=l
        self.exp=e

    def compare_to(self, other):
        return (self.letter==other.letter and self.exp==other.exp)

    def compare_letter(self,other):
        return (self.letter==other.letter)

    def sum(self,other):
        result= Letter(self.letter, self.exp+other.exp)
        return result

    def is_single(self):
        return (self.exp==1 or self.exp==-1)

    def is_trivial(self):
        return (self.exp==0)

    def find_inverse(self):
        result=Letter(self.letter,-self.exp)
        return result

    def __str__(self):
        return self.letter+"^"+str(self.exp)

    def find_head_tail(self):
        if self.exp<0:
            return Letter(self.letter,-1)
        elif self.exp>0:
            return Letter(self.letter,1)
        else: return Letter(self.letter,0)

    def find_middle(self):
        if self.exp<0:
            return Letter(self.letter,self.exp+2)
        elif self.exp>0:
            return Letter(self.letter, self.exp-2)
        else:
            return Letter(self.letter,0)
