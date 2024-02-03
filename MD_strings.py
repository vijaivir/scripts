import os

def prepend_text_to_md_files(folder_path, text_to_prepend):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r+') as file:
                # Read the original content
                original_content = file.read()
                # Move the pointer to the beginning of the file
                file.seek(0, 0)
                # Write the new text followed by the original content
                file.write(text_to_prepend.rstrip('\r\n') + '\n\n' + original_content)

# The text to be prepended
text = ""

# Path to the folder containing .md files
folder_path = '.'

# Call the function
prepend_text_to_md_files(folder_path, text)
