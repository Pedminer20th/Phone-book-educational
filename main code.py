# V_DEMO

contacts = []
print("""choose an option :
Add:Add a contact (name and mobile)
List:show the current List
Search:Search via name
Edit:Number edit
Delete:Dlete a contact
Exit:Exit the program""")
choice = input("Enter your choice : ")
while choice != 'Exit':
    if choice == 'Add':
        name = input("Enter the name : ")
        mobile = input("Enter the number : ")
        contact = [name, mobile]
        contacts.append(contact)
    elif choice == 'List':
        print("your current list is : ", contacts)
    elif choice == 'Search':
        search = input("Enter the name for search : ")
        for i in range(len(contacts)):
            if contacts[i][0] == search:
                print("The result is : ",
                      contacts[i][0], " : ", contacts[i][1])
    elif choice == 'Edit':
        print("heres your list :", contacts)
        change = input("Enter the contact you want to edit : ")
        for i in range(len(contacts)):
            if contacts[i][0] == change:
                print("Heres the old number : ", contacts[i][1])
                new_number = input("Enter the new number : ")
                contacts[i][1] = new_number
    elif choice == 'Delete' :
        print(contacts)
        dlt = input("which one do you want to delete : ")
        for i in range (len(contacts)-1 , -1 , -1) :
            if contacts[i][0] == dlt or contacts[i][1] == dlt :
                del contacts[i]         
    else :
        print("Choose wisely !!! ")
    print("""choose an option :
    Add:Add a contact (name and mobile)
    List:show the current List
    Search:Search via name
    Edit:Number edit
    Exit:Exit the program""")
    choice = input("Enter your choice : ")
