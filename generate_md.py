import os

def generate_readme(project_directory, readme_file):
    with open(readme_file, 'w') as readme:
        for root, dirs, files in os.walk(project_directory):
            # Add a page break for each folder
            if root != project_directory:
                folder_name = os.path.relpath(root, project_directory)
                readme.write(f"\n# {folder_name}\n\n")

            for file in files:
                if file.endswith((".py", ".c", ".cpp", ".h", ".hpp")):
                    file_path = os.path.join(root, file)

                    # Add a header with file name
                    readme.write(f"## {file}\n\n")
                    
                    # Read the content of the file and write it to the README
                    with open(file_path, 'r') as code_file:
                        code_content = code_file.read()
                        readme.write(f"```{file.split('.')[-1]}\n{code_content}\n```\n")

if __name__ == "__main__":
    project_directory = input("Enter the path to your code project: ")
    readme_filename = input("enter the filename of the markdown file: ")  # Output README file name

    generate_readme(project_directory, readme_filename)
    print(f"README generated successfully: {readme_filename}")

