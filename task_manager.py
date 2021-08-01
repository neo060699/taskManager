# This program accesses a database to see if a user is allowed to access the program
# Certain usernames have more authority than others, therefore they have more options than other users

# variables that need to be established before use
username_input = ""
username = "1"
password_input = ""
password = "1"
access = ''
option = ""

while access != "Access Granted":  # loop must run until username and in put are the same

    username_input = input("Enter username here                 ")
    password_input = input("Enter password here:                ")
    task_file = open('tasks.txt', 'r')
    user_file = open('user.txt', 'r')

    for line in user_file:  # This loop helps the program read the user.txt file
        username_split = line.split()
        username = username_split[0].replace(",", "")
        password_split = line.split()
        password = password_split[1]

        # This if statement determines if the data given is correct and matches the data in the user.txt file
        if username_input == username and password_input == password:
            access = "Access Granted"
            if access == "Access Granted":
                print("Access Granted")
            else:
                print("Access Denied")
    task_file.close()
    user_file.close()

if username_input == "admin":  # This function restricts the rest of the users from certain functions
    print(
        "Please select one of the following options: \nr - register user\na - add task\nva - view all tasks\n"
        "vm - view mine\ngr - general reports\nds - display statistics\ne - exit")
    print("")
    option = input("Type in your option             ")
else:
    # the following functions are displayed to non admin users
    print(
        "Please select one of the following options: \nr - register user\na - add task\nva - view all tasks\n"
        "vm - view my tasks\ne - exit")
    print("")
    option = input("Type in your option             ")

if option == "r":  # This option allows the admin to register users to the list and denies non admin
    if username_input == 'admin':
        reg_diff_user = False
        while reg_diff_user:
            user_file = open("user.txt", "a")  # 'a' appends the new data to the list
            register_user = input('Enter a new username:                ')
            register_password = input('Enter your password:             ')
            confirm_password = input('Confirm your password             ')
            if register_password == confirm_password:
                if username not in user_file:
                    user_file.write("\n" + register_user + ", " + register_password)  # test display
                    reg_diff_user = True
                else:
                    print("Error: This user has already been registered\nEnter a different username.")
                user_file.close()
            else:
                print('Only the Admin is allowed to register new users')


elif option == "a":  # this option is visible to every user it is used to add tasks to text file
    task_file = open("tasks.txt", "a")
    task_user = input('Assign task to user (Enter username): ')
    task_title = input("What is the task at hand?:          ")
    task_description = input("Describe the task at hand: ")
    task_dates = input('Enter task due date:                ')
    current_date = input("Enter today's date?")
    task_status = "Is task done:    No"

    # the "added_tasks" variable is to store the data the way it appears in the text file
    added_tasks = str([task_user, task_title, task_description, task_dates, current_date, task_status])
    task_file.write("\n" + added_tasks)

    task_file.close()

    # this option allows users to see all of the tasks on the txt file
elif option == "va":
    task_file = open("tasks.txt")
    for line in task_file:  # this loop reads through the txt file
        line_split = (line.split())
        print(line.replace(",", "\n"))
    task_file.close()


elif option == "vm":  # this option allows users to see tasks allocated to a single user
    task_file = open("tasks.txt")
    task_num = 1
    for line in task_file:  # this loop reads through the txt file
        line_split = (line.split())

        if line_split[0].replace(",", "") == username_input:
            print("Task " + str(task_num))
            print(line.replace(",", "\n"))
            task_num += 1
        else:
            print("There are no tasks for this user.")
    task_file.close()

# here is the general report option
# Here the the program will show the user an overview of the data in the file in digestible ways
elif option == "gr":
    task_file = open("tasks.txt")
    task_count = 0
    for line in task_file:  # This counter counts the total tasks in the folder
        task_count += 1
    total_task = task_count

    complete_task_iteration = 0
    task_file = open("tasks.txt")
    for line in task_file:
        line_split = (line.split())
        if line_split[-1] == 'Yes':
            complete_task_iteration += 1

    incomplete_task_iteration = 0
    task_file = open("tasks.txt")
    for line in task_file:
        line_split = (line.split())
        if line_split[-1] == "No":
            incomplete_task_iteration += 1

    user_file = open("user.txt")
    user_count = 0
    for line in user_file:
        user_count += 1

    task_file = open("tasks.txt")
    task_count = 0
    for line in task_file:  # This counter counts the total tasks in the folder
        task_count += 1
    total_task = task_count

    print("Task Overview: ")
    print("Amount of tasks: " + str(task_count))
    print("Number of tasks completed:  " + str(complete_task_iteration))
    print("Number of incomplete task: " + str(incomplete_task_iteration))
    incomplete_percentage = total_task / incomplete_task_iteration
    print(str(incomplete_percentage) + " of the tasks are incomplete.")
    print("")
    print("User Overview: ")
    print("Number of users on the system: " + str(user_count))

    task_file.close()

elif option == "ds":  # This option is only visible to the admin user,, it show the total number of tasks and users
    task_file = open("tasks.txt")
    user_file = open("user.txt")
    user_num = 0
    task_num = 0
    for line in task_file:
        task_num += 1
    for line in user_file:
        user_num += 1
    print("The number of tasks is: " + str(task_num))
    print("The number of users is: " + str(user_num))
