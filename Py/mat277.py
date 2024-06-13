import copy
import random

def karger_min_cut(graph):
    while len(graph)>2:
        v1=random.choice(list(graph.keys()))
        v2=random.choice(graph[v1])

        print(f"Graph: {graph}")
        print(f"Contracting Edge: ({v1}, {v2})")

        new_node=f"{v1}_{v2}"

        graph[new_node]=[neighbor for neighbor in graph[v1] + graph[v2] if neighbor!=v1 and neighbor!=v2]

        for neighbor in graph[new_node]:
            graph[neighbor]=[new_node if x==v1 or x==v2 else x for x in graph[neighbor]]

        del graph[v1]
        del graph[v2]

        print(f"Graph: {graph}")
        print("-"*60)

    return len(graph[list(graph.keys())[0]])

graph={
    1: [2,3,4],
    2: [1,3],
    3: [1,2,4],
    4: [1,3]
}

karger_result = karger_min_cut(copy.deepcopy(graph))
print(f"Karger's_min_cut: {karger_result}")