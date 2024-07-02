def canUnlockAll(boxes):
    if not boxes:
        return False
    count = len(boxes)
    visited = [False] * count
    stack = [0]
    visited[0] = True
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if visited[key] == False:
                visited[key] = True
                stack.append(key)
    return all(visited)
