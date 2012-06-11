class BaseModel(object):

    @classmethod
    def init(cls, **kwargs):
        instance = cls()
        instance.data = kwargs
        return instance

    def __getattr__(self, name):
        return self.data.get(name, None)

    def to_dict(self):
        return self.data
