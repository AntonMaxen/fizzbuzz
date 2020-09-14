def fizzbuzz(start, end):
    evendived = lambda x, n: x % n == 0
    lines = []
    for i in range(start, end + 1):
        fizz = evendived(i, 3)
        buzz = evendived(i, 5)
        tot_string = ""
        if fizz:
            tot_string += "fizz"

        if buzz:
            tot_string += "buzz"

        if not fizz and not buzz:
            tot_string += str(i)

        lines.append(tot_string)

    return lines


def main():
    print("\n".join(fizzbuzz(1, 100)))


if __name__ == '__main__':
    main()
