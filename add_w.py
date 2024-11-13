import os

image_folder = "./walls"
readme_file = "README.md"

with open(readme_file, 'a') as f:
    f.write("\n# Wallpaper Gallery\n\n")

    row_images = []

    for image_name in os.listdir(image_folder):
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp', '.tiff')):
            image_path = os.path.join(image_folder, image_name)

            # Add image as Markdown image link to the list
            row_images.append(f"![{image_name}]({image_path})")

            # After 5 images, write them to the README and reset the list
            if len(row_images) == 5:
                f.write("  ".join(row_images) + "\n\n")
                row_images = []

    # If there are any remaining images that didn't fill a full row
    if row_images:
        f.write("  ".join(row_images) + "\n\n")

print("README.md updated with images.")

