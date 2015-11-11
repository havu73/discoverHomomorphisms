import letter
class RootList:
    def __init__(self,l,i):
        self.list=l
        self.index=i

    def add_last(self,st):
        self.list.append(st)

    def update_pointer(self,st):
        for i in range(len(self.list)):
            if self.list[i].compare_to(st):
                self.index=i
                break

    def next(self):
        self.index=(self.index+1)%(len(self.list));
        return self.list[self.index]

    def __str__(self):
        result=""
        for letter in self.list:
            result+=letter.__str__()+"  "
        return result

    def equals(self, other):
        return(self.list[0].compare_to(other.list[0]))

    def get_current_index(self):
        return self.index

    def get(self, index):
        return self.list[index]

    
    
