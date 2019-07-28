# *args - gathers remaining arguments as a tuple
# if we pass *args as a parameter, we can pass any number of arguments in function call


def check(num,*args):
    print(num)
    for i in args:
        if i.lower() == "purple":
            return True
        return False

print(check("purple","PURPLE","ppl"))