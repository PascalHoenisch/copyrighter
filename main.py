from PIL import Image
import os
import sys
from pathlib import Path


def remove_transparent_padding(watermark):
    """
    Removes extra transparent margins around the watermark image.
    Returns a cropped, tighter watermark.
    """
    # Get the bounding box of the non-transparent areas
    bbox = watermark.getbbox()
    if bbox:
        return watermark.crop(bbox)
    return watermark


def add_copyright(image_path, watermark_path, output_dir):
    """Add a PNG watermark to an image and save it to the output directory."""
    try:
        # Open the input image
        with Image.open(image_path) as img:
            # Convert to RGBA to handle transparency
            img = img.convert('RGBA')

            # Open the watermark image
            with Image.open(watermark_path) as watermark:
                # Remove any transparent borders from the watermark
                watermark = watermark.convert('RGBA')  # Ensure it is in RGBA mode
                watermark = remove_transparent_padding(watermark)

                # Resize the watermark to fit the image proportionally (e.g., 20% of the image width)
                scale_factor = 0.2  # Percentage of the image width
                watermark_width = int(img.width * scale_factor)
                watermark_height = int(watermark.height * watermark_width / watermark.width)
                watermark = watermark.resize((watermark_width, watermark_height))

                # Define padding to move the watermark slightly out of the corner
                padding_x = 60  # Horizontal distance from the right edge
                padding_y = 50  # Vertical distance from the bottom edge

                # Calculate the position with the given padding
                position = (
                    img.width - watermark_width - padding_x,
                    img.height - watermark_height - padding_y
                )

                # Create a new image by combining the original image and the watermark
                combined = Image.alpha_composite(img, Image.new("RGBA", img.size, (0, 0, 0, 0)))
                combined.paste(watermark, position, watermark)

            # Prepare output path
            output_path = Path(output_dir) / f"{Path(image_path).stem}_watermarked.png"

            # Save the combined image
            combined.save(output_path, "PNG")
            print(f"Processed: {output_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")


def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <watermark_path> <input_path> <output_directory>")
        sys.exit(1)

    watermark_path = sys.argv[1]
    input_path = sys.argv[2]
    output_dir = sys.argv[3]

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Check if input is a file or directory
    if os.path.isfile(input_path):
        if input_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            add_copyright(input_path, watermark_path, output_dir)
    else:
        # Process all images in the directory
        for filename in os.listdir(input_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(input_path, filename)
                add_copyright(file_path, watermark_path, output_dir)


if __name__ == "__main__":
    main()