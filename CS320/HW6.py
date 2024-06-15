from edgegraph import *


def bfs(graph: GraphEL, start: VertexEL) -> list:
    # Argument Test
    if graph is None or start is None or start not in graph.vertices():
        return []

    # Singleton Test
    if graph.num_vertices() == 1:
        return [start]

    visited = set()  # To keep track of visited vertices by name
    queue = [start]  # Initialize queue with start vertex
    bfs_order = []   # To store BFS traversal order

    while queue:
        vertex = queue.pop(0)  # Dequeue a vertex from the queue
        if vertex.name not in visited:
            visited.add(vertex.name)  # Mark the vertex name as visited
            bfs_order.append(vertex)  # Add the vertex to the BFS order

            # Enqueue all adjacent vertices of the dequeued vertex
            for neighbor in graph.adjacent_vertices(vertex):
                if neighbor.name not in visited:
                    queue.append(neighbor)

    return bfs_order


# Test cases
def test_argument():
    # Test when graph is None
    assert bfs(None, VertexEL("A")) == []

    # Test when start vertex is None
    assert bfs(GraphEL(), None) == []

    # Test when start vertex is not in graph
    graph = GraphEL()
    graph.add_vertex(VertexEL("A"))
    assert bfs(graph, VertexEL("B")) == []


def test_singleton():
    # Test when graph has only one vertex
    graph = GraphEL()
    vertex = VertexEL("A")
    graph.add_vertex(vertex)
    assert bfs(graph, vertex) == [vertex]


def test_simple():
    # Test a simple scenario
    graph = GraphEL()
    A = VertexEL("A")
    B = VertexEL("B")
    C = VertexEL("C")
    D = VertexEL("D")
    graph.add_vertex(A)
    graph.add_vertex(B)
    graph.add_vertex(C)
    graph.add_vertex(D)
    graph.add_edge(EdgeEL("e1", A, B))
    graph.add_edge(EdgeEL("e2", B, C))
    graph.add_edge(EdgeEL("e3", C, D))
    graph.add_edge(EdgeEL("e4", A, D))
    assert bfs(graph, A) == [A, B, D, C]


def test_diamond():
    # Test a diamond scenario
    graph = GraphEL()
    A = VertexEL("A")
    B = VertexEL("B")
    C = VertexEL("C")
    D = VertexEL("D")
    graph.add_vertex(A)
    graph.add_vertex(B)
    graph.add_vertex(C)
    graph.add_vertex(D)
    graph.add_edge(EdgeEL("e1", A, B))
    graph.add_edge(EdgeEL("e2", A, C))
    graph.add_edge(EdgeEL("e3", B, D))
    graph.add_edge(EdgeEL("e4", C, D))
    assert bfs(graph, A) == [A, B, C, D]


def test_large():
    # Test a large scenario
    graph = GraphEL()
    vertices = [VertexEL(str(i)) for i in range(10)]
    for v in vertices:
        graph.add_vertex(v)
    for i in range(len(vertices) - 1):
        graph.add_edge(EdgeEL(f"e{i}", vertices[i], vertices[i + 1]))
    assert bfs(graph, vertices[0]) == vertices


# Run tests
test_argument()
test_singleton()
test_simple()
test_diamond()
test_large()
