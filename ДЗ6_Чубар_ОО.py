import networkx as nx
import matplotlib.pyplot as plt

# ЗАВДАННЯ 1. 
# Створення графа
G = nx.Graph()
# Додавання вершин і ребер (модель транспортної мережі)
G.add_edges_from([
    ('A', 'B', {'weight': 4}),
    ('A', 'C', {'weight': 3}),
    ('B', 'D', {'weight': 2}),
    ('C', 'D', {'weight': 4}),
    ('C', 'E', {'weight': 2}),
    ('D', 'F', {'weight': 1}),
    ('E', 'F', {'weight': 5}),
    ('E', 'G', {'weight': 7}),
    ('F', 'G', {'weight': 2})
])
# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа міста")

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree = dict(G.degree())
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь кожної вершини: {degree}")


# ЗАВДАННЯ 2.
# Пошук у глибину (DFS)
dfs_path = list(nx.dfs_edges(G, source='A'))
dfs_nodes = [edge[1] for edge in dfs_path]
dfs_nodes.insert(0, 'A')
print(f"Шлях DFS: {' -> '.join(dfs_nodes)}")

# Пошук у ширину (BFS)
bfs_path = list(nx.bfs_edges(G, source='A'))
bfs_nodes = [edge[1] for edge in bfs_path]
bfs_nodes.insert(0, 'A')
print(f"Шлях BFS: {' -> '.join(bfs_nodes)}")


# ЗАВДАННЯ 3.
# Алгоритм Дейкстри для знаходження найкоротшого шляху від вузла 'A'
shortest_paths = nx.single_source_dijkstra_path(G, source='A')
# Виведення всіх шляхів
for target, path in shortest_paths.items():
    print(f"Найкоротший шлях від 'A' до '{target}': {' -> '.join(path)}")

plt.show()