"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Starts at the root and uses recursion to find the correct position based on whether the value is smaller or larger.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # An empty position means the correct location was found.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Returns the node so the tree remains connected.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # If there are no more nodes, the value was not found.
        if node is None:
            return False

        # If the current node contains the value, the search is complete.
        if value == node.value:
            return True

        # Smaller values can only be located in the left subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Larger values can only be located in the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Creates an empty list to store the values during traversal.
        values = []

        # Starts the in-order traversal at the root.
        self._inorder_recursive(self.root, values)

        # Returns the completed list of values.
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Only processes the node if it exists.
        if node is not None:

            # First visit all smaller values in the left subtree.
            self._inorder_recursive(node.left, values)

            # Then add the current node's value.
            values.append(node.value)

            # Finally visit all larger values in the right subtree.
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Creates a new Binary Search Tree.
    tree = BST()

    # These values create both left and right subtrees.
    values = [50, 30, 70, 20, 40, 60, 80]

    # Inserts each value into the BST.
    for value in values:
        tree.insert(value)

    # A BST reduces the search space by deciding whether to continue left or right based on the value being compared.
    print("Values inserted:", values)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # Smaller values are stored on the left and larger values are stored on the right, the result is sorted.
    sorted_values = tree.inorder()

    print("In-order traversal:", sorted_values)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Searches for two values that exist in the BST.
    print("Search for 30:", tree.search(30))
    print("Search for 70:", tree.search(70))

    # Searches for two values that do not exist in the BST.
    print("Search for 25:", tree.search(25))
    print("Search for 90:", tree.search(90))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Creates an empty BST with no nodes.
    empty_tree = BST()

    # Searching an empty tree should return False because there are no nodes available to contain the value.
    print("Search empty tree for 50:", empty_tree.search(50))

if __name__ == "__main__":
    main()