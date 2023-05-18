from typing import List


class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_child(self, child):
        self.children[child.name] = child

    def print(self):
        queue = [(self, 0)]  # Maintain a queue with node and its depth

        while queue:
            node, depth = queue.pop(0)
            children = ", ".join(node.children.keys())
            print(f"{node.name}: {children}")

            for child in node.children.values():
                queue.append((child, depth + 1))


def merge(inp: List[List[str]]) -> Node:
    root = Node("*")  # Create a unique root node
    node_map = {("*",): root}  # Map node paths to their corresponding Node objects

    for lst in inp:
        current_node = root  # Start at the root node for each list

        for item in lst[1:]:  # Skip the first item which is always "*"
            if item not in current_node.children:
                new_node = Node(item)
                current_node.add_child(new_node)
                current_node = new_node
            else:
                current_node = current_node.children[item]

    return root


if __name__ == "__main__":
    root = merge([
        ["*", "a", "b", "car"],
        ["*", "a", "b", "e"],
        ["*", "a", "d", "b"],
        ["*", "a", "x"]
    ])

    root.print()
