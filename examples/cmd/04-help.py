import cmd

class App(cmd.Cmd):
    def do_greet(self, arg):
        '''Say hello to somebody'''
        if len(arg) == 0:
            print('Hello!')
        else:
            print('Hello, {}!'.format(arg))

    def do_add(self, args):
        items = args.split()
        if len(items) != 2:
            self.help_add()
            return      # end of command
        
        print(int(items[0])+int(items[1]))

    def help_add(self):
        print('You need two arguments:')
        print('\tUsage: add x y')

    def do_exit(self, arg):
        return True     # end of CLI

    do_EOF = do_exit

if __name__ == "__main__":
    App().cmdloop()