import sys

def read_array_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def calculate_steps(arr, target):
    steps = 0
    for num in arr:
        steps += abs(num - target)
    return steps

def main():
    filename = sys.argv[1]
    arr = read_array_from_file(filename)

    min_steps = float('inf')
    for target in arr:
        steps = calculate_steps(arr, target)
        if steps < min_steps:
            min_steps = steps
    print(f"Минимальное количество шагов: {min_steps}")

if __name__ == "__main__":
    main()
