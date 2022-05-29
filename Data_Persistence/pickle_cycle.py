import pickle

class Node:
    """Простой диграф.
    """
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_edge(self, node):
        "Создает границу между данным и другим узлом."
        self.connections.append(node)

    def __iter__(self) :
        return iter(self.connections)
    
def preorder_traversal(root, seen=None, parent=None):
    """Функция-генератор, возвращающая границы для графа.
    """
    if seen is None:
        seen = set()
    yield (parent, root)
    if root in seen:
        return
    seen.add(root)
    for node in root:
        recurse = preorder_traversal(node, seen, root)
        for parent, subnode in recurse:
            yield (parent, subnode)

def show_edges(root):
    "Выводит все границы в графе."
    for parent, child in preorder_traversal(root):
        if not parent:
            continue
        print('{:>5} -> {:>2} ({})'.format(
            parent.name, child.name, id(child)))

# Задание узлов
root = Node('root')
a = Node('а')
b = Node('b')
c = Node('c')

# Добавление границ между ними
root.add_edge(a)
root.add_edge(b)
a.add_edge(b)
b.add_edge(a)
b.add_edge(c)
a.add_edge(a)

print('ORIGINAL GRAPH:')
show_edges(root)

# Сериализация и десериализация графа для
# создания нового набора узлов
dumped = pickle.dumps(root)
reloaded = pickle.loads(dumped)

print('\nRELOADED GRAPH:')
show_edges(reloaded)
