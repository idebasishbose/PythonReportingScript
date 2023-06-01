import os
import json
from argparse import ArgumentParser
file_metadata = {}


def calculate_files_metadata(path: str) -> None:
    for root, _, files in os.walk(path):
        for _file in files:
            full_path = os.path.join(root, _file)
            size = os.path.getsize(full_path)
            file_metadata[full_path] = size


def add_options_to_parse(parser: ArgumentParser) -> ArgumentParser:
    parser.add_argument('-p', '--path', required=True,
                        help='The path which needs to be traversed.')
    return parser


def main():
    parser = ArgumentParser()
    add_options_to_parse(parser)
    args = parser.parse_args()
    calculate_files_metadata(args.path)
    print(json.dumps(file_metadata, indent=2))


if __name__ == '__main__':
    main()
