import argparse


def golden_horse_parser():
    parser = argparse.ArgumentParser(
        description='Clean golden horse schedule.csv',
    )
    parser.add_argument(
        '-i',
        '--input',
        type=str,
        help='Path to raw csv',
    )
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        help='Path to output csv',
    )
    parser.add_argument(
        '-enc',
        '--encoding',
        type=str,
        default='big5',
        help='How to encode the file',
    )
    return parser
