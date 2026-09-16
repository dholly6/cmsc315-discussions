"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Linear search checks each value one at a time from beginning to end.
    # In the worst case, every item must be checked, giving it O(n) complexity.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # Return -1 when the target does not exist in the list.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    low = 0
    high = len(lst) - 1

    while low <= high:
        # Check the middle of the remaining search area.
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid

        # If the target is larger, ignore the left half.
        elif lst[mid] < target:
            low = mid + 1

        # If the target is smaller, ignore the right half.
        else:
            high = mid - 1

        # Each loop eliminates about half of the remaining values.

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    small_scores = [55, 67, 72, 81, 90, 95]

    # 81 exists in the list, so both searches should return its index.
    print("Linear search for 81:", linear_search(small_scores, 81))
    print("Binary search for 81:", binary_search(small_scores, 81))

    # 100 does not exist, so both searches should return -1.
    print("Linear search for 100:", linear_search(small_scores, 100))
    print("Binary search for 100:", binary_search(small_scores, 100))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    large_scores = list(range(1, 1001))

    print("Linear search for 950:", linear_search(large_scores, 950))
    print("Binary search for 950:", binary_search(large_scores, 950))

    # Both searches find the same result, but linear search may have to
    # check many values. Binary search repeatedly cuts the search area
    # in half, making it more efficient as the dataset becomes larger.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Searching an empty list should return -1.
    empty_list = []
    print("Binary search empty list:", binary_search(empty_list, 81))

    # Edge case 2: Both searches should find the only item at index 0.
    single_score = [81]
    print("Linear search single item:", linear_search(single_score, 81))
    print("Binary search single item:", binary_search(single_score, 81))


if __name__ == "__main__":
    main()
