try:
    import gnureadline as readline
except ImportError:
    import readline
import logging

LOG_FILENAME = '/tmp/completer.log'
logging.basicConfig(
    format='%(message)s',
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

class SimpleCompleter:

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        response = None
        if state == 0:
            # Это первое обращение к данному тексту,
            # поэтому создаем полный список вариантов
            if text:
                self.matches = [
                    s
                    for s in self.options
                    if s and s.startswith(text)
                ]
                logging.debug('%s matches: %s',
                        repr(text), self.matches)
            else:
                self.matches = self.options[:]
                logging.debug('(empty input) matches: %s',
                            self.matches)

        # Вернуть элемент c индексом state из списка,
        # если он содержит достаточное количество элементов
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        logging.debug('complete(%s, %s) => %s',
                            repr(text), state, repr(response))
        return response

def input_loop():
    line = ''
    while line != 'stop':
        line = input('Prompt ("stop" to quit): ')
        print('Dispatch {}'.format(line))

# Зарегистрировать функцию завершения ввода
OPTIONS = ['start', 'stop', 'list', 'print']
readline.set_completer(SimpleCompleter(OPTIONS).complete)

# Использовать клавишу <tab> для завершения ввода
readline.parse_and_bind('tab: complete')

# Предложить пользователю ввести текст
input_loop()

















