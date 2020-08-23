from .compiler import Compiler

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        print(Compiler().compile(f.read()))

if __name__ == '__main__':
    main()