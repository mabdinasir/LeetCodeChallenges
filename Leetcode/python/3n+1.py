import random

# Colatz conjecture
# The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: 
# start with any positive integer n. Then each term is obtained from the previous term as follows: 
# if the previous term is even, the next term is one half the previous term. 
# Otherwise, the next term is 3 times the previous term plus 1. 
# The conjecture is that no matter what value of n, the sequence will always reach 1.

class Solution:
    def three_n_plus_one(self):
        n = 10000000
        for n in range(1, n):
            result = self.compute(n)
            color = self.get_random_color()
            print("\033[38;5;"+str(int(color))+"m"+str([int(num) for num in result])+"\033[0m", "\033[38;5;"+str(int(color))+"m"+str(len(result))+"\033[0m")
            if result[-1] != 1:
                print("This number does not reach 1. The Collatz conjecture has been cracked. Last number in sequence:", result[-1])
                break

    def compute(self, n):
        result = []
        result.append(n)
        while n != 1:
            if n % 2 == 0:
                n = n / 2
                result.append(n)
            else:
                n = 3 * n + 1
                result.append(n)
        return result

    def get_random_color(self):
        colors = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]
        return random.choice(colors)

s = Solution()
print(s.three_n_plus_one())
