def small_func(n):
    for i in range(n):
        print(i)



def main_func(func,*args, **kwargs):
    print("hello world")
    func(args[0])
    print("end of program")


main_func(small_func,10)