import csv

def read_csv(file_name):
    data = []
    try:
        with open(file_name, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data

# Example usage:
csv_file_name = 'output.csv'
csv_data = read_csv(csv_file_name)
print(f"Contents of '{csv_file_name}':\n")
for row in csv_data:
    print(row)