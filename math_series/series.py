
def  Lucas(input) :
    """ 
Lucas function that take input and send it to anther function 
called  sum_series.
Lucas numbers  defined as the sum of its two.
But here the first two terms are 2 and 1.
 
"""

    # if input ==  0 :

    #     return 2
    # elif input  == 1 :

    #     return 1

    # else :

    #      return  Lucas(input-1) +  Lucas(input-2)


    return  sum_series(input,2,1)


def fibonacci(input) : 
    """ 
A Fibonacci sequence is integer sequence of 0, 1, 1, 2, 3, 5, 8....
fibonacci function that take input and send it to anther function 
called  sum_series


"""





#   if input == 0:

#         return 0



#   elif input == 1:

#         return 1

#   else :

#         return fibonacci(input-1) + fibonacci(input-2)




    return  sum_series(input)
   

def sum_series(input,input1=0,input2=1):
    """ 
 sequence up to n-th term
by function called a sum_series that takes a 3 parameter input from the 
Fibonacci and Lucas functionsn """

    if input == 0:

         return input1

    elif input == 1:

        return input2

    else:
         return sum_series(input-1,input1,input2) + sum_series(input-2,input1,input2)