#une fonction qui fait appel à elle mm tant 
#que la condition définie n est pas verifier

def my_function(k):
    if(k > 0):
        result = k + my_function(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\nRecursion Example Results:")
my_function(6)


