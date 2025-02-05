def prime_numbers(N):
    n = [1] * N

    for k in range(2, N):
        if n[k] == 0:
            continue
        for i in range(k * 2, N, k):
            n[i] = 0
    with open("prime.csv", "a") as f:
        for k in range(1, N):
            if n[k] == 1:
                print(k)
                f.write(f"\n {str(k)},")


if __name__ == "__main__":
    with open("prime.csv", "a") as f:
        f.write("prime")
    prime_numbers(int(input("enter a natural number > ")))
