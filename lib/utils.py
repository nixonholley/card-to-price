import base64

def local_image_to_b64(image_path : str) -> base64:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        encoded_image_bytes = base64.b64encode(image_data)
        return encoded_image_bytes