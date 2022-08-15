contacts = []
print("""choose a number
1:Add
2:List
3:Search
0:Exit""")
choice = input("Enter your choice : ")
while choice != '0' :
    if choice == '1' :
        name = input("Enter the name : ")
        mobile = input("Enter the number : ")
        contact = [ name , mobile ]
        contacts.append(contact)
    elif choice == '2' :
        print("your current list is : "contacts)
    elif choice == '3' :
        search = input("Enter the name for search : ")
        for i in range (len(contacts)) :
            if contacts [i][0] == search :
                print("The result is : "contacts [i][0] , " : " , contacts[i][1])
    print("""choose a number
    1:Add
    2:List
    3:Search
    0:Exit""")
    choice = input("Enter your choice : ")
