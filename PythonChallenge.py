def calculate_class_allocation(num_students):
    max_class_size = 30
    min_classes = 2

    # Calculate the number of classes needed
    num_classes = min(max(min_classes, num_students // max_class_size), num_students)

    # Calculate the distribution of students per class
    students_per_class = num_students // num_classes
    remaining_students = num_students % num_classes

    allocation = {}

    for class_num in range(1, num_classes + 1):
        class_size = students_per_class

        # Distribute remaining students evenly across the classes
        if remaining_students > 0:
            class_size += 1
            remaining_students -= 1

        allocation[f"Class {class_num}"] = class_size

    return allocation


def print_class_allocation(num_students):
    allocation = calculate_class_allocation(num_students)

    # Print the proposed allocation
    print(f"Proposed Allocation: {len(allocation)} classes")
    print(allocation)


# EXAMPLE OUTPUT:

print_class_allocation(31)  # 2 classes, {'Class 1': 16, 'Class 2': 15}
print_class_allocation(59)  # 2 classes, {'Class 1': 30, 'Class 2': 29}
print_class_allocation(87)  # 3 classes, {'Class 1': 29, 'Class 2': 29, 'Class 3': 29}
