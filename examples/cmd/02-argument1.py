import cmd

class App(cmd.Cmd):
    def do_greet(self, arg):
        if len(arg) == 0:
            print('Hello!')
        else:
            print('Hello, {}!'.format(arg))

    def do_exit(self, arg):
        return True

    do_EOF = do_exit

if __name__ == "__main__":
    App().cmdloop()