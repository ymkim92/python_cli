import cmd2

class App(cmd2.Cmd):
    def do_greet(self, arg):
        print('Hello!')

    def do_exit(self, arg):
        return True

if __name__ == "__main__":
    App().cmdloop()
