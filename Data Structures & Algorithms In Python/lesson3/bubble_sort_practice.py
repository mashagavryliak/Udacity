def bubble_sort_iteration(numbers):

    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers


numbers = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
for i in range(3):
    numbers = bubble_sort_iteration(numbers)
    print numbers
print numbers
print (190**4 - 120/0.3)*1780
