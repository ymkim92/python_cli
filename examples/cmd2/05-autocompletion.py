import cmd2
import argparse

class App(cmd2.Cmd):
    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]

    oparser = argparse.ArgumentParser()
    oparser.add_argument('-n', dest='name', choices=FRIENDS, help='Name of friends ')
    @cmd2.with_argparser(oparser)
    def do_greet(self, args):
        '''Say hello to somebody'''
        if args.name is None:
            print('Hello!')
        else:
            print('Hello, {}!'.format(args.name))

    nparser = argparse.ArgumentParser()
    nparser.add_argument('num1', type=int, help='Integer number')
    nparser.add_argument('num2', type=int, help='Integer number')
    @cmd2.with_argparser(nparser)
    def do_add(self, args):
        print(args.num1 + args.num2)

    def do_exit(self, arg):
        return True     # end of CLI

if __name__ == "__main__":
    App().cmdloop()