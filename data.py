
def dfs(grid, i, j):
    if not(i < 0 or i >= len(grid) or j < 0 or j >= len(grid)):
        if grid[i][j] =="1":
            grid[i] = grid[i][:j]+ "0" + grid[i][j + 1:]

            dfs(grid, i + 1,j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

    return

def count_connected_shapes(grid):
    length = len(grid)
    shapes = 0

    for i in range(length):
        for j in range(length):
            if grid[i][j] == "1":
                shapes +=1
                dfs(grid, i, j)
    return shapes

def read_grid_from_file(file_path):
    with open(file_path, "r") as f:
        grid = [line.strip() for line in f]
    return grid


def main():
    large_file_path = "data_large.txt"
    small_file_path = "data_small.txt"
    small_grid = read_grid_from_file(small_file_path)
    large_grid = read_grid_from_file(large_file_path)
    result1 = count_connected_shapes(small_grid)
    result2 = count_connected_shapes(large_grid)
    print("Small data number of groups: ", result1)
    print("Large data number of groups: ", result2)

main()







