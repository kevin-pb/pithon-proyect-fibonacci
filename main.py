try:
    print("Introduce the  limit of the fibonacci secunece: \n")

    data_enter = int(input("- "))

    fibonacci_secunce = [0, 1, 1, 2]

    while fibonacci_secunce[-1] < data_enter:
    
        fibonacci_secunce.append(fibonacci_secunce[-1] + fibonacci_secunce[-2])
    
    print(fibonacci_secunce)  

except ValueError:
    print("You have not enter a entegeer number")
  