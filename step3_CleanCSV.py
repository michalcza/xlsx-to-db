import csv
import os

folder_path = r'C:\Users\Michal\Documents\loading'

for file_path in os.listdir(folder_path):
    if file_path.endswith('.csv'):
        # Construct the output file name by appending "_cleaned" to the original file name
        output_file_name = os.path.splitext(file_path)[0] + '_cleaned.csv'
        output_file_path = os.path.join(folder_path, output_file_name)

        with open(os.path.join(folder_path, file_path), 'r', encoding='utf-8') as input_file, \
                open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)

            # Process the header row
            header = next(reader)
            header = [h.replace('READING', '').strip() for h in header if h.strip() != '']
            header_int = [int(h) for h in header[1:] if h != '']

            # Filter the rows and write to the output file
            writer.writerow([header[0]] + [str(h) for h in header_int])
            for row in reader:
                filtered_row = [value for index, value in enumerate(row) if index == 0 or (index - 1) < len(header_int) and int(header_int[index-1]) <= 2204]
                writer.writerow(filtered_row)

        os.remove(os.path.join(folder_path, file_path))
        os.rename(output_file_path, os.path.join(folder_path, file_path))
        print(f'Cleaned {file_path} and deleted {file_path}')
