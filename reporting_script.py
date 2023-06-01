import os
import json
import sys
from argparse import ArgumentParser
file_metadata = {}


def calculate_files_metadata(args: ArgumentParser) -> None:
    for root, _, files in os.walk(args.path):
        for _file in files:
            full_path = os.path.join(root, _file)
            bytes_size = os.path.getsize(full_path)
            mb_size = float(bytes_size/1024**2)
            if len(file_metadata) <= args.limit and mb_size > args.filesize:
                file_metadata[full_path] = f"{mb_size} MB"


def add_options_to_parse(parser: ArgumentParser) -> ArgumentParser:
    parser.add_argument('-p', '--path',
                        required=True,
                        type=str,
                        help='The path which needs to be traversed.')
    parser.add_argument('-l', '--limit',
                        type=int,
                        default=sys.maxsize,
                        help='Limit number of files added to report.')
    parser.add_argument("-fs", "--filesize",
                        default=0.0,
                        type=float,
                        help="Mention file size in MB to narrow the reporting.")
    return parser


def main():
    parser = ArgumentParser()
    add_options_to_parse(parser)
    args = parser.parse_args()
    calculate_files_metadata(args)
    print(json.dumps(file_metadata, indent=2))


if __name__ == '__main__':
    main()
