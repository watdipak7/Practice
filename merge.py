from typing import List


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print(self):
        queue = [(self, 0)]  
        # Maintain a queue with node and its depth for BFS traversal

        while queue:
            node, depth = queue.pop(0)
            children = ", ".join(child.name for child in node.children) 
            #Children names added as string to node name string
            print(f"{node.name}: {children}")
            for child in node.children:
                queue.append((child, depth + 1))
            #Adding children in queue to go down the depth    


def merge(inp: List[List[str]]) -> Node:
    root = Node("*")  # Create a unique root node
    node_map = {("*",): root}  # Map node-paths to their corresponding Node objects

    for lst in inp:
        current_node = root  # Start at the root node for each list
        path = [current_node.name]  # Keep track of the current path from the root

        for item in lst[1:]:  # Skip the first item which is always "*"
            path.append(item)
            node_key = tuple(path)

            if node_key not in node_map:
                new_node = Node(item)
                node_map[node_key] = new_node
                current_node.add_child(new_node)
                current_node = new_node
            else:
                current_node = node_map[node_key]

        path.pop()  # Remove the last item in the path

    return root


if __name__ == "__main__":
    root = merge([
        ["*", "a", "b", "car"],
        ["*", "a", "b", "e"],
        ["*", "a", "d", "b"],
        ["*", "a", "x"]
    ])

    root.print()
