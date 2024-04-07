def count_sort_numbers(arr, exp, index):
    arr_len = len(arr)
    
    output = [0] * arr_len
    arr_count = [0] * 10
    
    for i in range(arr_len):
        arr_index = arr[i][index] // exp
        arr_count[arr_index % 10] += 1
    
    for i in range(1, 10):
        arr_count[i] += arr_count[i - 1]
    
    i = arr_len - 1
    while i >= 0:
        arr_index = arr[i][index] // exp
        output[arr_count[arr_index % 10] - 1] = arr[i]
        arr_count[arr_index % 10] -= 1
        i -= 1
    
    for i in range(arr_len):
        arr[i] = output[i]
    
    return output

def radix_sort_Paitient_ID(arr):
    maximum_ID = max([data[0] for data in arr])
    exp = 1
    while (maximum_ID // exp) > 0:
        count_sort_numbers(arr, exp, 0)
        exp *= 10


def radix_sort_Paitient_age(arr):
    maximum_ID =  max([data[2] for data in arr])
    exp = 1
    
    while (maximum_ID // exp) > 0:
        count_sort_numbers(arr, exp, 2)
        exp *= 10

def print_record(arr):
    for record in patient_records:
        print("Patient ID: {:<3} Name: {:<18} Age: {:<3} Disease: {:<15} DOB: {:<12} Admitted Date: {:<12} Diagnosis: {:<30} Allergy History: {}".format(
            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]))
