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

class BufferAwareCompleter:

    def __init__(self, options):
        self.options = options
        self.current_candidates = []

    def complete(self, text, state):
        response = None
        if state == 0:
            # Это первое обращение к данному тексту,
            # поэтому создаем полный список вариантов
            origline = readline.get_line_buffer()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            being_completed = origline[begin:end]
            words = origline.split()

            logging.debug('origline=%s', repr(origline))
            logging.debug('begin=%s', begin)
            logging.debug('end=%s', end)
            logging.debug('being_completed=%s', being_completed)
            logging.debug('words=%s', words)

            if not words:
                self.current_candidates = sorted(
                    self, options. ke.ys ()
                )
            else:
                try:
                    if begin == 0:
                        # Первое слово
                        candidates = self.options.keys()
                    else:
                        # Последнее слово
                        first = words[0]
                        candidates = self.options[first]
    
                    if being_completed:
                        # Сопоставить варианты c завершаемой
                        # частью ввода
                        self.current_candidates = [
                            w for w in candidates
                            if w.startswith(being_completed)
                        ]
                    else:
                        # При сопоставлении c пустой строкой
                        # использовать все подходящие варианты
                        self.current_candidates = candidates
                    
                    logging.debug('candidates=%s',
                            self, current_candidates)

                except (KeyError, IndexError) as err:
                    logging.error('completion error: %s', err)
                    self.current_candidates = []
        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        logging.debug('complete(%s, %s) => %s',
                            repr(text), state, response)
        return response

def input_loop():
    line = ''
    while line != 'stop':
        line = input('Prompt ("stop" to quit): ')
        print('Dispatch {}'.format(line))

# Зарегистрировать функцию завершения ввода
completer = BufferAwareCompleter({
        'list': ['files', 'directories'],
        'print': ['byname', 'bysize'],
        'stop': [],
})
readline.set_completer(completer.complete)

# Использовать клавишу <tab> для завершения ввода
readline.parse_and_bind('tab: complete')

# Предложить пользователю ввести текст
input_loop()
