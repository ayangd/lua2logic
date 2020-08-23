from .compiler import Compiler

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        if args.debug:
            Compiler().printChunk(f.read())
        else:
            print(Compiler().compile(f.read()))

if __name__ == '__main__':
    main()