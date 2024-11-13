import os

# Set the directory where your images are stored
image_dir = './walls'

# Get a list of all image files in the directory (assuming common image extensions)
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
image_files = [f for f in os.listdir(image_dir) if any(f.lower().endswith(ext) for ext in image_extensions)]

# Sort the files to ensure consistency (optional)
image_files.sort()

# Path to your existing README.md file
readme_path = 'README.md'

# Open the existing README.md file in append mode
with open(readme_path, 'a') as md_file:
    # Write a section header before the table (optional)
    md_file.write('\n## Wallpapers\n\n')  # You can change this to whatever heading you'd like
    
    # Write the table header
    md_file.write('| Column 1 | Column 2 | Column 3 | Column 4 |\n')
    md_file.write('|----------|----------|----------|----------|\n')

    # Group images into sets of four for each row
    for i in range(0, len(image_files), 4):
        row_images = image_files[i:i + 4]
        # For each image in the row, create a markdown image tag
        row = ' | '.join([f'![{img}]({os.path.join(image_dir, img)})' for img in row_images])
        md_file.write(f'| {row} |\n')

print(f"Markdown table has been appended to '{readme_path}'.")

