# The purpose of this exercise is to have a contact list on which a user can perform different operations, Edit, display,etc
# The contact details are stored in a list of dictonaries, named Contact_list
Contact_list = [{'name':'Anthony Reed','number':'0000000001','email':'a@gmail.com'},
                {'name':'Thomas more','number':'0000000002','email':'t@gmail.com'},
                {'name': 'Alice Chapel', 'number': '0000000003', 'email': 'c@gmail.com'},
                {'name': 'Kangroo Khan', 'number': '0000000004', 'email': 'k@gmail.com'}]
print('The Contact Details are: ', Contact_list) #printing contact details so user can see what are the stored contacts
end ='False' # Creating a 'end' flag and setting its value to False so that while loop will use this flag
while end != 'True':
    User_function = input ('\n''To display the contacts by name press d, by number press n, to Edit press e, to exit press x: ')
    #Getting user input to indicate which function he/she wants to perform on contacts, display by name or number, edit, or exit
    if User_function == 'd': # if user want to display contact by name
        for x in Contact_list:
            print(x['name']) # print all the contacts name
    elif User_function == 'n': # if user want to display contacts by number
        for k in Contact_list:
            print(k['number'])# print all the numbers
    elif User_function == 'e': # if the user wants to edit the contacts
        print('The contacts that can be edited are following: ') # display the list of contacts that can be editted
        for x in Contact_list:
            print(x['name'])
        Edit_menu= input('To Edit a contact Enter the name of the contact: ') # user input to indicate the name of contact that needs to be edited
        if Edit_menu == 'Anthony Reed': # if user want to edit the first contact
            print(Contact_list[0]) # display the current contact detials to the user
            Edit_option = input('To Edit name press 1, To Edit number press 2, To Edit email press 3: ') # ask user what to edit, name,number,email
            if Edit_option == '1': # logic for editing the name
                newname= input('Please enter the new name: ')
                Contact_list[0]['name'] = newname
                print(Contact_list) # printing the new contact list after the edit
            elif Edit_option == '2':# logic for editing the number
                newnum = input('Please enter the new number: ')
                Contact_list[0]['number'] = newnum
                print(Contact_list) # printing the new contact list after the edit
            elif Edit_option == '3':# logic for editing email
                newem = input('Please enter the new email: ')
                Contact_list[0]['email'] = newem
                print(Contact_list) # printing the new contact list after the edit
        elif Edit_menu == 'Thomas more':# same logic as above for second member in contact list
            print(Contact_list[1])
            Edit_option = input('To Edit name press 1, To Edit number press 2, To Edit email press 3: ')
            if Edit_option == '1':
                newname = input('Please enter the new name: ')
                Contact_list[1]['name'] = newname
                print(Contact_list)
            elif Edit_option == '2':
                newnum = input('Please enter the new number: ')
                Contact_list[1]['number'] = newnum
                print(Contact_list)
            elif Edit_option == '3':
                newem = input('Please enter the new email: ')
                Contact_list[1]['email'] = newem
                print(Contact_list)
        elif Edit_menu == 'Alice Chapel':# same logic as above for third member in contact list
            print(Contact_list[2])
            Edit_option = input('To Edit name press 1, To Edit number press 2, To Edit email press 3: ')
            if Edit_option == '1':
                newname = input('Please enter the new name: ')
                Contact_list[2]['name'] = newname
                print(Contact_list)
            elif Edit_option == '2':
                newnum = input('Please enter the new number: ')
                Contact_list[2]['number'] = newnum
                print(Contact_list)
            elif Edit_option == '3':
                newem = input('Please enter the new email: ')
                Contact_list[2]['email'] = newem
                print(Contact_list)
        elif Edit_menu == 'Kangroo Khan': # same logic as above for last member in contact list
            print(Contact_list[3])
            Edit_option = input('To Edit name press 1, To Edit number press 2, To Edit email press 3: ')
            if Edit_option == '1':
                newname = input('Please enter the new name: ')
                Contact_list[3]['name'] = newname
                print(Contact_list)
            elif Edit_option == '2':
                newnum = input('Please enter the new number: ')
                Contact_list[3]['number'] = newnum
                print(Contact_list)
            elif Edit_option == '3':
                newem = input('Please enter the new email: ')
                Contact_list[3]['email'] = newem
                print(Contact_list)
    elif User_function == 'x': # logic, if user want to end the function then terminate it
        break
    else: # If user has given an initial wrong input then promt the user to enter a valid option
        print("Please enter a Valid option")
        end='False'



