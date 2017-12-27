from multipledispatch import dispatch
from functools import partial

n1 = 21
n2 = 15
n3 = 37
n4 = 67

class Between0To10(object):
    pass

class Between10To20(object):
    pass

class Between20To30(object):
    pass

class Between30To40(object):
    pass

def check_num(num):
    if num >= 0 and num < 10:
        return Between0To10()
    elif num >= 10 and num < 20:
        return Between10To20()
    elif num >= 20 and num < 30:
        return Between20To30()
    elif num >= 30 and num < 40:
        return Between30To40()

namespace = dict()
dispatch = partial(dispatch, namespace=namespace)

@dispatch(Between0To10)
def print_status(obj):
    print('number is between 0 to 10')
    print('Pretty much young number!!')

@dispatch(Between10To20)
def print_status(obj):
    print('number is between 10 to 20')
    print('The Peak of the youth!!!')

@dispatch(Between20To30)
def print_status(obj):
    print('number is between 20 to 30')
    print('Working Hard X)')

@dispatch(Between30To40)
def print_status(obj):
    print('number is between 30 to 40')
    print('A little Tired......')

@dispatch(object)
def print_status(obj):
    print('number is over 40 or less than 0')

def main():
    nums = {
        'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4,
    }

    for k, v in nums.items():
        print('{0} is {1}'.format(k, v))
        print_status(check_num(v))

#def check_num(num):
#    if num >= 0 and num < 10:
#        print('number is between 0 and 10')
#    elif num >= 10 and num < 20:
#        print('number is between 10 and 20')
#    elif num >= 20 and num < 30:
#        print('number is between 20 and 30')
#    elif num >= 30 and num < 40:
#        print('number is between 30 and 40')
#    elif num >= 40:
#        print('number is over 40')
#
#def main():
#    print('n1 is {}'.format(n1))
#    check_num(n1)
#    print('n2 is {}'.format(n2))
#    check_num(n2)
#    print('n3 is {}'.format(n3))
#    check_num(n3)
#    print('n4 is {}'.format(n4))
#    check_num(n4)


if __name__ == '__main__':
    main()
