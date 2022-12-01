from wmg import WMG


def main() -> None:
    parser = WMG()
    parser.read_file('1994_Formula_One.wmg')
    parser.parse_file()


if __name__ == '__main__':
    main()
