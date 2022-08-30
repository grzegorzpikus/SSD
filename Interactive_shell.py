from cmd import Cmd


class MyPrompt(Cmd):

    intro = "*"*72 + "\n" + "Welcome, to simple Python shell. Type help" \
                            "to see available actions." + "\n" + "*"*72

    def do_exit(self, inp):
        """exit the application"""
        print("You have quit the application.")
        return True

    def do_add(self, inp):
        """the function adds two numbers and gives the result"""
        result = 0
        try:
            if len(inp.split()) == 2:
                result = int(inp.split()[0]) + int(inp.split()[1])
                print(result)
            else:
                print("separate two numbers with a space!")
        except ValueError:
            print("only numbers are allowed!")
        return result


p = MyPrompt()
p.cmdloop()


