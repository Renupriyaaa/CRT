def sum_of_digits(n: int) -> int:
    s = 0
    for digit in str(n):
        s += int(digit)
    return s

if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))