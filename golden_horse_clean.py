from parsers import golden_horse_parser


parser = golden_horse_parser()
args = parser.parse_args()
REDUNDANT_INFO_LINE_NUM = 4
TRAILING_USELESS_INFO_LINE_NUM = -1


def main():
    with open(args.input, encoding=args.encoding) as file_handle:
        lines = file_handle.readlines()[
            REDUNDANT_INFO_LINE_NUM:TRAILING_USELESS_INFO_LINE_NUM
        ]


if __name__ == '__main__':
    main()
