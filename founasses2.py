# Section 3:

def calculate_classes(num_students):
    # Ensure there are at least 2 classes
    if num_students <= 0:
        raise ValueError("The number of students must be a positive integer")
    elif num_students <= 30:
        num_classes = 2
        num_students_per_class = num_students // num_classes
        remaining_students = num_students % num_classes
    else:
        # Determine the number of classes needed
        num_classes = (num_students + 29) // 30
        num_students_per_class = num_students // num_classes
        remaining_students = num_students % num_classes

    # Calculate the allocation for each class
    allocation = {}
    for i in range(1, num_classes + 1):
        if i <= remaining_students:
            allocation[f"Class {i}"] = num_students_per_class + 1
        else:
            allocation[f"Class {i}"] = num_students_per_class

    # Print the proposed allocation and the allocation dictionary
    print(f"Proposed Allocation: {num_classes} classes")
    print(allocation)

num_students = 87
calculate_classes(num_students)


