from parsers import golden_horse_parser


parser = golden_horse_parser()
args = parser.parse_args()
REDUNDANT_INFO_LINE_NUM = 4
TRAILING_USELESS_INFO_LINE_NUM = -1


def clean_line(string, remove_trainling_position=-2):
    return string.replace('\t', '').split(',')[:remove_trainling_position]


def main():
    with open(args.input, encoding=args.encoding) as file_handle:
        lines = file_handle.readlines()[
            REDUNDANT_INFO_LINE_NUM:TRAILING_USELESS_INFO_LINE_NUM
        ]
        cleaned_lines = [
            clean_line(line) for line in lines
        ]

    with open(args.output, 'w') as file_handle:
        for line in cleaned_lines:
            file_handle.write(f'{",".join(line)}\n')


if __name__ == '__main__':
    main()
