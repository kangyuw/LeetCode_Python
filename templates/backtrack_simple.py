result = []
def backtrack(path, choices):
    if condition():
        result.append(path)
        return
    
    for choice in choices:
        # make choice
        path.append(choice)
        backtrack(path, choices)
        # remove choice
        path.remove(choice)