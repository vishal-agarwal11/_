# program to calculate the prime factors
# Sample
# Input: 333
# Output: [3, 3, 37]


def get_prine_factor(number):
    prime_factors = []
    factor = 2
    while number > 1:
        if number % factor == 0:
            prime_factors.append(factor)
            number = number//factor
        else:
            factor += 1
    return prime_factors


if __name__ == "__main__":
    print(get_prine_factor(333))
