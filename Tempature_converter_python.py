#function to ask the name of the person. It will continue to run
def name_finder():
    while True:
        #while true it will run asking the perosn for their name. The out is 404 (get it?)
        #If the user enters empt space or trys to skip it will let them knoow they can not do that and as them to try again.
        first_name = input("What is your first name? (type in 404 to escape) ")
        if len(first_name.strip()) < 1:
             print("You didn't not enter your first name. Let's try again")
             continue
        elif first_name.strip() == "404":
            print("Aww, you didn't want to finish playing? Oh well have a nice day! Goodbye!")
            break
        else:
             print('Hi', first_name+'!')

        while True:
            #ask teh user for their last name and goes thrugh a similar process as the first do while loop
              last_name = input("What is your last name? (type in 404 to escape) ")
              
              if len(last_name.strip()) < 1:
                 print("You didn't not enter your last name. Let's try again")
                 continue
              elif last_name.strip() == "404":
                print("Aww, you didn't want to finish playing? Oh well have a nice day! Goodbye!")
                break
              else:
##                print('Hi', last_name+'!')
                print(last_name)
                name=first_name+ ' ' +last_name
                print('Hi', name+'!')
                return(name)
#finds if the input is a number or not. If it is a number it will return the number as a float. If not it will return None
def is_numeric_basic(s):
    match = s 
    # Remove a leading negative sign if it exists
    if s.startswith('-'):
        #this will remove the first character of the string if it is a negative sign
        s = s[1:]
    # Remove the first decimal point and check if only digits remain
    #replace('.', '', 1) will remove the first decimal point in the string and then isdigit() will check if the remaining characters are all digits. If they are, it will return True. If not, it will return False.
    if (s.replace('.', '', 1).isdigit() and s != '' )== True:
        return(float(match))
    else:
        print("You did not enter a valid number. Please try again.")
        return None
#function to convert celcius to farenheit. It will continue to run until the user enters a valid number or types in leave                   
def celcius(fname):
    while True:
        tempc = input("Hey " + fname + ", what is the temperature in Celcius? ")
        tempc = is_numeric_basic(tempc)
        if tempc != None:
                tempc = float(tempc)
                faren = (tempc * 9/5) + 32
                print(tempc, "degrees Celcius is equal to", faren, "degrees Farenheit.")
                return(faren)
        elif tempc == None:

            continue
        elif tempc.strip().lower() == "leave":
                print("Aww, come on " + fname + ", you didn't want to finish playing? Oh well have a nice day! Goodbye!")
                break
#function to convert farenheit to celcius. It will continue to run until the user enters a valid number or types in leave       
def farenheit(fname):
     while True:
            tempf = input("Hey" + fname + ", what is the temperature in Farenheit? ")
            tempf = is_numeric_basic(tempf)
            if tempf != None:
                    tempf = float(tempf)
                    celci = (tempf - 32) * 5/9
                    print(tempf, "degrees Farenheit is equal to", celci, "degrees Celcius.")
                    return(celci)
            elif tempf == None:

                continue
            elif tempf.strip().lower() == "leave":
                    print("Aww, come on " + fname + ", you didn't want to finish playing? Oh well have a nice day! Goodbye!")
                    break
#function to ask the user what system they would like to use. It will continue to run until the user enters a valid system or types in 404 to escape            
def final_product(fname):
    while True:
        system = input("Hey " + fname+", what system would you like to use? (C)elcius or (F)arenheit? Or type in 404 to escape ")
        if system.strip().lower() == "c":
            cel_ending = celcius(fname)
            print(cel_ending)
            return(cel_ending)
        elif system.strip().lower() == "f":
            far_ending = farenheit(fname)
            print(far_ending)
            return(far_ending)
        elif system.strip() == "404":
            print("Aww, come on " + fname + ", you didn't want to finish playing? Oh well have a nice day! Goodbye!")
            break
        else:
            print(fname + ", you did not enter a valid system. Please try again.")
            continue
#runs the name_finder function and then runs the final_product function with the name as an argument. It will continue to run until the user types in 404 to escape or types in any other character to leave.
final_name = name_finder()
while True:
     #if the final_name is not None it will run the final_product function with the name as an argument. If it is None it will break the loop and end the program.
     if final_name is not None:
                final_product(final_name)
     else:
         break
     #it will ask the user if they want to change the name. If they enter Y it will run the name_finder function again. If they enter N it will continue to run the final_product function with the same name. If they enter any other character it will break the loop and end the program.
     repeat = input("Change the name? (Y/N/any char to leave) ")
     if repeat.strip().lower() == "y":
        final_name = name_finder()
     elif repeat.strip().lower() == "n":
       continue
     else:
        print("Aww, come on " + final_name + ", you didn't want to finish playing? Oh well have a nice day! Goodbye!")
        break
   
