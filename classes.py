class Base(object):
    name = 'Base'

    def __str__(self):
        return self.name

class Hoge(Base):
    name = 'Hoge'

    def __str__(self):
        return self.name



