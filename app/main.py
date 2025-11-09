from baml_py import Image
import base64
from dotenv import load_dotenv
load_dotenv('../.env')

def local_image_to_b64(image_path : str) -> base64:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        encoded_image_bytes = base64.b64encode(image_data)
        return encoded_image_bytes

def main():
    pass


if __name__ == "__main__":
    main()
