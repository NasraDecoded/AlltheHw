def make_country(name, capital): #Define a function that takes two inputs: name and capital
    country = {"name":name,      #Create a dictionary and store the value of name under the key "name"
            "capital" :capital}  #Store the value of capital under the key "capital"   
    print(country)               # Print the whole dictionary so we can see it works
make_country("sweden", "Stockholm")   # Call the function with Sweden and Stockholm