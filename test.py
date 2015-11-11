import letter
import root_list
import word

a=letter.Letter("a",1)
b=letter.Letter("b",1)
c=letter.Letter("c",1)
d=letter.Letter("d",1)
A=letter.Letter("a",-1)
B=letter.Letter("b",-1)
C=letter.Letter("c",-1)
D=letter.Letter("d",-1)
    
def test_letter():
    print a.compare_to(A)
    print a.compare_letter(A)
    print a.sum(A).__str__()
    print a.is_single()
    print a.is_trivial()
    print a.__str__()
    new_a= a.find_inverse()
    print new_a.__str__()
    e=letter.Letter("e",3)
    print e.find_head_tail().__str__()
    print e.find_middle().__str__()
    
def test_rootList():
    root=root_list.RootList([],None)
    root.add_last(a)
    root.add_last(b)
    root.add_last(A)
    root.add_last(B)
    root.add_last(c)
    root.add_last(d)
    root.add_last(C)
    root.add_last(D)
    print root.__str__()
    root.update_pointer(A)
    print root.next().__str__()

def test_word():
    identity=word.Word([])
    identity.append_letter(a)
    identity.append_letter(b)
    identity.append_letter(A)
    identity.append_letter(B)
    identity.append_letter(c)
    identity.append_letter(d)
    identity.append_letter(C)
    identity.append_letter(D)
 

    test1=word.Word([])
    test1.append_letter(d)
    test1.append_letter(c)
    test1.append_letter(A)
    test1.append_letter(b)
    identity.append_word(test1)
    print identity.__str__()
    test=identity.reduce()
    print test.__str__()
    
#test_letter()
#test_rootList()
test_word()
