#MAIN PAGE

#Importing the python files for the 3 tasks
import Task1 as TASK1
import Task2 as TASK2
import Task3 as TASK3

#Welcome Message
print("Welcome to CZ3005 Assignment 1!")
print("Press 1 to run Task 1")
print("Press 2 to run Task 2")
print("Press 3 to run Task 3")

#User's Input
task = input("Please Choose Task:")
print('\n')

#Running the Selected Task
if task == '1':
    TASK1.run_task1()

    retry = 'p'

    while retry != None:
        retry = input('Do you want to try again? [y/n] - ')
        if retry.lower() == 'y':
            TASK1.run_task1()

        elif retry.lower() == 'n':
            print('Task 1 Completed!')
            break

elif task == '2':
    print('Running Task 2: Uniform Cost Search (UCS) ... ')
    TASK2.run_task2()
    print("Task 2 Completed!")

elif task == '3':
    print('Running Task 3: A STAR Algorithm ... ')
    TASK3.run_task3()
    print("Task 3 Completed!")

else:
    print('Please type in the correct number!')



