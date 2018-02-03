password= input("Please select your password:") # asking user to enter a password
lencheck= len(password) # variable to store the length of password that will be used for validation
a = ['$','@','!','*'] # a list that contains special characters that will be used for validation
checklen = False # flag that will be set true if the length of password is between 6 and 16
checknumeric = False #flag that will be set true if the password contians atleast 1 number and 1 alphabet
checspecial = False #flag that will be set true if the password contians special character
speicalcharacter_count = 0 # count to see # of special character in password
check_upper_lower = False #flag that will be set true if the password contians atleast 1 lowecase and 1 upercase letter
Done = False # #flag that will be set true once all the validation checks are met
while Done != True : # logic for password validation
    while checklen != True: # logic to validate the password is between 6 and 16
        if lencheck < 6:
            print("The password you entered is too short, the length should be between 6 and 16")
            password = input("Please select your password:")
            lencheck = len(password)
        elif lencheck > 16:
            print("The password you entered is too long, the length should be between 6 and 16")
            password = input("Please select your password:")
            lencheck = len(password)
        else:
            checklen == True # if the password is within allowed length turn the flag true
            break

    while checknumeric != True : # logic to validate the password contians at least 1 number and 1 alphabet
        if password.isalpha()==True:
            print("The password you entered is not valid, it should contain atleast 1 number")
            password = input("Please select your password:")
            lencheck = len(password)
        elif password.isnumeric()==True :
            print("The password you entered is not valid, it should contain atleast 1 alphabet")
            password = input("Please select your password:")
            lencheck = len(password)
        else:
            checknumeric = True # if the condition is met turn the flag true
            break
    while checspecial != True: # logic to validate the password contians atleast 1 special character
        for x in a:
            if x in password:
                speicalcharacter_count +=1

        if speicalcharacter_count == 0:
                print("The password should contain atleast one of following special characters: $, @, ! or * ")
                password = input("Please select your password:")
                lencheck = len(password)
        else:
            checspecial == True # if condition is met set the flag to True
            break

    while check_upper_lower != True: # logic to validate the password contians atleast 1 uppercase and 1 lowercase letter
        if password.islower()== True:
            print("The password you entered is not valid, it should contain atleast 1 upper case letter")
            password = input("Please select your password:")
            lencheck = len(password)
        elif password.isupper()==True:
            print("The password you entered is not valid, it should contain atleast 1 lowercase letter")
            password = input("Please select your password:")
            lencheck = len(password)
        else:
            check_upper_lower = True # if condition is met set the flag to Tru
            break

    print("congradulations you have entered a valid password") # print conformation message to user
    Done = True # Flag set to true to indicate that all the password validations are done
    break
