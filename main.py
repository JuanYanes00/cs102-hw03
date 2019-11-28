import sys
from statistics import mean

def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")
    with open(input_file_path, "r") as f:
        for line in f:
            splittedlines = line.split(",")
            empty = []
            for x in splittedlines:
                empty.append(float(x))
            print(f"{mean(empty)}")

if __name__ == "__main__":
    main()
