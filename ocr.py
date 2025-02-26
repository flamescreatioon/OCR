import argparse
import os
from PIL import Image
import pytesseract
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('ocr')

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Replace with your Tesseract path

def extract_text_from_image(image_path, lang='eng'):
    """
    Extract text from an image using OCR
    
    Args:
        image_path (str): Path to the image file
        lang (str): Language code for OCR (default: 'eng' for English)
                    See https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html
                    for a list of available language codes
    
    Returns:
        str: Extracted text
    """
    logger.info(f"Processing image: {image_path}")
    
    try:
        # Open the image
        image = Image.open(image_path)
        
        # Extract text using Tesseract
        text = pytesseract.image_to_string(image, lang=lang)
        
        return text
    except Exception as e:
        logger.error(f"Error processing {image_path}: {str(e)}")
        return None

def process_images(input_path, output_path=None, lang='eng'):
    """
    Process a single image or a directory of images
    
    Args:
        input_path (str): Path to an image file or directory containing images
        output_path (str, optional): Path to save the extracted text
        lang (str): Language code for OCR
    """
    if os.path.isfile(input_path):
        # Process a single file
        text = extract_text_from_image(input_path, lang)
        
        if text:
            if output_path:
                # Save the extracted text to a file
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                logger.info(f"Text saved to {output_path}")
            else:
                # Print the extracted text to the console
                print(f"\n--- Extracted Text from {os.path.basename(input_path)} ---\n")
                print(text)
        else:
            logger.error(f"Failed to extract text from {input_path}")
    
    elif os.path.isdir(input_path):
        # Process a directory of images
        if not output_path:
            output_path = os.path.join(input_path, "ocr_results")
            os.makedirs(output_path, exist_ok=True)
        else:
            os.makedirs(output_path, exist_ok=True)
        
        # Get list of image files (common formats)
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.gif']
        image_files = [f for f in os.listdir(input_path) if os.path.splitext(f.lower())[1] in image_extensions]
        
        logger.info(f"Found {len(image_files)} images in {input_path}")
        
        for img_file in image_files:
            img_path = os.path.join(input_path, img_file)
            file_name = os.path.splitext(img_file)[0]
            out_file = os.path.join(output_path, f"{file_name}.txt")
            
            text = extract_text_from_image(img_path, lang)
            
            if text:
                # Save the extracted text to a file
                with open(out_file, 'w', encoding='utf-8') as f:
                    f.write(text)
                logger.info(f"Extracted text from {img_file} saved to {out_file}")
            else:
                logger.error(f"Failed to extract text from {img_file}")
    
    else:
        logger.error(f"Invalid input path: {input_path}")
        print(f"Error: The path '{input_path}' does not exist or is not accessible.")

def main():
    parser = argparse.ArgumentParser(description='Extract text from images using OCR')
    parser.add_argument('input', help='Path to an image file or directory containing images')
    parser.add_argument('-o', '--output', help='Path to save the extracted text (file or directory)')
    parser.add_argument('-l', '--lang', default='eng', help='Language code for OCR (default: eng)')
    
    args = parser.parse_args()
    
    # Check if Tesseract is installed and accessible
    try:
        pytesseract.get_tesseract_version()
    except pytesseract.TesseractNotFoundError:
        logger.error("Tesseract OCR is not installed or not in PATH")
        print("Error: Tesseract OCR is not installed or not in your PATH.")
        print("Please install Tesseract OCR: https://github.com/tesseract-ocr/tesseract")
        return
    
    # Process the images
    process_images(args.input, args.output, args.lang)

if __name__ == "__main__":
    main()