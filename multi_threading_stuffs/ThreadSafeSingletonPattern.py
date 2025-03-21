class SingletonParent(object):
    _instance = None

    # def __call__(cls, *args, **kwargs):
    #     if cls not in cls._instance:
    #         cls._instance[cls] = super(SingletonParent, cls).__call__(cls, *args, **kwargs)
    #     return cls._instance[cls]

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonParent, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class SingletonChild(SingletonParent):
    cache = None

    def lalaland(self):
        self.cache = "Guddi Faad Dunga"


if __name__ == '__main__':
    obj1 = SingletonChild()
    obj2 = SingletonChild()

    print(id(obj1))
    print(id(obj2))

    obj1.lalaland()
    print(obj1.cache)
    print(obj2.cache)

