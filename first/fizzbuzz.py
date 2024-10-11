# シンプルなFizzBuzz
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# なぜこれでFizzBuzzができるか考えてみよう
def fizzbuzz_oneliner(n):
    print("\n".join(("" if i % 3 else "Fizz") + ("" if i % 5 else "Buzz") + (str(i) if (i % 3) * (i % 5) else "") for i in range(1, n + 1)))


if __name__ == "__main__":
    n = 30
    fizzbuzz(n)
    # fizzbuzz_oneliner(n)
