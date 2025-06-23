from pathlib import Path


def fibonacci(n: int, k: int):
    nums: list[int] = []
    if n <= 0:
        raise ValueError("n cannot be less than 1")

    for idx in range(n):
        if idx == 0 or idx == 1:
            nums.append(1)
        else:
            nums.append(nums[idx - 1] + k * nums[idx - 2])

    return nums[n - 1]


def run_fib(data_path: Path):
    print("***** Running FIB task *****")
    with open(f"{data_path}/rosalind_fib.txt", "r") as f:
        [n, k] = f.readline().split(" ")
    fib = fibonacci(int(n), int(k))

    print(f"Number of pairs of rabbits:\t{fib}")
