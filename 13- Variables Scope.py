# Global variables can be used anywhere
# Local variables can only be used under its related function


a = 56  # Global Variable
def func1():
    global b    # Global declearation
    b = 90  
    print(b)
    print("a under funct1:",a)
func1()


def func2():
    c = 80  # Local Variables
    print(c)
    print(b)
    print("a under funct2: ",a)
func2()
