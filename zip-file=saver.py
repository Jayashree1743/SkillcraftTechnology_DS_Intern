from google.colab import drive
import requests
from tqdm import tqdm
import zipfile
import os

# Step 1: Mount Google Drive
drive.mount('/content/drive')

# Step 2: Provide ZIP file URL and paths
url = "https://example.com/yourfile.zip"   # Replace with your ZIP link
zip_path = "/content/drive/MyDrive/yourfile.zip"
extract_path = "/content/drive/MyDrive/extracted_files"  # Folder for extracted files

# Step 3: Download with progress bar
response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))

with open(zip_path, "wb") as f, tqdm(
    desc="Downloading",
    total=total_size,
    unit="B",
    unit_scale=True,
    unit_divisor=1024,
) as bar:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
            bar.update(len(chunk))

print(f"✅ File downloaded to: {zip_path}")

# Step 4: Extract into Drive
os.makedirs(extract_path, exist_ok=True)
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_path)

print(f"📂 Files extracted to: {extract_path}")

# Step 5: Delete the ZIP file
os.remove(zip_path)
print(f"🗑️ Deleted ZIP file: {zip_path}")
