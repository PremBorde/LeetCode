from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m, n = len(grid), len(grid[0])   # grid ke rows (m) aur columns (n) nikal lo
        total = m * n                    # total elements count kar lo

        # Step 1: Flatten grid (2D → 1D list)
        flat = []
        for i in range(m):               # har row ke liye
            for j in range(n):           # har column ke liye
                flat.append(grid[i][j])  # element ko flat list me daal do

        # Step 2: Shift list by k positions
        k = k % total                    # agar k bada hai to modulo se adjust karo
        shifted = []
        # last ke k elements pehle daalo
        for i in range(total - k, total):
            shifted.append(flat[i])
        # baaki elements baad me daalo
        for i in range(total - k):
            shifted.append(flat[i])

        # Step 3: Rebuild into 2D grid (1D → 2D)
        result = []
        for i in range(m):               # har row ke liye
            row = []
            start = i * n                # row ka start index
            end = (i + 1) * n            # row ka end index
            for j in range(start, end):  # us range ke elements uthao
                row.append(shifted[j])
            result.append(row)           # row ko result me daal do

        return result
