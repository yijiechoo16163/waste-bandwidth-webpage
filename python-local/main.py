import requests
import os
import time
from tqdm import tqdm

url = "https://waste-bandwidth-webpage.pages.dev/v2/testfile20.bin"
file_name = "testfile20.bin"

# Loop 10 times with a progress bar
for i in tqdm(range(10), desc="Download-Test-Delete Progress"):
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{start_time}] Iteration {i + 1}")

    # Step 1: Download the file
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] File downloaded successfully as {file_name}")

        # Step 2: Perform any testing operations here
        file_size = os.path.getsize(file_name)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] File size: {file_size} bytes")

        # Step 3: Delete the file after testing
        os.remove(file_name)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {file_name} has been deleted after testing.\n")
    else:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failed to download file. Status code: {response.status_code}")
        break  # Optionally break the loop if download fails
