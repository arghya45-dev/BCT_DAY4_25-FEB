# #Task:  User Sign-up/login info
# 1.create empty array
# 2.create dictionary for each user containing name,email Id,password.
# 3.user will put data during Sign-up 
# 4.then he will login ....if matches with previous data ...pass...or fail
# 5.data for user1,user2,user3....user n...will be saved
# 6.it will come in tabular form
# 7.I can delete any user data too


from prettytable import PrettyTable


users = []


def sign_up():
    name = input("Enter your name: ")
    email = input("Enter your email ID: ")

  
    for user in users:
        if user["Email"] == email:
            print("Email already registered. Try logging in.")
            return
    
    password = input("Enter your password: ")  
    users.append({"Name": name, "Email": email, "Password": password})
    print("Sign-up successful!")


def log_in():
    email = input("Enter your email ID: ")
    password = input("Enter your password: ")

    for user in users:
        if user["Email"] == email and user["Password"] == password:
            print("Login successful!")
            return True
    print("Login failed! Incorrect email or password.")
    return False


def display_users():
    if not users:
        print("No users found.")
        return

    table = PrettyTable(["Name", "Email"])
    for user in users:
        table.add_row([user.Name, user["Email"]])
    
    print("\nRegistered Users:")
    print(table)


def delete_user():
    email = input("Enter the email ID of the user to delete: ")

    for user in users:
        if user["Email"] == email:
            users.remove(user)
            print("User deleted successfully!")
            return
    
    print("User not found.")


while True:
    print("\n1. Sign Up\n2. Log In\n3. Display Users\n4. Delete User\n5. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        sign_up()
    elif choice == 2:
        log_in()
    elif choice == 3:
        display_users()
    elif choice == 4:
        delete_user()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")