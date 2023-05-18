{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPoBECE0UIVDzWCXJ0JQMVG",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/coderbijarniya/Practice/blob/main/merge.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N-tACMjZtf-H",
        "outputId": "03296484-849a-4115-aa47-2e6c5cf7dc65"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "*: a\n",
            "a: b, d, x\n",
            "b: car, e\n",
            "d: b\n",
            "x: \n",
            "car: \n",
            "e: \n",
            "b: \n"
          ]
        }
      ],
      "source": [
        "from typing import List\n",
        "\n",
        "\n",
        "class Node:\n",
        "    def __init__(self, name):\n",
        "        self.name = name\n",
        "        self.children = []\n",
        "\n",
        "    def add_child(self, child):\n",
        "        self.children.append(child)\n",
        "\n",
        "    def print(self):\n",
        "        queue = [(self, 0)]  \n",
        "        # Maintain a queue with node and its depth for BFS traversal\n",
        "\n",
        "        while queue:\n",
        "            node, depth = queue.pop(0)\n",
        "            children = \", \".join(child.name for child in node.children) \n",
        "            #Children names added as string to node name string\n",
        "            print(f\"{node.name}: {children}\")\n",
        "            for child in node.children:\n",
        "                queue.append((child, depth + 1))\n",
        "            #Adding children in queue to go down the depth    \n",
        "\n",
        "\n",
        "def merge(inp: List[List[str]]) -> Node:\n",
        "    root = Node(\"*\")  # Create a unique root node\n",
        "    node_map = {(\"*\",): root}  # Map node-paths to their corresponding Node objects\n",
        "\n",
        "    for lst in inp:\n",
        "        current_node = root  # Start at the root node for each list\n",
        "        path = [current_node.name]  # Keep track of the current path from the root\n",
        "\n",
        "        for item in lst[1:]:  # Skip the first item which is always \"*\"\n",
        "            path.append(item)\n",
        "            node_key = tuple(path)\n",
        "\n",
        "            if node_key not in node_map:\n",
        "                new_node = Node(item)\n",
        "                node_map[node_key] = new_node\n",
        "                current_node.add_child(new_node)\n",
        "                current_node = new_node\n",
        "            else:\n",
        "                current_node = node_map[node_key]\n",
        "\n",
        "        path.pop()  # Remove the last item in the path\n",
        "\n",
        "    return root\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    root = merge([\n",
        "        [\"*\", \"a\", \"b\", \"car\"],\n",
        "        [\"*\", \"a\", \"b\", \"e\"],\n",
        "        [\"*\", \"a\", \"d\", \"b\"],\n",
        "        [\"*\", \"a\", \"x\"]\n",
        "    ])\n",
        "\n",
        "    root.print()"
      ]
    }
  ]
}