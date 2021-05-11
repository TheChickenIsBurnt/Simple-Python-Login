# definitions

def pausepy():
  input(" ")

# welcome screen

print("Welcome to the login. Please press enter to continue.")
pausepy()

# login

user_name = input("username: ")
if user_name == "your username":
  pass_word = input("password: ")
  if pass_word ==  "your password":
    print("You have succesfully logged in!")
    pausepy()

    # put anything you want after the succesful login.
  else:
    print("INCORRECT PASSWORD! PLEASE RESTART.")
    pausepy()
else:
  print("INCORRECT USERNAME! PLEASE RESTART.")
  pausepy()



