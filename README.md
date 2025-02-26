# OCR Project

This project provides a simple command-line tool to extract text from images using Optical Character Recognition (OCR) with Tesseract. It supports processing single image files or directories containing multiple images.

## Prerequisites

- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and added to your system's PATH
- Required Python packages: `Pillow`, `pytesseract`

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages using pip:
    ```sh
    pip install Pillow pytesseract
    ```

## Usage

The script can be run from the command line. Below are the available options:

```sh
python ocr.py [-h] [-o OUTPUT] [-l LANG] input
```

### Arguments

- `input`: Path to an image file or directory containing images.
- `-o OUTPUT`, `--output OUTPUT`: Path to save the extracted text (file or directory). If not provided, the extracted text will be printed to the console or saved in a directory named `ocr_results` within the input directory.
- `-l LANG`, `--lang LANG`: Language code for OCR (default: `eng` for English). See [Tesseract language data files](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html) for available language codes.

### Examples

1. Extract text from a single image and print to console:
    ```sh
    python ocr.py path/to/image.jpg
    ```

2. Extract text from a single image and save to a file:
    ```sh
    python ocr.py path/to/image.jpg -o path/to/output.txt
    ```

3. Extract text from all images in a directory and save to a directory:
    ```sh
    python ocr.py path/to/images -o path/to/output_directory
    ```

## Logging

The script uses Python's logging module to log information and errors. Logs are printed to the console with timestamps and log levels.

## Error Handling

If Tesseract OCR is not installed or not in the system's PATH, the script will print an error message and exit. Ensure Tesseract is installed and accessible before running the script.

## Future of the Project

### Recognizing Handwriting

One of the future goals of this project is to enhance its capabilities to recognize handwritten text. Handwriting recognition is more challenging than printed text due to the variability in individual writing styles. We plan to explore and integrate advanced machine learning models and techniques to improve the accuracy of handwriting recognition.

### Natural Language Processing (NLP)

In addition to extracting text, we aim to incorporate Natural Language Processing (NLP) packages to further process and analyze the extracted text. This could include features such as:

- Text summarization
- Named entity recognition (NER)
- Sentiment analysis
- Language translation

By leveraging NLP, we can provide more meaningful insights and applications for the extracted text, making the tool more versatile and powerful.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Pillow](https://python-pillow.org/)
- [pytesseract](https://github.com/madmaze/pytesseract)