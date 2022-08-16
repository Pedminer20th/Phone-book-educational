contacts = []
print("""choose a number
1:Add
2:List
3:Search
4:Number edit
0:Exit""")
choice = input("Enter your choice : ")
while choice != '0':
    if choice == '1':
        name = input("Enter the name : ")
        mobile = input("Enter the number : ")
        contact = [name, mobile]
        contacts.append(contact)
    if choice == '2':
        print("your current list is : ", contacts)
    if choice == '3':
        search = input("Enter the name for search : ")
        for i in range(len(contacts)):
            if contacts[i][0] == search:
                print("The result is : ",
                      contacts[i][0], " : ", contacts[i][1])
    if choice == '4':
        print("heres your list :", contacts)
        change = input("Enter the contact you want to edit : ")
        for i in range(len(contacts)):
            if contacts[i][0] == change:
                print("Heres the old number : ", contacts[i][1])
                new_number = input("Enter the new number : ")
                contacts[i][1] = new_number
    print("""choose a number
    1:Add
    2:List
    3:Search
    4:Number edit
    
    0:Exit""")
    choice = input("Enter your choice: ")
