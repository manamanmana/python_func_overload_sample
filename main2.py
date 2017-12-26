from classes import Hoge
from multipledispatch import dispatch
from functools import partial

namespace = dict()
dispatch = partial(dispatch, namespace=namespace)

@dispatch(Hoge)
def handle(obj, fuga=None):
    print(obj.name, end=' : ')
    print('Kwarg fuga is {0}'.format(fuga))

@dispatch(type(None))
def handle(obj):
    print('None has been passed.')

hoge = Hoge()
handle(hoge, fuga="Hello")
handle(None)



