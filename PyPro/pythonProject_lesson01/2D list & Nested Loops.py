nuber_grid = [
    [1, 2, 3], #0       # 3 rows, 4 columms, we type the index of position
    [4, 5, 6], #1
    [7, 8, 9], #2
    [0]        #3
]

print(nuber_grid[2][1])

for row in nuber_grid:
       print(row)

for row in nuber_grid:
   for col in row:
       print(col)