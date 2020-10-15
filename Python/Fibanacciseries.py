def fib():     #a function namely fib
    a, b=0, 1       #2 variables a and b while values 0 and 1 respectively
    while True:      #Until the condition is true the loop will continue (This is an Infinite loop)
        yield a      
        a, b = b, a+b   #2 variables a and b are now equal to b and a+b respectively
for f in fib():         #we iterate a loop through the function fib
    if f > 50:          #and if the function value at any point is 50, stop the loop
        break  
    print(f)      
