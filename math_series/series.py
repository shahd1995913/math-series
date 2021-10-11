


def  Lucas(input) :

    # if input ==  0 :

    #     return 2
    # elif input  == 1 :

    #     return 1

    # else :

    #      return  Lucas(input-1) +  Lucas(input-2)


    return  sum_series(input,2,1)


def fibonacci(input) :


#   if input == 0:

#         return 0



#   elif input == 1:

#         return 1

#   else :

#         return fibonacci(input-1) + fibonacci(input-2)




    return  sum_series(input)
   

def sum_series(input,input1=0,input2=1):

    if input == 0:

         return input1

    elif input == 1:

        return input2

    else:
         return sum_series(input-1,input1,input2) + sum_series(input-2,input1,input2)