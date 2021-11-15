# Display a welcome message to Python theater and display another that shows the list of prices based on the age groups.
print("Welcome to Python theater! Here is a list of our ticket prices.")
print("Normal: $15\nChildren up to 12 years old: $8\nSeniors age 65 and above: $10")

# Display a message informing the user that 3D movies are available and what the surcharge is for them.
print("Here at Python theater we also show 3D movies. Each ticket will be an additional $3 for a 3D movie.")

# Create variables for the three different ticket prices which is $8 for children, $15 for normal price, and $10 for seniors.
children_ticket = 8
normal_ticket = 15
senior_ticket = 10

# Store the surcharge of $3 for the 3D movies in a variable.
three_d = 3

# Prompt the user for their age and if they are seeing a 3D movie. Store answers to each input into two separate variables. 
age = int(input("How old are you?\n"))
surcharge = input("Are you seeing a 3D movie today? enter Yes or No\n")

# Check if users age is less than or equal to 12 and check if the movie is 3D. Use .lower() so the input for surcharge isn't case sensitive.  
if age <= 12 and surcharge.lower() == "yes":
    print("Your total ticket cost is" ,children_ticket + three_d)
elif age <= 12 and surcharge.lower() == "no":
    print("Your total ticket cost is" ,children_ticket)

# Check if users age is greater than 12 and less than 65 for a normal ticket price. Also check if the movie is 3D. Use .lower() so the input for surcharge isn't case sensitive.
if age > 12 and age < 65 and surcharge.lower() == "yes":
    print("Your total ticket cost is" ,normal_ticket + three_d)
elif age > 12 and age < 65 and surcharge.lower() == "no":
    print("Your total ticket cost is" ,normal_ticket)
    
# Check if users age is greater than or equal to 65 and check if the movie is 3D. Use .lower() so the input for surcharge isn't case sensitive.
if age >= 65 and surcharge.lower() == "yes":
    print("Your total ticket cost is" ,senior_ticket + three_d)
elif age >= 65 and surcharge.lower() == "no":
    print("Your total ticket cost is ",senior_ticket)
