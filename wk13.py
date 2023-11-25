import os

def generate_file_info():
    file_list = []
    
    # Get the list of files in the current working directory
    files = os.listdir(os.getcwd())

    for file in files:
        file_path = os.path.join(os.getcwd(), file)
        
        # Check if the item is a file
        if os.path.isfile(file_path):
            # Get file information
            file_info = {
                'name': file,
                'size': os.path.getsize(file_path)  # in bytes
            }
            
            file_list.append(file_info)

    return file_list

# Generate file information
file_info_list = generate_file_info()

# Print the list of dictionaries
for file_info in file_info_list:
    print(file_info)
