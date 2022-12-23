def singleton(cls):
    def wrapped(*args, **kwargs):
        if cls.tmp is None:
            instance = cls(*args, **kwargs)
            cls.tmp = instance
            return instance
        return cls.tmp

    cls.tmp = None
    return wrapped


@singleton
class Example:
    pass


obj = Example()
another_obj = Example()

print(id(obj))
print(id(another_obj))

print(obj is another_obj)
