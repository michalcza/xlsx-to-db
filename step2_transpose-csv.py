import csv
import os

# This script reads each CSV file in the folder, checks if the last column has a header and deletes it if it's empty, and then deletes all columns where the column header is greater than 2204. It saves the modified CSV file to a temporary file and then replaces the original file with the modified file and deletes the temporary file.
# This code should first remove the value 'READING' from the header if it is present, and then remove all columns where the column header value is greater than 2204.

folder_path = r'C:\Users\Michal\Documents\GitHub\xlsx-to-db'

for file_path in os.listdir(folder_path):
    if file_path.endswith('.csv'):
        # Construct the output file name by appending "_t" to the original file name
        output_file_name = os.path.splitext(file_path)[0] + '_t.csv'
        output_file_path = os.path.join(folder_path, output_file_name)

        with open(os.path.join(folder_path, file_path), 'r', encoding='utf-8') as input_file, \
                open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)

            # Transpose the rows and write to the output file
            for row in zip(*reader):
                writer.writerow(row)

        os.remove(os.path.join(folder_path, file_path))
        os.rename(output_file_path, os.path.join(folder_path, file_path[:-4] + '.csv'))
        print(f'Transposed {file_path} to {file_path[:-4]} and deleted {file_path}')
