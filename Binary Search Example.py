# Have a user input for target

arr = ["Arturo", "Elsa", "JoAnn", "John", "Jose", "Lee", "Snyder", "Tracy"]

# Change input type to string and modify the prompt
target = input("Enter a name to search for: ")


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    compared_names = []  # List to store the names that are compared

    print(f"Searching for {target}...")

    while low <= high:
        mid = (low + high) // 2
        print(f"Low: {low}, High: {high}, Mid: {mid}, Checking: {arr[mid]}")

        compared_names.append(arr[mid])  # Add the name being compared to the list

        if arr[mid] == target:
            print(f"Found {target} at index {mid}\n")
            print(f"{target} was compared to {', '.join(compared_names)}")
            return mid
        elif arr[mid] < target:
            print(f"{arr[mid]} is less than {target}, searching the right half.")
            low = mid + 1
        else:
            print(f"{arr[mid]} is greater than {target}, searching the left half.")
            high = mid - 1

    print(f"{target} not found.\n")
    print(f"{target} was compared to {', '.join(compared_names)}")
    return "Not Found"


# Run the binary search function
binary_search(arr, target)
