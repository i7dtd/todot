import curses
import os
import pickle

print('TODO list')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_task():
    clear_console()
    name = input('enter task: ')
    task.append(name)
    return menu(task)



def view_task():
    clear_console()
    if not task:
        print("you don't have any task")
    else:
        print(task)
    input('Press enter to contune ')
    return menu(task)

def delete_task():
    clear_console()
    index = int(input('Delete task number: '))
    task.pop(index - 1)
    return menu(task)

def complete_task():
    clear_console()
    index = int(input('Complete task number: '))
    if index <= len(task) or index >= 1: 
        copm_task = task[index - 1]
        task.pop(index - 1)
        task.append(f'{copm_task} ✓')
    else:
        print('You enter wrong number')
    return menu(task)


def save_task():
    clear_console()
    file = open('todo.txt', 'wb')
    pickle.dump(task, file)
    file.close
    return menu()
    


def menu(task):
    clear_console()
    print('1 -> add task\n\
2 -> all tasks\n\
3 -> make complite\n\
4 -> delete task\n\
5 -> save tasks\n\
6 -> qiut\n')
    option = input('Enter option: ')
    
    if option == '1':
        add_task()
    if option == '2':
        view_task() 
    if option == '3':
        complete_task()
    if option == '4':
        delete_task()
    if option == '5':
        save_task()
    if option == '6':
        exit()


if __name__ == '__main__':
    task = []
    menu(task)

