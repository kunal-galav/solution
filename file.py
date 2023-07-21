# check if the input contains any digit or numbers , or special characters
# if Input has numbers or special characters : print invalid input , and prompt for try again
# try getting input 10 times , if user doesn't input valid entry till 10th time , close the program and ask them to try again later.

username = input("What is you name? ")
if(username.isdigit()):
    print("the given input is digit")
elif (username.isalpha()):
    print(username)
else:
    print("the given input is special character")

