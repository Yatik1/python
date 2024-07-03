def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")  # format string
        
        
print_kwargs(FirstName="Yatik" , surName = "Srivastava")
print_kwargs(age=21)
print_kwargs(name="Yatik Srivastava" , age=21,occupation = "unemployed")