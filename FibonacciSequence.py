
from typing import List

def generate_fibonacci(count: int) -> List[int]:
    if count <= 0:
        return []
    sequence = []
    a,b = 0,1

    for _ in range(n_terms):
        sequence.append(a)
        a, b = b, a+b
    return sequence
def get_valid_input() -> int:
    while True:
        try:
            val = int(input("Enter the number of terms: "))
            if val > 0:
                return val
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid Input !!, Please enter a positive integer/ a numeric whole number.")
if __name__ == "__main__":
    n_terms = get_valid_input()
    fib_list = generate_fibonacci(n_terms)
    print(f"\nGenerated Sequence({n_terms}terms):")
    print(fib_list)
