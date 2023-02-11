import argparse
import fileinput

from fzm.app import run


def main():
    args = cli()
    source = get_input(args.inp)
    run(source)


def cli():
    parser = argparse.ArgumentParser(
        prog="fzm",
        description="commandline fuzzy matcher",
        epilog="https://www.github.com/windrim/fzm"
    )

    parser.add_argument("inp", metavar="input")
    args = parser.parse_args()
    return args
    

def get_input(arg: str) -> list[str]:
    return [line.rstrip() for line in fileinput.input(files=(arg,))]

