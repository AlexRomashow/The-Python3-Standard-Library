import csv
from io import StringIO
import textwrap

csv.register_dialect('escaped',
                    escapechar='\\',
                    doublequote=False,
                    quoting=csv.QUOTE_NONE)
csv.register_dialect('singlequote',
                    quotechar="'",
                    quoting=csv.QUOTE_ALL)

# Сгенерировать пробные данные для всех известных диалектов
samples = []
for name in sorted(csv.list_dialects()):
    buffer = StringIO()
    dialect = csv.get_dialect(name)
    writer = csv.writer(buffer, dialect=dialect)
    writer.writerow(
        ('col1', 1, '10/01/2010',
        'Special chars " \' {} to parse'.format(
            dialect.delimiter))
    )
    samples.append((name, dialect, buffer.getvalue()))

# Определить диалект для данного образца, а затем использовать
# результат для парсинга данных
sniffer = csv.Sniffer()
for name, expected, sample in samples:
    print('Dialect: "{}"'.format(name))
    print('In: {}'.format(sample.rstrip()))
    dialect = sniffer.sniff(sample, delimiters=',\t')
    reader = csv.reader(StringIO(sample), dialect=dialect)
    print('Parsed:\n {}\n'.format(
            '\n '.join(repr(r) for r in next(reader))))
