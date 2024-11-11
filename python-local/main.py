import requests
import os

url = "https://waste-bandwidth-webpage.pages.dev/v2/testfile20.bin"
file_name = "testfile20.bin"

# Loop 10 times
for i in range(10):
    print(f"Iteration {i + 1}")

    # Step 1: Download the file
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded successfully as {file_name}")

        # Step 2: Perform any testing operations here
        file_size = os.path.getsize(file_name)
        print(f"File size: {file_size} bytes")

        # Step 3: Delete the file after testing
        os.remove(file_name)
        print(f"{file_name} has been deleted after testing.\n")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        break  # Optionally break the loop if download fails
