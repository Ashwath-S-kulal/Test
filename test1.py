def disarium(num):
    total = 0
    num_str = str(num)
    for index, digit in enumerate(num_str, start=1):
        total += int(digit) ** index
    return total == num

def firstNDisarium(n):
    result = []
    num = 0
    while len(result) < n:
        if disarium(num):
            result.append(num)
        num += 1
    return result

def disariumBetween(start, end):
    return [num for num in range(start, end + 1) if disarium(num)]

if __name__ == "__main__":
    n = int(input("Enter how many Disarium numbers you want: "))
    print(f"First {n} Disarium numbers are: {firstNDisarium(n)}")

    start = int(input("\nEnter start of range: "))
    end = int(input("Enter end of range: "))
    print(f"Disarium numbers between {start} and {end} are: {disariumBetween(start, end)}")
