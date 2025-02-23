# Luis Jimenez
# Input
# Asks for a number

counter = 0
doLoop = True

while doLoop and counter < 3:

    usr_input = input("Do you want to test the parity of a number? (Y for yes, N for no): ")

    if usr_input == 'Y' or usr_input == 'y':

        number_ = int(input("Enter A Positive Integer: "))
# Process
        if number_ % 2 == 0:
            print("Your number is Even")
        else:
            print("Your number is Odd")
    elif usr_input == 'N' or usr_input == 'n':
        doLoop = False
    else: 
        if counter < 2:
            print("INVALID ENTRY. Try again.")
        counter = counter + 1
if counter == 3:
    print("Too many bad entries. Goodbye.")
else:
    print("Program has stopped")
