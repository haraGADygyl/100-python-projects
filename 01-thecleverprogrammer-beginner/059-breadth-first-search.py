class Queue:
    def __init__(self):
        self.size = 0
        self.items = []

    def enqueue(self, el):
        self.items.append(el)
        self.size += 1

    def dequeue(self):
        try:
            self.size -= 1
            return self.items.pop(0)
        except Exception as error:
            print(f'{error} is not possible')

    def xprint(self, index):
        print(self.items[index])

    def __repr__(self):
        return f'{self.items}: {self.size}'


def breadth_first(graph, root):
    q = Queue()

    visited_notes = []
    q.enqueue(root)
    visited_notes.append(root)

    current_node = root

    while q.size > 0:
        current_node = q.dequeue()
        adj_nodes = graph[current_node]
        remaining_elements = sorted(set(adj_nodes) - set(visited_notes))

        if len(remaining_elements) > 0:
            for element in remaining_elements:
                visited_notes.append(element)
                q.enqueue(element)

    return visited_notes


if __name__ == '__main__':
    graph = dict()

    graph['A'] = ['B', 'G', 'D']
    graph['B'] = ['A', 'F', 'E']
    graph['C'] = ['F', 'H']
    graph['D'] = ['F', 'A']
    graph['E'] = ['B', 'G']
    graph['F'] = ['B', 'D', 'C']
    graph['G'] = ['A', 'E']
    graph['H'] = ['C']

    print(breadth_first(graph, 'A'))
