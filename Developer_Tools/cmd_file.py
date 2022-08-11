import cmd

class HelloWorld(cmd.Cmd):
    
    # Отключить использование модуля rawinput
    use_rawinput = False

    # Не отображать подсказку после чтения каждой команды
    prompt = ''

    def do_greet(self, line):
        print("hello,", line)

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'rt') as input:
        HelloWorld(stdin=input).cmdloop()
