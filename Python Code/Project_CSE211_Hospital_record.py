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
            print("\033[1;37mPatient ID: {:<3} Name: {:<18} Age: {:<3} Blood group: {:<3} Disease: {:<15} DOB: {:<12} Admitted Date: {:<12} Diagnosis: {:<30} Allergy 1: {}, {}".format(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8][0], record[8][1]))

def hospital_record_application(rec):
    app = HospitalRecord(rec)
    def eq():
        print('\033[1;32m' + '=' * 47)

    def print_records():
        print('\033[1;32m' + '*' * 220)
        app.print_record()
        print('\033[1;32m' + '*' * 220)

    while True:
        eq()
        print('\033[1;31m' + '-' * 15, 'HOSPITAL RECORD', '-' * 15)
        eq()
        print('\033[1;37m' + 'Please choose from the options below:-')
        print('\033[1;37m' + '1. Sort data by Patient ID \n2. Sort Data by Patient Name\n3. Sort Data by Patient Age\n4. Sort Data by Patient Blood Group\n5. Sort Data by Patient Disease\n6. Sort Data by Patient Date of Birth\n7. Sort data by Hospital admitted date\n8. Sort data by allergy 1\n9. Sort data by allergy 2\n10. View Patient Record(press v)\n11. Quit')
        eq()
        user_input = input('\033[1;37m' + 'Please Enter your option: ')
        if user_input == '1':
            app.radix_sort_Patient_ID()
            print_records()
        elif user_input == '2':
            app.radix_sort_string(1)
            print_records()
        elif user_input == '3':
            app.radix_sort_Patient_age()
            print_records()
        elif user_input == '4':
            app.radix_sort_string(3)
            print_records()
        elif user_input == '5':
            app.radix_sort_string(4)
            print_records()
        elif user_input == '6':
            app.radix_sort_string(5)
            print_records()
        elif user_input == '7':
            app.radix_sort_string(6)
            print_records()
        elif user_input == '8':
            app.radix_sort_string(7)
            print_records()
        elif user_input == '9':
            app.radix_sort_string(8)
            print_records()
        elif user_input == '11' or user_input == 'quit' or user_input == 'q':
            eq()
            print('\033[1;31m' + "Program ended")
            eq()
            break
        else:
            print('\033[1;31m' + 'Wrong Input please select from the above options only.')

# Patient ID, name, Age, blood group, disease, date of birth, admitted data, diagnosis, allergy history
patient_records = [
    [9, 'James Martinez', 32, 'AB', 'Anemia', '1992-09-08', '2024-03-09', 'Anemia diagnosis', ['Peanuts', 'Penicillin']],
    [20, 'Charlotte Robinson', 70, 'O', 'Asthma', '1954-08-21', '2024-02-22', 'Asthma diagnosis', ['Shellfish', 'Soy']],
    [42, 'Gabriel Rivera', 39, 'B', 'Flu', '1985-11-30', '2024-01-18', 'Flu diagnosis', ['Penicillin', 'Shellfish']],
    [21, 'William Clark', 38, 'A', 'Bronchitis', '1986-06-14', '2024-02-21', 'Bronchitis diagnosis', ['Penicillin', 'Pollen']],
    [25, 'Logan Walker', 27, 'A', 'Flu', '1997-01-01', '2024-02-15', 'Flu diagnosis', ['Penicillin', 'Milk']],
    [47, 'Brooklyn Gutiérrez', 33, 'B', 'Bronchitis', '1991-07-17', '2024-01-09', 'Bronchitis diagnosis', ['Penicillin', 'Wheat']],
    [23, 'Evelyn Lewis', 33, 'O', 'Eczema', '1991-07-26', '2024-02-18', 'Eczema diagnosis', ['Pollen', 'Dust']],
    [17, 'Ava Thompson', 43, 'AB', 'Pneumonia', '1981-04-03', '2024-02-26', 'Pneumonia diagnosis', ['Dust', 'Milk']],
    [12, 'Liam Jackson', 36, 'A', 'Bronchitis', '1988-09-20', '2024-03-05', 'Bronchitis diagnosis', ['Peanuts', 'Penicillin']],
    [1, 'John Doe', 35, 'O', 'Hypertension', '1989-05-15', '2024-03-20', 'High blood pressure diagnosis', ['Penicillin', 'Dust']],
    [4, 'Jane Williams', 28, 'A', 'Migraine', '1996-12-10', '2024-03-15', 'Migraine diagnosis', ['Shellfish', 'Milk']], 
    [46, 'Lucas Bell', 57, 'O', 'Asthma', '1967-01-02', '2024-01-11', 'Asthma diagnosis', ['Shellfish', 'Milk']],
    [30, 'Aria King', 40, 'A', 'Migraine', '1984-04-18', '2024-02-07', 'Migraine diagnosis', ['Peanuts', 'Soy']],
    [15, 'Emma Johnson', 62, 'O', 'Arthritis', '1962-07-15', '2024-03-01', 'Arthritis diagnosis', ['Penicillin', 'Wheat']],
    [22, 'Harper Rodriguez', 47, 'B', 'Diabetes', '1977-09-05', '2024-02-20', 'Diabetes diagnosis', ['Peanuts', 'Soy']],
    [33, 'Mateo Hill', 51, 'B', 'Diabetes', '1973-12-17', '2024-02-02', 'Diabetes diagnosis', ['Peanuts', 'Dust']],
    [6, 'Emily Davis', 75, 'O', 'Flu', '1949-11-05', '2024-03-13', 'Flu diagnosis', ['Penicillin', 'Soy']],
    [38, 'Victoria Perez', 59, 'AB', 'Pneumonia', '1965-04-29', '2024-01-25', 'Pneumonia diagnosis', ['Shellfish', 'Dust']],
    [40, 'Nathan Flores', 46, 'A', 'Migraine', '1978-01-24', '2024-01-21', 'Migraine diagnosis', ['Pollen', 'Penicillin']],
    [14, 'Noah Harris', 45, 'B', 'Diabetes', '1979-05-28', '2024-03-02', 'Diabetes diagnosis', ['Pollen', 'Milk']],
    [10, 'Emma Anderson', 58, 'O', 'Eczema', '1966-07-12', '2024-03-08', 'Eczema diagnosis', ['Pollen', 'Soy']],
    [35, 'Mason Green', 42, 'A', 'Hypertension', '1982-07-20', '2024-01-30', 'High blood pressure diagnosis', ['Peanuts', 'Shellfish']],
    [24, 'James Lee', 57, 'A', 'Arthritis', '1967-03-17', '2024-02-17', 'Arthritis diagnosis', ['Peanuts', 'Wheat']],
    [13, 'Isabella White', 50, 'B', 'Hypertension', '1974-11-12', '2024-03-03', 'High blood pressure diagnosis', ['Shellfish', 'Dust']],
    [44, 'Leo Reed', 28, 'O', 'Anemia', '1995-06-26', '2024-01-15', 'Anemia diagnosis', ['Peanuts', 'Dust']],
    [34, 'Camila Scott', 30, 'O', 'Anemia', '1993-09-08', '2024-01-31', 'Anemia diagnosis', ['Pollen', 'Penicillin']]
]

hospital_record_application(patient_records)
