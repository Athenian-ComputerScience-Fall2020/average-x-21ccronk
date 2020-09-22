# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# Help from Megan

def avg(user_list):
    average = (sum(user_list))/(len(user_list))
    return average


if __name__ == '__main__':
    # test your fucntion with this print statement before writing the input loop
    #print(avg([0, 12, 3]))    # Put the values you want to test in for x,y and z

    div = int(input("How many number would you like to take the average of?"))
   
    # Now, comment out the print statement and work on the code below
    # Remember to indent in this section

    user_list = [] # start with an empty list
    x = 0
    while x <= div:
        y = int(input("Enter a number: "))
        x = x + 1
        user_list.append(y)

    print(avg(user_list))
    # Write a loop to allow the user to input the values to be averaged
