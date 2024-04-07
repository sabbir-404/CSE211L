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
        
        return output

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
        max_len = max(len(record[index]) for record in self.patient_records)
        
        for i in range(len(self.patient_records)):
            self.patient_records[i][index] = self.patient_records[i][index].ljust(max_len)

        for char_index in range(max_len - 1, -1, -1):
            self.count_sort_strings(self.patient_records, char_index, index)

        for i in range(len(self.patient_records)):
            self.patient_records[i][index] = self.patient_records[i][index].rstrip()

    def print_record(self):
        for record in self.patient_records:
            print("Patient ID: {:<3} Name: {:<18} Age: {:<3} Disease: {:<15} DOB: {:<12} Admitted Date: {:<12} Diagnosis: {:<30} Allergy History: {}".format(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]))



# paitient ID, name, Age, disease, date of birth, admitted data, diagnosis, allergy history
patient_records = [
    [9, 'James Martinez', 32, 'Anemia', '1992-09-08', '2024-03-09', 'Anemia diagnosis', ['Peanuts', 'Penicillin']],
    [20, 'Charlotte Robinson', 70, 'Asthma', '1954-08-21', '2024-02-22', 'Asthma diagnosis', ['Shellfish', 'Soy']],
    [42, 'Gabriel Rivera', 39, 'Flu', '1985-11-30', '2024-01-18', 'Flu diagnosis', ['Penicillin', 'Shellfish']],
    [21, 'William Clark', 38, 'Bronchitis', '1986-06-14', '2024-02-21', 'Bronchitis diagnosis', ['Penicillin', 'Pollen']],
    [25, 'Logan Walker', 27, 'Flu', '1997-01-01', '2024-02-15', 'Flu diagnosis', ['Penicillin', 'Milk']],
    [47, 'Brooklyn Gutiérrez', 33, 'Bronchitis', '1991-07-17', '2024-01-09', 'Bronchitis diagnosis', ['Penicillin', 'Wheat']],
    [23, 'Evelyn Lewis', 33, 'Eczema', '1991-07-26', '2024-02-18', 'Eczema diagnosis', ['Pollen', 'Dust']],
    [17, 'Ava Thompson', 43, 'Pneumonia', '1981-04-03', '2024-02-26', 'Pneumonia diagnosis', ['Dust', 'Milk']],
    [12, 'Liam Jackson', 36, 'Bronchitis', '1988-09-20', '2024-03-05', 'Bronchitis diagnosis', ['Peanuts', 'Penicillin']],
    [1, 'John Doe', 35, 'Hypertension', '1989-05-15', '2024-03-20', 'High blood pressure diagnosis', ['Penicillin', 'Dust']],
    [4, 'Jane Williams', 28, 'Migraine', '1996-12-10', '2024-03-15', 'Migraine diagnosis', ['Shellfish', 'Milk']],
    [46, 'Lucas Bell', 57, 'Asthma', '1967-01-02', '2024-01-11', 'Asthma diagnosis', ['Shellfish', 'Milk']],
    [30, 'Aria King', 40, 'Migraine', '1984-04-18', '2024-02-07', 'Migraine diagnosis', ['Peanuts', 'Soy']],
    [15, 'Emma Johnson', 62, 'Arthritis', '1962-07-15', '2024-03-01', 'Arthritis diagnosis', ['Penicillin', 'Wheat']],
    [22, 'Harper Rodriguez', 47, 'Diabetes', '1977-09-05', '2024-02-20', 'Diabetes diagnosis', ['Peanuts', 'Soy']],
    [33, 'Mateo Hill', 51, 'Diabetes', '1973-12-17', '2024-02-02', 'Diabetes diagnosis', ['Peanuts', 'Dust']],
    [6, 'Emily Davis', 75, 'Flu', '1949-11-05', '2024-03-13', 'Flu diagnosis', ['Penicillin', 'Soy']],
    [38, 'Victoria Perez', 59, 'Pneumonia', '1965-04-29', '2024-01-25', 'Pneumonia diagnosis', ['Shellfish', 'Dust']],
    [40, 'Nathan Flores', 46, 'Migraine', '1978-01-24', '2024-01-21', 'Migraine diagnosis', ['Pollen', 'Penicillin']],
    [14, 'Noah Harris', 45, 'Diabetes', '1979-05-28', '2024-03-02', 'Diabetes diagnosis', ['Pollen', 'Milk']],
    [10, 'Emma Anderson', 58, 'Eczema', '1966-07-12', '2024-03-08', 'Eczema diagnosis', ['Pollen', 'Soy']],
    [35, 'Mason Green', 42, 'Hypertension', '1982-07-20', '2024-01-30', 'High blood pressure diagnosis', ['Peanuts', 'Shellfish']],
    [24, 'James Lee', 57, 'Arthritis', '1967-03-17', '2024-02-17', 'Arthritis diagnosis', ['Peanuts', 'Wheat']],
    [13, 'Isabella White', 50, 'Hypertension', '1974-11-12', '2024-03-03', 'High blood pressure diagnosis', ['Shellfish', 'Dust']],
    [44, 'Leo Reed', 28, 'Anemia', '1995-06-26', '2024-01-15', 'Anemia diagnosis', ['Peanuts', 'Dust']],
    [34, 'Camila Scott', 30, 'Anemia', '1993-09-08', '2024-01-31', 'Anemia diagnosis', ['Pollen', 'Penicillin']],
    [11, 'Sophia Moore', 24, 'Flu', '2000-03-08', '2024-03-07', 'Flu diagnosis', ['Pollen', 'Shellfish']],
    [48, 'Penelope Simmons', 51, 'Pneumonia', '1973-11-24', '2024-01-08', 'Pneumonia diagnosis', ['Peanuts', 'Milk']],
    [36, 'Hannah Adams', 64, 'Asthma', '1960-10-13', '2024-01-28', 'Asthma diagnosis', ['Penicillin', 'Soy']],
    [8, 'Olivia Taylor', 68, 'Arthritis', '1956-02-17', '2024-03-10', 'Arthritis diagnosis', ['Dust', 'Milk']],
    [29, 'Scarlett Hernandez', 56, 'Pneumonia', '1968-08-04', '2024-02-09', 'Pneumonia diagnosis', ['Penicillin', 'Milk']],
    [27, 'Sofia Allen', 61, 'Asthma', '1963-05-22', '2024-02-12', 'Asthma diagnosis', ['Shellfish', 'Milk']],
    [7, 'David Wilson', 41, 'Pneumonia', '1983-06-30', '2024-03-12', 'Pneumonia diagnosis', ['Shellfish', 'Wheat']],
    [2, 'Alice Smith', 45, 'Diabetes', '1979-10-22', '2024-03-18', 'Diabetes diagnosis', ['Shellfish', 'Pollen']],
    [3, 'Bob Johnson', 60, 'Asthma', '1964-08-03', '2024-03-17', 'Asthma diagnosis', ['Peanuts', 'Cats']],
    [31, 'Grayson Wright', 63, 'Arthritis', '1961-06-25', '2024-02-05', 'Arthritis diagnosis', ['Pollen', 'Wheat']],
    [50, 'Layla Flores', 60, 'Arthritis', '1964-12-28', '2024-01-05', 'Arthritis diagnosis', ['Shellfish', 'Dust']],
    [16, 'Oliver Martin', 29, 'Migraine', '1995-02-19', '2024-02-28', 'Migraine diagnosis', ['Peanuts', 'Shellfish']],
    [32, 'Luna Lopez', 34, 'Flu', '1990-02-14', '2024-02-04', 'Flu diagnosis', ['Shellfish', 'Milk']],
    [28, 'Jackson Young', 35, 'Bronchitis', '1989-11-11', '2024-02-10', 'Bronchitis diagnosis', ['Pollen', 'Soy']],
    [5, 'Michael Brown', 52, 'Bronchitis', '1972-04-25', '2024-03-14', 'Bronchitis diagnosis', ['Pollen', 'Eggs']],
    [37, 'Henry Baker', 37, 'Bronchitis', '1987-08-06', '2024-01-27', 'Bronchitis diagnosis', ['Peanuts', 'Milk']],
    [19, 'Mia Martinez', 31, 'Anemia', '1993-12-29', '2024-02-24', 'Anemia diagnosis', ['Penicillin', 'Wheat']],
    [43, 'Audrey Cooper', 49, 'Diabetes', '1975-09-03', '2024-01-16', 'Diabetes diagnosis', ['Pollen', 'Milk']],
    [49, 'Xavier Foster', 41, 'Migraine', '1983-05-16', '2024-01-06', 'Migraine diagnosis', ['Pollen', 'Soy']],
    [26, 'Avery Hall', 48, 'Hypertension', '1976-12-03', '2024-02-14', 'High blood pressure diagnosis', ['Peanuts', 'Dust']],
    [41, 'Grace Murphy', 65, 'Arthritis', '1959-05-07', '2024-01-20', 'Arthritis diagnosis', ['Peanuts', 'Wheat']],
    [45, 'Savannah Bailey', 47, 'Hypertension', '1977-03-09', '2024-01-13', 'High blood pressure diagnosis', ['Peanuts', 'Soy']],
    [39, 'Zoe Turner', 26, 'Eczema', '1998-03-11', '2024-01-23', 'Eczema diagnosis', ['Peanuts', 'Milk']],
    [18, 'Elijah Garcia', 55, 'Hypertension', '1969-10-07', '2024-02-25', 'High blood pressure diagnosis', ['Pollen', 'Soy']]
]

app = HospitalRecord(patient_records)

# app.radix_sort_Patient_age()
app.radix_sort_string(1)
app.print_record()
