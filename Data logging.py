VisitorName = input("Enter a name of visitor:\n ")
Phone_No = int(input("Enter A Phone Number of Visitor:\n "))
VisitorAddress = input("Visitor Address:\n ")
VisitorBody_Temp = int(input("Enter Body Temperature in Integer: \n"))
enter = ("\n")

for data in (VisitorName, Phone_No, VisitorAddress, VisitorBody_Temp, enter):
    if data == '' :
        f = open("Visitor_info.txt", "w")
        f.writelines(data + "\t")
    elif data == data:
        f = open("Visitor_info.txt", "a")
        f.writelines(str(data) + "\t")
    else:
        f = open("Visitor_info.txt", "r")
        f.read(data)
f.close()