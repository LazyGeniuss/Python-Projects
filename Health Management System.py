# HEALTH MANAGEMENT SYSTEM
# this system keeps track of six file
# alex exe.txt
# alex diet.txt
# mike exe.txt
# mike diet.txt
# carol exe.txt
# carol diet.txt
# you can basically read or write data in above file using this program
def getdate():
    import datetime
    return datetime.datetime.now()

def log_data(h,g):
    if h == 1 and g == 1:
        with open("Alex exe.txt", "a") as a:
            inp = input("Enter the Exercise data of Alex\n")
            a.write(str(getdate()) + " " + inp + "\n")
    elif h == 1 and g == 2:
        with open("Alex diet.txt", "a") as a:
            inp = input("Enter the Diet data of Alex\n")
            a.write(str(getdate()) + " " + inp + "\n")
    elif h == 2 and g == 1:
        with open("Mike exe.txt", "a") as a:
            inp = input("Enter the Exercise data of Mike\n")
            a.write(str(getdate()) + " " + inp + "\n")
    elif h == 2 and g == 2:
        with open("Mike diet.txt", "a") as a:
            inp = input("Enter the Diet data of Mike\n")
            a.write(str(getdate()) + " " + inp + "\n")
    elif h == 3 and g == 1:
        with open("Carol exe.txt", "a") as a:
            inp = input("Enter the Exercise data of Carol\n")
            a.write(str(getdate()) + " " + inp + "\n")
    elif h == 3 and g == 2:
        with open("Carol diet.txt", "a") as a:
            inp = input("Enter the Diet data of Carol\n")
            a.write(str(getdate()) + " " + inp + "\n")
    else:
        print("Invalid Input")

def retrieve_data(h,g):
    if h == 1 and g == 1:
        with open("Alex exe.txt") as a:
            print(a.read())
    elif h == 1 and g == 2:
        with open("Alex diet.txt") as a:
            print(a.read())
    elif h == 2 and g == 1:
        with open("Mike exe.txt") as a:
            print(a.read())
    elif h == 2 and g == 2:
        with open("Mike diet.txt") as a:
            print(a.read())
    elif h == 3 and g == 1:
        with open("Carol exe.txt") as a:
            print(a.read())
    elif h == 3 and g == 2:
        with open("Carol diet.txt") as a:
            print(a.read())
    else:
        print("Invalid Input")

print("\t\t\tHEALTH MANAGEMENT SYSTEM\t\t\t\n")

while 1:
    i = int(input("Enter '1' to log the data or '2' to retrieve the or '0' to exit the program\n"))
    if i == 0:
        break
    h = int(input("Enter '1' for Alex, '2' for Mike, '3' for Carol\n"))
    g = int(input("Enter '1' for Exercise and '2' for Diet\n"))
    if i == 2:
        retrieve_data(h,g)
    elif i == 1:
        log_data(h,g)
    else:
        print("Invalid input")
print("You have exited the system")