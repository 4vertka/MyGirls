import os

image_folder = "./walls"
readme_file = "README.md"

with open(readme_file, 'a') as f:
    f.write("\n# Wallpaper Gallery\n\n")
    
    # Start the table for the image grid
    f.write("<table>\n")

    row_images = []

    for image_name in os.listdir(image_folder):
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp', '.tiff')):
            image_path = os.path.join(image_folder, image_name)

            # Add the image as an HTML <img> tag in a table cell <td>
            row_images.append(f"<td><img src='{image_path}' alt='{image_name}' width='150' height='150'></td>")

            # After 5 images, close the row and start a new one
            if len(row_images) == 5:
                f.write("<tr>\n" + "\n".join(row_images) + "\n</tr>\n")
                row_images = []  # Reset for the next row

    # If there are any remaining images that didn't fill a full row
    if row_images:
        f.write("<tr>\n" + "\n".join(row_images) + "\n</tr>\n")

    # Close the table
    f.write("</table>\n")

print("README.md updated with images in a grid layout.")

