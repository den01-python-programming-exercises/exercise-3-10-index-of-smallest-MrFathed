def main():
    #write your code below this line
    numbers = []

    while True:
        number = int(input())

        if number == 9999:
            break

        numbers.append(number)

    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number

    print("Smallest number: " + str(smallest))

    for i in range(len(numbers)):
        if numbers[i] == smallest:
            print("Found at index: " + str(i))

if __name__ == '__main__':
    main()
