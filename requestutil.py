class POST(object):
    name = 'POST'

    def __str__(self):
        return self.name

class GET(object):
    name = 'GET'

    def __str__(self):
        return self.name

def get_request_method_obj(method):
    cls = globals()[method]
    instance = cls()
    return instance
