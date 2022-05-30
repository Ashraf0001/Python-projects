def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 5
print("The factorial of", num, "is", factorial(num))


def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#Think of this pizza delivery store


#Sometimes the logic behind recursion is hard to follow through.
#Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
#Recursive functions are hard to debug.

