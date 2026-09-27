"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # Create a copy so the original list is not changed.
    sorted_list = lst.copy()

    # Move through the list multiple times.
    for i in range(len(sorted_list) - 1):
        swapped = False

        # Compare neighboring values.
        for j in range(len(sorted_list) - 1 - i):

            # Swap the values if they are in the wrong order.
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = \
                    sorted_list[j + 1], sorted_list[j]
                swapped = True

        # Stop early if no swaps were needed.
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # A list with zero or one element is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle and divide the list into two halves.
    midpoint = len(lst) // 2
    left = lst[:midpoint]
    right = lst[midpoint:]

    # Recursively sort both halves.
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the sorted halves.
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    result = []
    left_index = 0
    right_index = 0

    # Compare values from both lists and add the smaller value.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any values remaining in either list.
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    # Video game scores that need to be sorted.
    game_scores = [450, 120, 780, 340, 900, 210, 560]

    print("Original game scores:", game_scores)
    print("Bubble Sort:", bubble_sort(game_scores))
    print("Merge Sort:", merge_sort(game_scores))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")

    # A second set of player scores.
    player_scores = [65, 22, 91, 48, 73, 15, 84, 39]

    print("Original player scores:", player_scores)
    print("Bubble Sort:", bubble_sort(player_scores))
    print("Merge Sort:", merge_sort(player_scores))

    # Both algorithms should produce the same sorted result.
    print("Results match:",
          bubble_sort(player_scores) == merge_sort(player_scores))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: An empty list should remain empty.
    empty_list = []
    print("Empty list with Bubble Sort:", bubble_sort(empty_list))
    print("Empty list with Merge Sort:", merge_sort(empty_list))

    # Edge case 2: An already sorted list should remain unchanged.
    sorted_scores = [10, 20, 30, 40, 50]
    print("Already sorted with Bubble Sort:",
          bubble_sort(sorted_scores))
    print("Already sorted with Merge Sort:",
          merge_sort(sorted_scores))


if __name__ == "__main__":
    main()
