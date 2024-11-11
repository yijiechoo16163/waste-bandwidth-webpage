import requests
import os
import time
from tqdm import tqdm

# Define colors for the tags only
INFO_COLOR = "\033[92m"  # Green text for INFO and DONE
WARN_COLOR = "\033[91m"  # Red text for WARN
END_COLOR = "\033[0m"    # Reset color to white

url = "https://waste-bandwidth-webpage.pages.dev/v2/testfile20.bin"
file_name = "testfile20.bin"

# Start overall timer
start_script_time = time.time()

# Loop 10 times
for i in range(10):
    iteration_start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{iteration_start_time}] {INFO_COLOR}INFO{END_COLOR} Iteration {i + 1} started")

    # Step 1: Download the file with progress bar
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        start_time = time.time()

        with open(file_name, "wb") as file:
            with tqdm(total=total_size, unit="B", unit_scale=True, desc=f"Downloading {file_name}", dynamic_ncols=True, leave=False) as pbar:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
                    pbar.update(len(chunk))

        # Calculate download time and speed
        download_time = time.time() - start_time
        download_speed_mbps = (total_size * 8 / download_time) / 1_000_000
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {INFO_COLOR}INFO{END_COLOR} File downloaded successfully as {file_name}, speed: {download_speed_mbps:.2f} Mbps")

        # Step 2: Delete the file after testing
        os.remove(file_name)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {INFO_COLOR}INFO{END_COLOR} Iteration {i + 1} done.\n")
    else:
        # Print error and break the loop
        error_msg = f"Failed to download file. Status code: {response.status_code}"
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {WARN_COLOR}WARN{END_COLOR} {error_msg}")
        break

# Final output with execution time and average speed
total_time = time.time() - start_script_time
average_speed_mbps = (total_size * 8 * 10 / total_time) / 1_000_000
print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {INFO_COLOR}DONE{END_COLOR} The script ran successfully in {total_time:.2f} seconds. Average download speed: {average_speed_mbps:.2f} Mbps.")
