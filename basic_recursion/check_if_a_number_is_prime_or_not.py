class Solution:
    def isPrime(self, num, x):
        # If x exceeds the square root of num, no factors found, so num is prime
        if x > (num ** 0.5):
            return True
        
        # If num is divisible by x, it is not a prime number
        if (num % x) == 0:
            return False
        
        # Recursively check the next possible factor
        return self.isPrime(num, (x + 1))

    def checkPrime(self, num):
        # Numbers less than or equal to 1 are not prime
        if num <= 1:
            return False

        # Start checking for factors from 2 upwards
        return self.isPrime(num, 2)

if __name__ == "__main__":
    sol = Solution()
    num = int(input())

    print(sol.checkPrime(num))