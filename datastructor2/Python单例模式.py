#coding: utf8

#############################################################类实现单例模式
class Singleton(object):
	__instance = None
	def __init__(cls, *args, **kwargs):
		pass

	def __new__(cls, *args, **kwargs):
		if Singleton.__instance is None:
			Singleton.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
		return Singleton.__instance

class MyClass(Singleton):
	def __init__(self):
		print("Myclass->init method is called!")

##############################################################使用装饰器实现的单例模式
def singleton(cls):
    instance = {}
    def decorator(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return decorator

@singleton
class DecoratorClass():
	def __init__(self):
		print("Decorator->init methed called!")


if __name__ == '__main__':
	print("类实现的单例模式：")
	mc = MyClass()
	mc2 = MyClass()
	print(id(mc))
	print(id(mc2))
	print("装饰器实现的单例模式：")
	dc = DecoratorClass()
	dc2 = DecoratorClass()
	print(id(dc))
	print(id(dc2))
