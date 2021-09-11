number = int(input("adad ra vared konid: "))
if number > 1:
    for i in range(2,number//2):
        if (number % i)==0:
            print("adad vared shodeh aval nist :( ")
            break
        else:
            print("adad vared shodeh aval ast :) ")
            break
else:
    print("adad vared shodeh aval nist :( ")
