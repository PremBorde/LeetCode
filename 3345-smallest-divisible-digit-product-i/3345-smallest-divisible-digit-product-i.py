class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(x):
            product = 1
            while x > 0:
                product *= (x % 10)  # 1 * 0 = 0 
                x //= 10
            return product

        # Start checking from n upwards
        while True:
            if digit_product(n) % t == 0:
                return n
            n += 1
# product = 1
# last digit = 5 → product = 1 * 5 = 5
# remove digit → x = 1
# last digit = 1 → product = 5 * 1 = 5
# remove digit → x = 0 → stop
# Result = 5
# Check 5 % 6 == 0 → ❌ not divisible
# So increment n = 16