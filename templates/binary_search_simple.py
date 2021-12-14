# Initialize the boundary variables to include all possible elements
# Decide Return Value:
#    left or left - 1
#    left is the minimal k satisfying the condition function
# Design the condition function

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left