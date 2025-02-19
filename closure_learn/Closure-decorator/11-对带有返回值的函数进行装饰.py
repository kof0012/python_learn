def set_func(func):
    print("---开始进行装饰")

    def call_func(*args, **kwargs):
        print("---这是权限验证1----")
        print("---这是权限验证2----")
        # func(args, kwargs)  # 不行，相当于传递了2个参数 ：1个元组，1个字典
        return func(*args, **kwargs)  # 拆包

    return call_func


@set_func  # 相当于 test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print("-----test1----%d" % num)
    print("-----test1----", args)
    print("-----test1----", kwargs)
    return "ok"


@set_func
def test2():
    pass


ret = test1(100)
print(ret)

ret = test2()
print(ret)
