def fibonacci(input):
    return sum_series(input)
   

def sum_series(input,input1=0,input2=1):

    if input == 0:
         return 0
    elif input == 1:
        return 1
    else:
         return sum_series(input-1,input1,input2) + sum_series(input-2,input1,input2)