import pickle
import pprint

data = [{'a': 'A', 'b': 2, 'c': 3.0}]
print('Data:', end=' ')
pprint.pprint(data)

data_string = pickle.dumps(data)
print('Pickle: {!r}'.format(data_string))
