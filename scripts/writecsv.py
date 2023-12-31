import csv

def write_csv(file_name, data):
    try:
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)
        print(f"Data written to '{file_name}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
csv_file_name = 'output.csv'
data_to_write = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Alice', 30, 'San Francisco'],
    ['Bob', 22, 'Los Angeles']
]
write_csv(csv_file_name, data_to_write)
