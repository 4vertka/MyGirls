import os

image_dir = './walls'

image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
image_files = [f for f in os.listdir(image_dir) if any(f.lower().endswith(ext) for ext in image_extensions)]

image_files.sort()

readme_path = 'README.md'

with open(readme_path, 'a') as md_file:
    md_file.write('\n## Wallpapers\n\n')  
    
    md_file.write('| Column 1 | Column 2 | Column 3 | Column 4 |\n')
    md_file.write('|----------|----------|----------|----------|\n')

    for i in range(0, len(image_files), 4):
        row_images = image_files[i:i + 4]
        row = ' | '.join([f'![{img}]({os.path.join(image_dir, img)})' for img in row_images])
        md_file.write(f'| {row} |\n')

print(f"Markdown table has been appended to '{readme_path}'.")

