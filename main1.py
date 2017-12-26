from requestutil import POST, GET, get_request_method_obj
from multipledispatch import dispatch
from functools import partial

namespace = dict()
dispatch = partial(dispatch, namespace=namespace)

@dispatch(POST)
def handle_request(method):
    print('Request Method is POST')

@dispatch(GET)
def handle_request(method):
    print('Request Method is GET')

@dispatch(object)
def handle_request(method):
    print('Request Method is not POST or GET')

def main():
    get = get_request_method_obj('GET')
    post = get_request_method_obj('POST')

    handle_request(get)
    handle_request(post)
    handle_request(None)


if __name__ == '__main__':
    main()
