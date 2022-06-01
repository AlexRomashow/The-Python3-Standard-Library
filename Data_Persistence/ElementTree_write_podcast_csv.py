import csv
from xml.etree.ElementTree import iterparse
import sys

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

group_name = ''

parsing = iterparse('podcast.opml', events=['start'])

for (event, node) in parsing:
    if node.tag != 'outline':
        # Игнорировать все, что не входит в дескриптор outline
        continue
    if not node.attrib.get('xmlUrl'):
        # Запомнить текущую группу
        group_name = node.attrib['text']
    else:
        # Вывести запись, соответствующую подкасту
        writer.writerow(
            (group_name, node.attrib['text'],
                node.attrib['xmlUrl'],
                node.attrib.get('htmlUrl', ''))
        )
