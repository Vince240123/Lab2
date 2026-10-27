def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average = calc_average(num_list)
    min_max_values = find_min_max(num_list)
    median_value = calc_median_temperature(num_list)
    print("Average: " + str(average))
    print("Minimum and Maximum values: " + str(min_max_values))
    print("Median: " + str(median_value))

def display_main_menu():
    print("display_main_menu")

def get_user_input():
    float_Input = []

    Input = input('Enter your float numbers: ')

    split_input = Input.split(',')

    for numbers in split_input:
        float_Input.append(float(numbers))

    print(float_Input)

    return(float_Input)

def calc_average(List):

    sum = 0

    for numbers in List:
        sum += numbers

    average_number = sum/ len(List)

    return average_number

def find_min_max(List):
    min_max = []
    min_number = 1000000
    max_number = 0
    for numbers in List:
        if numbers < min_number:
            min_number = numbers
        elif numbers > max_number:
            max_number = numbers

    min_max.append(min_number)
    min_max.append(max_number)

    return(min_max)

def sort_temparature(List):
    List.sort()
    return List

def calc_median_temperature(List):
    sorted_list = sort_temparature(List)
    length = len(List)
    if length % 2 == 0:
        median = (sorted_list[(length // 2)] + sorted_list[(length // 2) + 1]) / 2
    elif length % 2 == 1:
        median = sorted_list[length // 2]

    return median

if __name__ == "__main__":
    main()