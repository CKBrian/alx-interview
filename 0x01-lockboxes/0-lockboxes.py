#!/usr/bin/python3
'''Defines a module that implements a canUnlockAll function'''


def canUnlockAll(boxes):
    """
    Returns a tuple.

    Args:
        lst (Iterable[Sequence]): The input iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each containg an
        element from the input list and its corresponding length.
    """
    if not boxes:
        return False

    # Initialize a set to keep track of visited boxes
    visited = set()

    # Initialize a queue with the first box
    queue = [0]

    # Mark the first box as visited
    visited.add(0)

    # Perform BFS
    while queue:
        current_box = queue.pop(0)

        # Check all keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and that box hasn't been visited yet
            if key < len(boxes) and key not in visited:
                # Mark the box as visited and add it to the queue
                visited.add(key)
                queue.append(key)

    # If all boxes have been visited, return True; otherwise, return False
    return len(visited) == len(boxes)
