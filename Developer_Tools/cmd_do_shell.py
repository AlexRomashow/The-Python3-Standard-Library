import cmd
import subprocess

class ShellEnabled(cmd.Cmd):
    
    last_output = ''

    def do_shell(self, line):
        "Run а shell command"
        print("running shell command:", line)
        sub_cmd = subprocess.Popen(line,
                                    shell=True,
                                    stdout=subprocess.PIPE)
        output = sub_cmd.communicate()[0].decode('utf-8')
        print(output)
        self.last_output = output

    def do_echo(self, line):
        """Print the input, replacing '$out' with
        the output of the last shell command
        """
        # Явно ненадежньпй вариант
        print(line.replace('$out', self.last_output))

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    ShellEnabled().cmdloop()
