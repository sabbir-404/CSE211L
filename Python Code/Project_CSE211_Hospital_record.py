class HospitalRecord:
    def __init__(self, arr):
        self.patient_records = arr

    def count_sort_numbers(self, arr, exp, index):
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

    def count_sort_strings(self, arr, char_index, index):
        arr_len = len(arr)
        output = [0] * arr_len
        arr_count = [0] * 256
        
        for i in range(arr_len):
            if char_index < len(arr[i][index]):
                char_val = ord(arr[i][index][char_index])
                arr_count[char_val] += 1
            else:
                arr_count[0] += 1
        
        for i in range(1, 256):
            arr_count[i] += arr_count[i - 1]
        
        i = arr_len - 1
        while i >= 0:
            if char_index < len(arr[i][index]):
                char_val = ord(arr[i][index][char_index])
                output[arr_count[char_val] - 1] = arr[i]
                arr_count[char_val] -= 1
            else:
                output[arr_count[0] - 1] = arr[i]
                arr_count[0] -= 1
            
            i -= 1

        for i in range(arr_len):
            arr[i] = output[i]

    def radix_sort_Patient_ID(self):
        maximum_ID = max([data[0] for data in self.patient_records])
        exp = 1
        
        while (maximum_ID // exp) > 0:
            self.count_sort_numbers(self.patient_records, exp, 0)
            exp *= 10

    def radix_sort_Patient_age(self):
        maximum_age = max([data[2] for data in self.patient_records])
        exp = 1
        
        while (maximum_age // exp) > 0:
            self.count_sort_numbers(self.patient_records, exp, 2)
            exp *= 10

    def radix_sort_string(self, index):
        max_len = max(len(str(record[index])) for record in self.patient_records)
        
        for i in range(len(self.patient_records)):
            if isinstance(self.patient_records[i][index], list):
                self.patient_records[i][index] = ', '.join(self.patient_records[i][index])
            
            self.patient_records[i][index] = str(self.patient_records[i][index]).ljust(max_len)

        for char_index in range(max_len - 1, -1, -1):
            self.count_sort_strings(self.patient_records, char_index, index)

        for i in range(len(self.patient_records)):
            self.patient_records[i][index] = str(self.patient_records[i][index]).rstrip()


    def print_record(self):
        for record in self.patient_records:
            print("Patient ID: {:<3} Name: {:<18} Age: {:<3} Blood group: {:<3} Disease: {:<15} DOB: {:<12} Admitted Date: {:<12} Diagnosis: {:<30} Allergy 1: {}, {}".format(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8][0], record[8][1]))

def hospital_record_application(rec):
    app = HospitalRecord(rec)
    def eq():
        print('=' * 47)

    def print_records():
        print('*' * 220)
        app.print_record()
        print('*' * 220)

    while True:
        eq()
        print('-' * 15, 'HOSPITAL RECORD', '-' * 15)
        eq()
        print('Please choose from the options below:-')
        print('1. Sort data by Patient ID \n2. Sort Data by Patient Name\n3. Sort Data by Patient Age\n4. Sort Data by Patient Blood Group\n5. Sort Data by Patient Disease\n6. Sort Data by Patient Date of Birth\n7. Sort data by Hospital admitted date\n8. Sort data by allergy 1\n9. Sort data by allergy 2\n10. View Patient Record(press v)\n11. Quit')
        eq()
        user_input = input('Please Enter your option: ')
        if user_input == '1':
            app.radix_sort_Patient_ID()
            eq()
            print('\033[94m;Data sorted by Patient ID')
            eq()
            print_records()
        elif user_input == '2':
            app.radix_sort_string(1)
            eq()
            print('\033[94m;Data sorted by Patient Name')
            eq()
            print_records()
        elif user_input == '3':
            app.radix_sort_Patient_age()
            eq()
            print('\033[94m;Data sorted by Patient Age')
            eq()
            print_records()
        elif user_input == '4':
            app.radix_sort_string(3)
            eq()
            print('\033[94m;Data sorted by Patient Blood Group')
            eq()
            print_records()
        elif user_input == '5':
            app.radix_sort_string(4)
            eq()
            print('\033[94m;Data sorted by Patient Disease')
            eq()
            print_records()
        elif user_input == '6':
            app.radix_sort_string(5)
            eq()
            print('\033[94m;Data sorted by Patient Date of Birth')
            eq()
            print_records()
        elif user_input == '7':
            app.radix_sort_string(6)
            eq()
            print('\033[94m;Data sorted by Patient Admitted Data')
            eq()
            print_records()
        elif user_input == '8':
            app.radix_sort_string(7)
            eq()
            print('\033[94m;Data sorted by Patient Diagnosis')
            eq()
            print_records()
        elif user_input == '9':
            app.radix_sort_string(8)
            eq()
            print('\033[94m;Data sorted by Patient Allergy History')
            eq()
            print_records()
        elif user_input == '11' or user_input == 'quit' or user_input == 'q':
            eq()
            eq()
            print("Program ended")
            eq()
            eq()
            break
        else:
            print('Wrong Input please select from the above options only.')


#Sample data
# paitient ID, name, Age,blood group, disease, date of birth, admitted data, diagnosis, allergy history
patient_records = [
    [4871, 'James Martinez', 32, 'AB', 'Anemia', '1992-09-08', '2024-03-09', 'Anemia diagnosis', 'Peanuts'],
    [2765, 'Charlotte Robinson', 70, 'O', 'Asthma', '1954-08-21', '2024-02-22', 'Asthma diagnosis', 'Shellfish'],
    [8942, 'Gabriel Rivera', 39, 'B', 'Flu', '1985-11-30', '2024-01-18', 'Flu diagnosis', 'Penicillin'],
    [5928, 'William Clark', 38, 'A', 'Bronchitis', '1986-06-14', '2024-02-21', 'Bronchitis diagnosis', 'Penicillin'],
    [3276, 'Logan Walker', 27, 'A', 'Flu', '1997-01-01', '2024-02-15', 'Flu diagnosis', 'Penicillin'],
    [6754, 'Brooklyn Gutiérrez', 33, 'B', 'Bronchitis', '1991-07-17', '2024-01-09', 'Bronchitis diagnosis', 'Penicillin'],
    [4189, 'Evelyn Lewis', 33, 'O', 'Eczema', '1991-07-26', '2024-02-18', 'Eczema diagnosis', 'Pollen'],
    [1897, 'Ava Thompson', 43, 'AB', 'Pneumonia', '1981-04-03', '2024-02-26', 'Pneumonia diagnosis', 'Dust'],
    [7532, 'Liam Jackson', 36, 'A', 'Bronchitis', '1988-09-20', '2024-03-05', 'Bronchitis diagnosis', 'Peanuts'],
    [5210, 'John Doe', 35, 'O', 'Hypertension', '1989-05-15', '2024-03-20', 'High blood pressure diagnosis', 'Penicillin'],
    [3198, 'Jane Williams', 28, 'A', 'Migraine', '1996-12-10', '2024-03-15', 'Migraine diagnosis', 'Shellfish'], 
    [8314, 'Lucas Bell', 57, 'O', 'Asthma', '1967-01-02', '2024-01-11', 'Asthma diagnosis', 'Shellfish'],
    [6427, 'Aria King', 40, 'A', 'Migraine', '1984-04-18', '2024-02-07', 'Migraine diagnosis', 'Peanuts'],
    [4863, 'Emma Johnson', 62, 'O', 'Arthritis', '1962-07-15', '2024-03-01', 'Arthritis diagnosis', 'Penicillin'],
    [2685, 'Harper Rodriguez', 47, 'B', 'Diabetes', '1977-09-05', '2024-02-20', 'Diabetes diagnosis', 'Peanuts'],
    [9245, 'Mateo Hill', 51, 'B', 'Diabetes', '1973-12-17', '2024-02-02', 'Diabetes diagnosis', 'Peanuts'],
    [1786, 'Emily Davis', 75, 'O', 'Flu', '1949-11-05', '2024-03-13', 'Flu diagnosis', 'Penicillin'],
    [5432, 'Victoria Perez', 59, 'AB', 'Pneumonia', '1965-04-29', '2024-01-25', 'Pneumonia diagnosis', 'Shellfish'],
    [7162, 'Nathan Flores', 46, 'A', 'Migraine', '1978-01-24', '2024-01-21', 'Migraine diagnosis', 'Pollen'],
    [3498, 'Noah Harris', 45, 'B', 'Diabetes', '1979-05-28', '2024-03-02', 'Diabetes diagnosis', 'Pollen'],
    [6271, 'Emma Anderson', 58, 'O', 'Eczema', '1966-07-12', '2024-03-08', 'Eczema diagnosis', 'Pollen'],
    [8954, 'Mason Green', 42, 'A', 'Hypertension', '1982-07-20', '2024-01-30', 'High blood pressure diagnosis', 'Peanuts'],
    [4109, 'James Lee', 57, 'A', 'Arthritis', '1967-03-17', '2024-02-17', 'Arthritis diagnosis', 'Peanuts'],
    [2356, 'Isabella White', 50, 'B', 'Hypertension', '1974-11-12', '2024-03-03', 'High blood pressure diagnosis', 'Shellfish'],
    [6792, 'Leo Reed', 28, 'O', 'Anemia', '1995-06-26', '2024-01-15', 'Anemia diagnosis', 'Peanuts'],
    [9127, 'Camila Scott', 30, 'O', 'Anemia', '1993-09-08', '2024-01-31', 'Anemia diagnosis', 'Pollen']
]


#Application call
hospital_record_application(patient_records)