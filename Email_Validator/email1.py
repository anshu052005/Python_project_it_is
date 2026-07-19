email = input("Enter your Email : ")
#  abcd@xyz.com , anshu@gmail.com

j,k,d = 0,0,0
if len(email) >=6:
    # Hum check krenge ki email ka first character alphabet hai ya nahi.
    if email[0].isalpha():
        # Hum check krenge ki email mein sirf ek hi @ hai ya nahi.
        if ("@" in email) and (email.count("@") == 1):
            # Hum check krenge ki email mein sirf ek hi . hai ya nahi.
            # Yahaan humne xor operator ka use kiya hai.
            # Hum ye check kr rhe hai ki email ke last 4th and last 3rd position pe dot h ya nhi kyuki aksar dot ishi position pe rehta hai
            if (email[-4] == ".") ^ (email[-3] == "."):

                # above sare base cases check krne ke baad hum or loop lagake iterate krenge
                for i in email:
                    # sabse pehle hum dekhenge ki jo i hai ya humara charcter wo space h ki nhi kyuki space nhi hona chahiye email me
                    if i == i.isspace():
                        k=1
                    # nhi to kya wo ek alphabet hai
                    elif(i.isalpha()):
                        # agar alphabet hai to wo upper case nhi hona chahiye , agar wo upper case hai to hum j=1 kr denge jo further wrong email batayega
                        if i==i.upper():
                            j=1
                    elif (i.isdigit()):
                        # agar wo digit hai to continue kro
                        continue
                    elif (i=="_") or (i==".") or i=="@" :
                        # agar wo _ , . , @ hai to bhi continue kro
                        continue
                    else:
                        # agar inn sab ke alwa kuchh aur hai to invalid email hoga 
                        d=1
                    
                if(k==1) or (j==1) or (d==1):
                        print("Wrong Email")
                
            else:
                print("Wrong Email : dot issue")
        else:
            print("Wrong Email : Invalid email format")
    else:
        print("Wrong Email : Email should start with an alphabet")
    

else:
    print("Wrong Email : Email should be minimum 6 characters")


 
