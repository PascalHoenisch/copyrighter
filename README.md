# Copyrighter

Python tooling for adding a watermark to images.

## Installation

To set up the project, follow these steps:

### Install UV (Package Management Tool)

**Windows** (PowerShell):

```powershell 
(Invoke-WebRequest -Uri "[https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1)" -UseBasicParsing).Content | python -
``` 

*Make sure to close and reopen PowerShell after installation.*

**Linux / macOS**:

```bash 
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
``` 

### Project Setup

1. Clone the repository:

```bash 
git clone git@github.com:PascalHoenisch/copyrighter.git cd copyrighter
``` 

2. Set up a virtual environment and install dependencies:

```bash
# Create and activate a virtual environment
uv venv
``` 

---

## Command Line Usage

The script processes images by adding a PNG watermark to their bottom-right corner with a small padding. It requires
three arguments:

1. **Path to the watermark image** (e.g., a logo in PNG format).
2. **Input path** (can be a single image or a directory of images).
3. **Output directory** (all processed images will be saved here).

### Examples

**To process a single image:**

```bash 
python main.py path/to/watermark.png path/to/image.png output/folder
``` 

**To process an entire directory of images:**

```bash 
python main.py path/to/watermark.png path/to/images output/folder
``` 

---

## Technical Details

### How It Works:

1. **Transparent Padding Removal**:  
   The script removes extra transparent margins from the watermark PNG to allow for precise placement.
2. **Watermark Scaling**:  
   The watermark is resized to approximately **20% of the image width** to maintain proportionality regardless of the
   original image size.
3. **Watermark Position**:  
   The watermark is placed slightly out of the bottom-right corner with a default padding of:
    - `60 pixels` horizontally.
    - `50 pixels` vertically.
4. **Output**:  
   All processed images retain their original dimensions and are saved as PNG files.

---

### Supported Formats:

- **Input Image Formats**: PNG (`.png`), JPEG (`.jpg`, `.jpeg`).
- **Output Format**: All processed images are saved as PNG.
- **Naming Convention**: Each processed image is saved with the same name as the input file, suffixed with
  `_watermarked` (e.g., `image_watermarked.png`).

---

### Customization:

To adjust the placement of the watermark relative to the edges:

- **Horizontal Padding (`padding_x`)**: By default, 60 pixels from the right edge.
- **Vertical Padding (`padding_y`)**: By default, 50 pixels from the bottom edge.

You can modify these padding values in the logic for further customization.

---

## Example Output

For an input image `photo.jpg`, a successfully processed file will have the name `photo_watermarked.png` in the
specified output folder.

---

## License

This project is open-source and distributed under the **MIT License**.
