import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help='commands')

# Команда list
list_parser = subparsers.add_parser(
    'list', help='List contents')
list_parser.add_argument (
    'dirname', action='store',
    help='Directory to list')

# Команда create
create_parser = subparsers.add_parser(
    'create', help='Create a directory')
create_parser.add_argument(
    'dirname', action='store',
    help='New directory to create')
create_parser.add_argument(
    '--read-only', default=False, action='store_true',
    help='Set permissions to prevent writing to the directory',
)

# Команда delete
delete_parser = subparsers.add_parser(
    'delete', help='Remove a directory')
delete_parser.add_argument (
    'dirname', action='store', help='The directory to remove')
delete_parser.add_argument(
    '--recursive', '-r', default=False, action='store_true',
    help='Remove the contents of the directory, too',
)

print(parser.parse_args())
