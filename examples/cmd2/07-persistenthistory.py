import cmd2
import argparse

history_file = '~/.persistent_history.cmd2'

class App(cmd2.Cmd):
    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]

    def __init__(self, hist_file=''):
        if hist_file=='':
            super().__init__()
        else:
            super().__init__(persistent_history_file=hist_file, persistent_history_length=500)

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
    App(hist_file=history_file).cmdloop()