import cmd

class InteractiveOrCommandLine(cmd.Cmd) :
    """Принимает команды через обычную интерактивную подсказку
    или из командной строки.
    """
    def do_greet(self, line):
        print('hello,', line)

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        InteractiveOrCommandLine().onecmd(' '.join(sys.argv[1:]))
    else:
        InteractiveOrCommandLine().cmdloop()
