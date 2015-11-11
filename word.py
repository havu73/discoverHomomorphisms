import letter
import root_list
import copy
class Word:
    def create_root_list():
        a=letter.Letter("a",1)
        b=letter.Letter("b",1)
        c=letter.Letter("c",1)
        d=letter.Letter("d",1)
        A=letter.Letter("a",-1)
        B=letter.Letter("b",-1)
        C=letter.Letter("c",-1)
        D=letter.Letter("d",-1)
        root=root_list.RootList([],0)
        root.add_last(a)
        root.add_last(b)
        root.add_last(A)
        root.add_last(B)
        root.add_last(c)
        root.add_last(d)
        root.add_last(C)
        root.add_last(D)
        root_inv=root_list.RootList([],0)
        root_inv.add_last(d)
        root_inv.add_last(c)
        root_inv.add_last(D)
        root_inv.add_last(C)
        root_inv.add_last(b)
        root_inv.add_last(a)
        root_inv.add_last(B)
        root_inv.add_last(A)
        return [root,root_inv]
    root_list=create_root_list()
    ROOT=root_list[0]
    ROOT_INV=root_list[1]
    
    def __init__(self,l):
        self.list=l

    def append_letter(self,l):
        if l.is_trivial():
            pass
        if len(self.list)==0:
            self.list.append(l)
        else:
            if self.list[len(self.list)-1].compare_letter(l):
                to_add=self.list[len(self.list)-1].sum(l)
                if not (to_add.is_trivial()):
                    self.list[len(self.list)-1]=to_add
                else:
                    self.list=self.list[:-len(self.list)]
            else:
                self.list.append(l)
    
    
    def append_word(self,w):
        if len(self.list)==0:
            self.list=copy.deepcopy(w.list)
        elif len(w.list)==0:
            pass
        else:
            cont=True
            while(len(w.list)!=0 and len(self.list)!=0 and cont):
                if self.list[len(self.list)-1].compare_letter(w.list[0]):
                    new_letter=self.list[len(self.list)-1].sum(w.list[0])
                    if not new_letter.is_trivial():
                        self.list[len(self.list)-1]=new_letter
                        del w.list[0]
                    else:
                        del w.list[0]
                        del self.list[len(self.list)-1]
                else: cont=False
            if len(w.list)!=0:
                self.list.extend(w.list)
                del w

    def append_letter_return_new(self,let):
        result=Word([])
        result.append_word(copy.deepcopy(self))
        result.append_letter(let)
        return result
    
    def append_word_return_new(self,w):
        result=Word([])
        result.append_word(copy.deepcopy(self))
        result.append_word(w)
        return result
    
    def clear(self):
        del self.list[:]

    def append_reduced_word(self,temp,current_root,start_index):
        new_temp=self.find_dehn_inverse(temp, current_root, start_index)
        self.append_word(new_temp)

    def dehn_inverse_assist(self,current_root,start_index,length):
        result=Word([])
        i=0
        while i<length:
            index=(start_index+8-i-1)%8
            new =current_root.get(index).find_inverse()
            result.append_letter(new)
            i+=1
        return result

    def find_dehn_inverse(self,temp, current_root, start_index):
        result=Word([])
        if len(temp.list)<4:
            return temp
        elif len(temp.list)>4:
            length=8-len(temp.list)
            result=self.dehn_inverse_assist(current_root,start_index,length)
            return result
        else:
            if current_root.equals(Word.ROOT_INV):
                result=self.dehn_inverse_assist(current_root,start_index,4)
                return result
            else:
                return temp


    def __str__(self):
        result=""
        for let in self.list:
            result+= let.__str__()+"   "
        return result

    def is_identity(self):
        test=self.reduce()
        del self
        return len(test.list)==0
    
    def compare_to_reduced(self,other):
        new_this=self.reduce()
        new_other=other.reduce()
        if len(new_this.list)!=len(other.list): return False
        elif (new_this.is_identity() and new_other.is_identity()): return True
        else:
            result=True
            for i in range (len(new_this.list)):
                if not (new_this.list[i].compare_to(new_other.list[i])):
                    result=False
                    break
            return result

    def reduce(self):
        if (len(self.list)==0):return self
        else:
            current_root=None
            temp=Word([])
            result=Word([])
            start_index=None
            for i in range(len(self.list)):
                let=self.list[i]
                if i==0:
                    temp.append_letter(let)
                    continue
                if (let.is_single()):
                    if(current_root!=None):
                        if(let.compare_to(current_root.next())):
                            temp.append_letter(let)
                            if(i==len(self.list)-1):
                                result.append_reduced_word(temp, current_root,start_index)
                            else: continue
                        else:
                            result.append_reduced_word(temp,current_root,start_index)
                            temp.clear()
                            if i==len(self.list):
                                result.append_letter(let)
                            else:
                                temp.append_letter(let)
                                current_root=None
                                start_index=None
                                continue
                    else:
                        Word.ROOT.update_pointer(temp.list[0])
                        Word.ROOT_INV.update_pointer(temp.list[0])
                        if (let.compare_to(Word.ROOT.next())):
                            current_root=Word.ROOT
                            temp.append_letter(let)
                            start_index=Word.ROOT.get_current_index()-1
                            if (i==len(self.list)-1):
                                result.append_word(temp)
                                temp.clear
                            else: continue
                        elif (let.compare_to(Word.ROOT_INV.next())):
                            current_root=Word.ROOT_INV
                            temp.append_letter(let)
                            start_index=Word.ROOT_INV.get_current_index()-1
                            if (i==len(self.list)-1):
                                result.append_word(temp)
                                temp.clear
                            else: continue
                        else:
                            if(i==len(self.list)-1):
                                result.append_word(temp)
                                result.append_letter(let)
                                temp.clear()
                            else:
                                result.append_word(temp)
                                temp.clear()
                                temp.append_letter(let)
                                current_root=None
                                start_index=None
                                continue
                else:
                    head=let.find_head_tail()
                    middle=let.find_middle()
                    tail=let.find_head_tail()
                    if(current_root!=None):
                        if(head.compare_to(current_root.next())):
                            temp.append_letter(head)
                            result.append_reduced_word(temp,current_root,start_index)
                            result.append_letter(middle)
                            temp.clear()
                            current_root=None
                            start_index=None
                            temp.append_letter(tail)
                        else:
                            result.append_reduced_word(temp, current_root,start_index)
                            result.append_letter(head)
                            result.append_letter(middle)
                            temp.clear()
                            current_root=None
                            start_index=None
                            temp.append_letter(tail)
                        if(i==len(self.list)-1):
                            result.append_word(temp)
                        else: continue
                    else:
                        result.append_word(temp)
                        temp.clear()
                        result.append_letter(head)
                        result.append_letter(middle)
                        temp.append_letter(tail)
                        if(i==len(self.list)-1):
                            result.append_letter(tail)
                            temp.clear()
                        else: continue
            return result

    def find_inverse(self):
        result=Word([])
        for i in range (len(self.list)):
            let=self.list[len(self.list)-1-i]
            result.append_letter(let.find_inverse())
        return result

    def sum_exp(self):
        result=0
        for let in self.list:
            result+=abs(let.exp)
        return result
                            
        
        
