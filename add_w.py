import os
from PIL import Image

image_folder = "./walls"  
readme_file = "README.md"
thumb_size = (150, 150)  

with open(readme_file, 'a') as f:
    f.write("\n# Wallpaper Gallery\n\n")
    
    row_images = []
    
    for image_name in os.listdir(image_folder):
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp', '.tiff')):
            image_path = os.path.join(image_folder, image_name)
            
            try:
                with Image.open(image_path) as img:
                    img.thumbnail(thumb_size)  
                    
                    thumb_folder = os.path.join(image_folder, 'thumbs')
                    os.makedirs(thumb_folder, exist_ok=True)
                    thumb_path = os.path.join(thumb_folder, image_name)
                    img.save(thumb_path)

                row_images.append(f"![{image_name}]({thumb_path})")

            except Exception as e:
                print(f"Warning: Could not process image {image_name}. Error: {e}")
                continue  

            if len(row_images) == 5:
                f.write("  ".join(row_images) + "\n\n")
                row_images = []

    if row_images:
        f.write(" | ".join(row_images) + "\n\n")

print("README.md updated with images.")

