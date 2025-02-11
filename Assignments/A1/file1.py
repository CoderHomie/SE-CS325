def math_func(func):
    def wrapper(*args):
        print(str(args[0]) + " + " + str(args[1]) + " = " + str(args[0] + args[1]))
        func(args[0], args[1])
    return wrapper


@math_func
def addition(x, y):
    return x + y

def main():
    addition(1,2)

if __name__ == "__main__":
    main()