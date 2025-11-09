from baml_py import Image
from baml_lib.baml_client import b
from dotenv import load_dotenv

# LLM API Keys are located in the .env file
load_dotenv('../.env')


async def extract_yugioh_card_from_url(url: str):
    """
    Extracts an image of a receipt stored at a URL.

    Args:
        url (str): The URL of the receipt image.

    Returns:
        dict: The receipt data. See the baml_src/recipt_model.baml file for the structure of the receipt data.
    """
    img = Image.from_url(url)
    output = b.ExtractYugiohCardFromImage(img)
    return output


async def extract_yugioh_card_from_base64(base64: str):
    """Extract a receipt from a base 64 image file.

    Args:
        base64 (str): Base64 string encoded image

    Returns:
        dict: The receipt data. See the baml_src/recipt_model.baml file for the structure of the receipt data.
    """

    img_64 = Image.from_base64("image/png", base64)
    output = b.ExtractYugiohCardFromImage(img_64)
    return output