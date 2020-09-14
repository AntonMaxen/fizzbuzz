def evendiv(x, n):
    return x % n == 0


def fizzbuzz(start, end, fizzdiv=3, buzzdiv=5, ultimate=42):
    lines = []
    for i in range(start, end + 1):
        fizz = evendiv(i, fizzdiv)
        buzz = evendiv(i, buzzdiv)
        tot_string = ""

        if i == ultimate:
            tot_string += "Answer to the Ultimate Question of Life, the Universe, and Everything"
        else:
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
