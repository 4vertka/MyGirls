import os

image_folder = "./walls"
readme_file = "README.md"

with open(readme_file, 'a') as f:
    f.write("\n# Wallpaper Gallery\n\n")

    row_images = []

    for image_name in os.listdir(image_folder):
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp', '.tiff')):
            image_path = os.path.join(image_folder, image_name)

            # Directly use the image file path for the markdown image link
            row_images.append(f"![{image_name}]({image_path})")

            if len(row_images) == 5:  
                f.write("  ".join(row_images) + "\n\n")
                row_images = []

    if row_images:  
        f.write("  ".join(row_images) + "\n\n")

print("README.md updated with images.")

