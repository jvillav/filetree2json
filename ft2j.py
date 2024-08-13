# File tree to JSON

import argparse
import os
import json

def directory_to_json(path, verbose):
    result = {}
    print(f"Processing: {path}")

    for root, dirs, files in os.walk(path):
        # Get the relative path to ensure the JSON object doesn't contain full paths
        relative_path = os.path.relpath(root, path)
        # Create a reference to the current level in the JSON hierarchy
        current_level = result
 
        # Navigate to the correct level in the hierarchy
        if relative_path != '.':
            for part in relative_path.split(os.sep):
                current_level = current_level.setdefault(part, {})

        # Add directories
        for dir_name in dirs:
            current_level[dir_name] = {}

        # Add files and their contents
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    if verbose:
                        print(f"Processing: {file_path}")
            except Exception as e:
                file_content = "Unable to parse file"
                print(f"Unable to process {file_path}\nERROR:{str(e)}")

            current_level[file_name] = file_content

    return result

def recreate_structure_from_json(json_data, root_path):
    for name, content in json_data.items():
        current_path = os.path.join(root_path, name)

        if isinstance(content, dict):
            # It's a directory
            os.makedirs(current_path, exist_ok=True)
            recreate_structure_from_json(content, current_path)
        else:
            # It's a file
            try:
                with open(current_path, 'w', encoding='utf-8') as file:
                    file.write(content)
            except Exception as e:
                print(f"Unable to recreate {current_path} due to: {str(e)}")

def main():

    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Convert a directory structure and its contents into a JSON object, or recreate the directory structure and its contents from a JSON file.")
    parser.add_argument("-d","--directory", default="./", help="The path of the directory to convert.")
    parser.add_argument("-o", "--output", default="output.json", help="The path of the output JSON file. Defaults to 'output.json'.")

    parser.add_argument("-i", "--json_file", default="", help="The path of the JSON file containing the directory structure.")
    parser.add_argument("-p", "--output_directory", default="./", help="The root directory where the structure will be recreated.")
    parser.add_argument("-v", "--verbose", default="False", help="Enable a verbose output.")
    args = parser.parse_args()
    
    # Create
    if args.json_file == "":
        directory_structure = directory_to_json(args.directory, args.verbose)
        output_file_path = args.output      
        # Convert the dictionary to a JSON string
        json_output = json.dumps(directory_structure, indent=4)

        # If you want to save it to a file
        with open(output_file_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json_output)


        print(f"Directory structure and contents have been saved to {output_file_path}")

    # Reconstruct
    else:
        root_path = args.output_directory
        # Load the JSON data
        with open(args.json_file, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            recreate_structure_from_json(json_data, root_path)
        





if __name__ == "__main__":
    main()





