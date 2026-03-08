def grid_challenge(grid):
    # จัดเรียงตัวอักษรในแต่ละแถว แล้วเช็คว่าแต่ละคอลัมน์เรียงตามลำดับตัวอักษรมั้ย
    # จัดเรียงแต่ละแถว
    sorted_grid = ["".join(sorted(row)) for row in grid]
    
    # เช็คคอลัมน์
    rows = len(sorted_grid)
    cols = len(sorted_grid[0])
    
    for c in range(cols):
        for r in range(rows - 1):
            if sorted_grid[r][c] > sorted_grid[r+1][c]:
                return "NO"
    return "YES"
