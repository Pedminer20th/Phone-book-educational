# V_DEMO

contacts = []
print("""choose an option :
Add:Add a contact (name and mobile)
List:show the current List
Search:Search via name
Edit:Number edit
Exit:Exit the program""")
choice = input("Enter your choice : ")
while choice != 'Exit':
    if choice == 'Add':
        name = input("Enter the name : ")
        mobile = input("Enter the number : ")
        contact = [name, mobile]
        contacts.append(contact)
    if choice == 'List':
        print("your current list is : ", contacts)
    if choice == 'Search':
        search = input("Enter the name for search : ")
        for i in range(len(contacts)):
            if contacts[i][0] == search:
                print("The result is : ",
                      contacts[i][0], " : ", contacts[i][1])
    if choice == 'Edit':
        print("heres your list :", contacts)
        change = input("Enter the contact you want to edit : ")
        for i in range(len(contacts)):
            if contacts[i][0] == change:
                print("Heres the old number : ", contacts[i][1])
                new_number = input("Enter the new number : ")
                contacts[i][1] = new_number
    print("""choose an option :
    Add:Add a contact (name and mobile)
    List:show the current List
    Search:Search via name
    Edit:Number edit
    Exit:Exit the program""")
    choice = input("Enter your choice : ")
