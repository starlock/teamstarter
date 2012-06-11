class BaseModel(object):

    @classmethod
    def init(cls, **kwargs):
        instance = cls()
        for key, value in kwargs.iteritems():
            setattr(instance, key, value)
        return instance

    def to_dict(self):
        ret = {}
        for key in self.properties:
            ret[key] = getattr(self, key, None)
        return ret
