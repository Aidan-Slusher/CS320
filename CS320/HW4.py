# determine if a list is made up of a repeating pattern

# import math # optional and you can delete this line if not useful

# subroutines if any, go here

# fill in repeat
def longest_path(torus):
    if not torus or not all(torus):
        return []

    m, n = len(torus), len(torus[0])

    def dfs(x, y):
        current_value = torus[x][y]
        max_path = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = (x + dx) % m, (y + dy) % n  # wrap around for torus
            if torus[nx][ny] > current_value:
                path = dfs(nx, ny)
                if len(path) > len(max_path):
                    max_path = path
        return [(x, y)] + max_path

    paths = []
    for i in range(m):
        for j in range(n):
            path = dfs(i, j)
            paths.append(path)

    longest = max(paths, key=len)
    if len(longest) <= 1:  # Check if the longest path is shorter than or equal to 1
        return []

    return longest
