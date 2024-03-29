while True:
    list = ["somerthing","smssss","sssss"]

    class Format:
        end = '\033[0m'
        underline = '\033[4m'

    def view():
        print(Format.underline + 'Your To-do list' + Format.end)
        for i, item in enumerate(list,1):
            print(str(i)+'.',item)
            

    def add(x):
        level = input("what is the priority level?(1-3): ") #level 3 is the least highest priority
        if level == '1':
            list.insert(0,x)
            
        elif level == '2':
            length = len(list)/2
            rounded = int(round(length))
            if len(list) == 1:
                list.append(x)
            if rounded >= 1:
                list.insert(rounded,x)
                
        elif level == '3':
            list.append(x)
            
        else:
            print("invalid option")
            exit()
            
        view()
        
    def remove(x):
        list.pop(x)
        view()

    options = input("What do you want to do?(a,r,v): ").lower() #a for adding to list, r for removing from list, v for viewing list

    if options == "a".lower():
        view()
        x = input("what would you like to add to the list?: ")
        if not x:
            print("cannot be empty")
            exit()
        elif x in list:
            print(f'"{x}" is already in to do list')
            exit()
        add(x)
        
    elif options == "r":
        view()
        try:
            x = int(input('which element would you like to remove from your to do list?(enter the number): '))
            if not x:
                print("cannot be empty")
                exit()
            remove(x-1)
        except ValueError:
            print("must be element number of item in the list")
            exit()
            
    elif options == 'v':
        view()
        
    else:
        print("invalid option")
        exit()

