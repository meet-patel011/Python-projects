email = input("Enter your Email: ") #g@g.in
j = 0
k = 0
d = 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@") == 1):
            if (email[-3] == ".") ^ (email[-4] == "."):
                for i in email:
                    if i == i.isspace():
                        j = 1
                    elif i.isalpha():
                        if i == i.upper():
                            k = 1
                    elif i.isdigit():
                        continue
                    elif i == "@" or i == "_" or i == ".":
                        continue
                    else:
                        d=1      
                if (j == 1) or (k == 1) or (d == 1):
                    print("Invalid Email")
                else:
                    print("Valid Email")        
            else:
                print("Invalid Email")                
        else:
            print("Invalid Email")     
    else:
        print("Invalid Email")                 
else:
    print("Invalid Email") 
