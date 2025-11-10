import base64
import requests
from typing import Optional, Dict, Any, List

def local_image_to_b64(image_path : str) -> base64:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        encoded_image_bytes = base64.b64encode(image_data)
        return encoded_image_bytes


def build_rest_headers(api_key: str) -> Dict[str, str]:
    """
    Build the required REST headers for the JustTCG API.
    The API requires only one header: X-API-Key.
    """
    return {
        "X-API-Key": api_key,
        "Content-Type": "application/json"
    }


def submit_api_request(
    api_key: str,
    url: str,
    method: str = "GET",
    params: Optional[Dict[str, Any]] = None,
    body: Optional[Any] = None,
    timeout: int = 20,
) -> Dict[str, Any]:
    """
    Make a typed, generic request to the JustTCG API.
    
    - Supports GET and POST
    - Handles errors with rich detail
    - Automatically attaches headers
    - Returns JSON response or raises detailed exceptions
    """

    headers = build_rest_headers(api_key)

    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=timeout)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=body, timeout=timeout)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        data = response.json()

        # Handle API errors
        if not response.ok:
            error_msg = data.get("error") or "Unknown error"
            error_code = data.get("code")
            raise RuntimeError(
                f"API request failed ({response.status_code}): {error_msg} "
                f"(code={error_code})"
            )

        return data

    except requests.exceptions.Timeout:
        raise TimeoutError("Request to API timed out")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Network error: {str(e)}")

