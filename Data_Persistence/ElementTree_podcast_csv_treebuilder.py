import csv
import io
from xml.etree.ElementTree import XMLParser
import sys

class PodcastListToCSV:

    def __init__(self, outputFile):
        self.writer = csv.writer(
            outputFile,
            quoting=csv.QUOTE_NONNUMERIC,
        )
        self.group_name = ''

    def start(self, tag, attrib):
        if tag != 'outline':
            # Игнорировать все, что не входит в дескриптор outline
            return
        if not attrib.get('xmlUrl'):
            # Запомнить текущую группу
            self.group_name = attrib['text']
        else:
            # Вывести запись, соответствующую подкасту
            self.writer.writerow(
                (self.group_name,
                attrib['text'],
                attrib['xmlUrl'],
                attrib.get('htmlUrl', ''))
            )

    def end(self, tag):
        "Ignore closing tags"

    def data(self, data):
        "Ignore data inside nodes"

    def close(self):
        "Nothing special to do here"

target = PodcastListToCSV(sys.stdout)
parser = XMLParser(target=target)
with open('podcast.opml', 'rt') as f:
    for line in f:
        parser.feed(line)
parser.close()

