#编写一个Dict类，这个类和dict一致，可以通过属性来访问。
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(rf"'Dict' object has no attribute {key}")

    def __setattr__(self, key, value):
        self[key] = value