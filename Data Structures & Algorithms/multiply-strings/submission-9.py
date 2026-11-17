class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                product = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += product
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10
        
        res = res[::-1]
        i = 0
        while res[i] == 0 and i < len(res):
            i += 1
        
        total = map(str, res[i:])

        return "".join(total)

        