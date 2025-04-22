import requests

IMGBB_API_KEY = "8d9806701a011b5ffc5e83e25835d12e"

def upload_image_to_imgbb(image_path):
    url = f"https://api.imgbb.com/1/upload?key={IMGBB_API_KEY}"

    with open(image_path, "rb") as file:
        files = {
            "image": file
        }
        response = requests.post(url, files=files)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["url"]
    else:
        print("Upload failed:", response.status_code)
        print("Response:", response.text)
        return None

# Test it
image_url = upload_image_to_imgbb("fake-thumb.jpg")
print("Uploaded image URL:", image_url)