class gr:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

    def get_neighbors(self, v):
        return self.adj_list[v]

    def has_edge(self, u, v):
        return v in self.adj_list[u]

    def dfs(g, v, visited, stack):
        visited.add(v)
        for neighbor in g.get_neighbors(v):
            if neighbor not in visited:
                gr.dfs(g, neighbor, visited, stack)
        stack.append(v)
        
    def topological_sort(g):
            visited = set()
            stack = []
            for v in g.adj_list:
                if v not in visited:
                    gr.dfs(g, v, visited, stack)
            return stack[::-1]

class gr1:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self):
        vertex_id = len(self.vertices)
        self.vertices[vertex_id] = []
        return vertex_id

    def add_edge(self, v1, v2):
        self.vertices[v1].append(v2)
        self.vertices[v2].append(v1)
        self.edges.append((v1, v2))

    def remove_edge(self, v1, v2):
        self.vertices[v1].remove(v2)
        self.vertices[v2].remove(v1)
        self.edges.remove((v1, v2))

    def fleury(graph):
        start_vertex = next(iter(graph.vertices))
        stack = [start_vertex]
        euler_cycle = []

        while stack:
            current_vertex = stack[-1]
            if graph.vertices[current_vertex]:
                next_vertex = graph.vertices[current_vertex][0]
                graph.remove_edge(current_vertex, next_vertex)
                stack.append(next_vertex)
            else:
                euler_cycle.append(current_vertex)
                stack.pop()
        return euler_cycle

class gr2:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        if v1 not in self.edges:
            self.edges[v1] = set()
        if v2 not in self.edges:
            self.edges[v2] = set()
        self.edges[v1].add(v2)
        self.edges[v2].add(v1)

    def find_eulerian_cycle(self):
        # Проверяем, что граф связный и каждая вершина имеет четную степень
        for vertex in self.vertices:
            if len(self.vertices[vertex]) % 2 != 0:
                return None
        visited = {}
        cycle = []
        # Начинаем обход с произвольной вершины
        start_vertex = list(self.vertices.keys())[0]
        cycle.append(start_vertex)
        visited[start_vertex] = True
        # Продолжаем обход, пока не посетим все ребра
        while len(cycle) < len(self.edges):
            current_vertex = cycle[-1]
            # Ищем не посещенные вершины, соединенные с текущей
            unvisited_neighbors = [v for v in self.edges[current_vertex] if v not in visited]
            if unvisited_neighbors:
                # Если есть не посещенные соседи, выбираем произвольного и добавляем его в цикл
                next_vertex = unvisited_neighbors[0]
                cycle.append(next_vertex)
                visited[next_vertex] = True
            else:
                # Если нет не посещенных соседей, объединяем циклы
                for i in range(len(cycle)):
                    if len(self.edges[cycle[i]]) > 1:
                        # Ищем вершину с несколькими соседями
                        merge_vertex = cycle[i]
                        # Объединяем циклы
                        cycle = cycle[i+1:] + cycle[1:i+1] + [merge_vertex]
                        break
        return cycle
    
class gr3:
    def __init__(self):
        self.adj_list = {}
        self.visited = set()

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

    def dfs(self, u, stack):
        self.visited.add(u)
        if u in self.adj_list:
            for v in self.adj_list[u]:
                if v not in self.visited:
                    self.dfs(v, stack)
        stack.append(u)

    def reverse_graph(self):
        reversed_graph = gr3()
        for u in self.adj_list:
            for v in self.adj_list[u]:
                reversed_graph.add_edge(v, u)
        return reversed_graph

    def kosaraju(self):
        stack = []
        for u in self.adj_list:
            if u not in self.visited:
                self.dfs(u, stack)
        reversed_graph = self.reverse_graph()
        components = []
        while stack:
            u = stack.pop()
            if u not in reversed_graph.visited:
                component = []
                reversed_graph.dfs(u, component)
                components.append(component)
        return components
