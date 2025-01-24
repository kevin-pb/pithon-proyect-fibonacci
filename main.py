try:
    print("Introduce the  limit of the fibonacci secunece: \n")

    data_enter = int(input("- "))

    number = 1

    fibonacci_secunce = []

    while number < data_enter:
    
        fibonacci_secunce.append(number)
    
        number += number
    
    print(fibonacci_secunce)  

except ValueError:
    print("You have not enter a entegeer number")
  