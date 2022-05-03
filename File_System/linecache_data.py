import os
import tempfile
lorem = '''Lorem ipsum dolor sit amet, consectetuer
adipiscing elit. Vivamus eget elit. In posuere mi non
risus. Mauris id quam posuere lectus sollicitudin
varius. Praesent at mi. Nunc eu velit. Sed augue massa,
fermentum id, nonummy а, nonummy sit amet, ligula. Curabitur
eros pede, egestas at, ultricies ас, apellentesque eu,
tellus.
Sed sed odio sed mi luctus mollis. Integer et nulla ас augue
convallis accumsan. Ut felis. Donec lectus sapien, elementum
nec, condimentum ас, interdum non, tellus. Aenean viverra,
mauris vehicula semper porttitor, ipsum odio consectetuer
lorem, ас imperdiet eros odio а sapien. Nulla mauris tellus,
aliquam non, egestas а, nonummy et, erat. Vivamus sagittis
porttitor eros.'''

def make_tempfile():
    fd, temp_file_name = tempfile.mkstemp()
    os.close(fd)
    with open(temp_file_name, 'wt') as f:
        f.write(lorem)
    return temp_file_name

def cleanup(filename):
    os.unlink(filename)
