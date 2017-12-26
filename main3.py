from multipledispatch import dispatch
from functools import partial

namespace = dict()
dispatch = partial(dispatch, namespace=namespace)

@dispatch(str)
def handle(arg):
    print(arg)

@dispatch(int, int)
def handle(x, y):
    print('This "handle(x, y)" func takes 2 int args and return the sum.')
    print('{0} + {1} = {2}'.format(x, y, (x + y)))

handle(1, 2)
handle('Hello this "handle(arg)" func only takes 1 str arg.')
