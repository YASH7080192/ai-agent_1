import os
import qrcode


def execute(arguments: dict):

    text = arguments.get("text")

    if not text:
        return {
            "status": "error",
            "message": "No text provided."
        }

    try:

        os.makedirs("generated_qr", exist_ok=True)

        file_path = "generated_qr/qrcode.png"

        img = qrcode.make(text)
        img.save(file_path)

        return {
            "status": "success",
            "message": "QR Code generated successfully.",
            "path": file_path
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


if __name__ == "__main__":

    result = execute(
        {
            "text": "https://google.com"
        }
    )

    print(result)