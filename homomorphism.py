import letter
import word
import copy
import math
def list_test(n):
    if n<0: return []
    if n==0:
        return ['0','1','2','3','4']
    else:
        new_list=[]
        for item in list_test(n-1):
            for i in range (5):
                new_item=item+str(i)
                new_list.append(new_item)
        return new_list

test=list_test(3)#0

def convert_word(let):
    return word.Word([let])


def generate_letter_list():
    a=letter.Letter("a",1)
    b=letter.Letter("b",1)
    c=letter.Letter("c",1)
    d=letter.Letter("d",1)
    A=letter.Letter("a",-1)
    B=letter.Letter("b",-1)
    C=letter.Letter("c",-1)
    D=letter.Letter("d",-1)
    return[a,b,c,d,A,B,C,D]

letter_list=generate_letter_list()#1

def zero_list():
    return [[word.Word([])]]

zero=zero_list()#2

def one_list():
    result=[]
    for item in letter_list:
        result.append([convert_word(item)])
    return result

one=one_list()#3


def two_list():
    result=[]
    for item1 in one:
        for item2 in letter_list:
            to_add=word.Word([])
            first=copy.deepcopy(item1[0])
            to_add.append_word(first)
            to_add.append_letter(item2)
            if not (to_add.is_identity()):
                result.append([to_add])
            del to_add
            del first
    return result   

two=two_list()#4
    
def three_list():
    result=[]
    for item1 in two:
        for item2 in letter_list:
            to_add=word.Word([])
            first=copy.deepcopy(item1[0])
            to_add.append_word(first)
            to_add.append_letter(item2)
            if (len(to_add.list)==3 or (len(to_add.list)==1 and abs(to_add.list[0].exp)==3) or (len(to_add.list)==2 and (abs(to_add.list[0].exp)+abs(to_add.list[1].exp))==3)):
                result.append([to_add])
            del to_add
            del first
    return result


three=three_list()#5

def four_list():
    result=[]
    for item1 in three:
        for item2 in letter_list:
            to_add=word.Word([])
            first=copy.deepcopy(item1[0])
            to_add.append_word(first)
            to_add.append_letter(item2)
            
            if(len(to_add.list)==4):
                result.append([to_add])
            elif to_add.sum_exp()==4:
                result.append([to_add])
            else: pass
            del to_add
            del first
    return result

four=four_list()#6
##for thing in four:
##    toPrint='['
##    for otherThing in thing:
##        toPrint+=otherThing.__str__()
##    toPrint+=']'
##    print toPrint
final=[]#7

def test_homomorphism(f_list):
    a=f_list[0]
    b=f_list[1]
    c=f_list[2]
    d=f_list[3]
    A=a.find_inverse()
    B=b.find_inverse()
    C=c.find_inverse()
    D=d.find_inverse()
    test=word.Word([])
    test.append_word(a)
    test.append_word(b)
    test.append_word(A)
    test.append_word(B)
    test.append_word(c)
    test.append_word(d)
    test.append_word(C)
    test.append_word(D)
    return test.is_identity()

def generate_length_based(length):
    if (len(length)==1):
        if(int(length)==0):return copy.deepcopy(zero)
        elif (int(length)==1):return copy.deepcopy(one)
        elif (int(length)==2):return copy.deepcopy(two)
        elif (int(length)==3):return copy.deepcopy(three)
        else: return four
    else:
        previous_list=generate_length_based(length[:len(length)-1])
        this_list=generate_length_based(length[len(length)-1])
        result=[]
        for thing1 in previous_list:
            for thing2 in this_list:
                to_add=copy.deepcopy(thing1)
                to_add.append(thing2[0])
                result.append(to_add)
        del previous_list
        del this_list
        return result
                   
    
      
def main():
##    for thing in test:
##        print thing
    for i in range (5):
        print test[6+i]
        result=generate_length_based(test[6+i])
        for thing in result:
            to_print="["
            for item in thing:
                to_print+=item.__str__()+"-- "
            to_print+="]"
            
            if test_homomorphism(thing):
                print to_print
## 
                
##    should_be_none=generate_length_based(test[0])
##    print len(should_be_none[0])
##    print test_homomorphism(should_be_none[0])
    
main()
    
        
    
