import os

def main():

    while True:

        print("1. ADD\n2. HELP\n3. LIST\n4. EXIT")
        inp = input("choose one of four commands: ")

        if inp == 'EXIT':
            print("you have quit!")
            exit()
        elif inp == 'HELP':
            print("Add command adds two integers.")
            print("Exit command quits the application")
            print("List shows all files in a directory")
        elif inp == 'ADD':
            num1 = input("provide first number: ")
            num2 = input("provide second number: ")
            print(int(num1) + int(num2))
            return
        elif inp == 'LIST':
            files = os.listdir()
            print(files)
            return
        else:
            print("Wrong command, please ty again.")
            main()


if __name__ == '__main__':
    main()