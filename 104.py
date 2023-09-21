n = [10, 11, 12, 13, 14, 15]
l = ['A', 'B', 'C', 'D', 'E', 'F']

def hex2int(s1):
    
    if s1 in l:
        index = l.index(s1) 
        return 10 + index 
    else:
        return s1    


def int2hex(s2):

    if s2 in n:
        index = n.index(s2)
        return l[index]
    else:
        return s2


def main():
    s1_ = input('Введите число в 16-ричной системе: ').capitalize()
    s2_ = int(input('Введите число в 10-тичной системе: '))
    print(hex2int(s1_))
    print(int2hex(s2_))
main()    