import argparse

class CustomAction(argparse.Action):
    
    def __init__(self,
            option_strings,
            dest,
            nargs=None,
            const=None,
            default=None,
            type=None,
            choices=None,
            required=False,
            help=None,
            metavar=None):
        argparse.Action. __init__(self,
                option_strings=option_strings,
                dest=dest,
                nargs=nargs,
                const=const,
                default=default,
                type=type,
                choices=choices,
                required=required,
                help=help,
                metavar=metavar,
                )
        print('Initializing CustomAction')
        for name, value in sorted(locals().items()):
            if name == 'self' or value is None:
                continue
            print('{} = {!r}'.format(name, value))
        print()
        return
    
    def __call__(self, parser, namespace, values,
                option_string=None):
        print('Processing CustomAction for {}'.format(self.dest))
        print('parser = {}'.format(id(parser)))
        print('values = {!r}'.format(values))
        print('option_string = {!r}'.format(option_string))

        # Выполнить необходимую обработку входных значений
        if isinstance(values, list):
            values = [v.upper() for v in values]
        else:
            values = values.upper()
        # Сохранить результаты в пространстве имен, используя
        # переменную destination, предоставленную конструктору
        setattr(namespace, self.dest, values)
        print()

parser = argparse.ArgumentParser()

parser.add_argument('-а', action=CustomAction)
parser.add_argument('-m', nargs='*', action=CustomAction)

results = parser.parse_args(['-a', 'value',
                    '-m', 'multivalue',
                    'second'])
print(results)
