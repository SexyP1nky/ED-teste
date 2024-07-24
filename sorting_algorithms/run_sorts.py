import os
import selection_sort
import insertion_sort

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def write_output_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write('\n'.join(map(str, data)))

def main():
    input_directory = "input_files"
    output_directory = "output_files"
    os.makedirs(output_directory, exist_ok=True)

    for file_name in os.listdir(input_directory):
        if file_name.endswith('.in'):
            input_path = os.path.join(input_directory, file_name)

            input_data = read_input_file(input_path)
            
            # Selection Sort
            sorted_data_selection, time_taken_selection = selection_sort.selection_sort(input_data.copy())
            output_path_selection = os.path.join(output_directory, f"{file_name}_selection.out")
            write_output_file(output_path_selection, sorted_data_selection)
            
            # Insertion Sort
            sorted_data_insertion, time_taken_insertion = insertion_sort.insertion_sort(input_data.copy())
            output_path_insertion = os.path.join(output_directory, f"{file_name}_insertion.out")
            write_output_file(output_path_insertion, sorted_data_insertion)

            print(f"File: {file_name}")
            print(f"Selection Sort Tempo: {time_taken_selection:.6f} segundos")
            print(f"Insertion Sort Tempo: {time_taken_insertion:.6f} segundos")
            print("-" * 40)

if __name__ == "__main__":
    main()
