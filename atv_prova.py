def main():
    k = int()
    i = int()
    n = int()

    print("k=", k, "i=", i, "n=", n)

    n = int(input())
    print("k=", k, "i=", i, "n=", n)

    k = 1
    print("k=", k, "i=", i, "n=", n)

    i= 2
    print("k=", k, "i=", i, "n=", n)
    
    while i <= n:
        k = k * i
        print("k=", k, "i=", i, "n=", n)
        i = i + 1
        print("k=", k, "i=", i, "n=", n)
    print("k=", k, "i=", i, "n=", n)


main()