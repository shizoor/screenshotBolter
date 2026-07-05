import argparse
import sys
import mss
import time, datetime
from PIL import Image

outputdirectory = "Z:\\outlier\\screenshots"   #Feel free to change this as needed

def capture_and_combine(monitor_numbers):
    with mss.MSS() as sct:
        # sct.monitors[0] is the whole virtual screen, 1+ are individual screens
        available_monitors = len(sct.monitors) - 1

        if available_monitors == 0:
            print("No monitors detected.")
            sys.exit(1)

        # Remove duplicates and validate monitor numbers
        valid_requested = []
        for num in set(monitor_numbers):
            if num < 1 or num > available_monitors:
                print(f"Warning: Monitor {num} does not exist (Available: 1-{available_monitors}). Skipping.")
            else:
                valid_requested.append(num)

        if not valid_requested:
            print("No valid monitors specified.")
            sys.exit(1)

        # Sort numbers so the lesser monitor number is handled first (left-to-right order)
        valid_requested.sort()

        captured_images = []

        # 1. Capture the individual screens
        for num in valid_requested:
            # Grab screenshot data using mss
            sct_img = sct.grab(sct.monitors[num])

            # Convert mss format directly to a Pillow Image
            pil_img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

            # Save individual screen
            # Save the image to disk
            now = datetime.datetime.now()
            res = str(now.timestamp() * 1000)
            output_name = outputdirectory + f"monitor_{num}_{res}.png"
            pil_img.save(output_name)
            print(f"Successfully saved {output_name}")

            # Store the pillow object for stitching
            captured_images.append(pil_img)

        # 2. Stitch images if multiple valid monitors were captured
        if len(captured_images) >= 2:
            # Calculate total width and the maximum height among the screens
            total_width = sum(img.width for img in captured_images)
            max_height = max(img.height for img in captured_images)

            # Create a blank, transparent canvas large enough to hold all images
            combined_img = Image.new("RGBA", (total_width, max_height))

            # Paste images side by side
            x_offset = 0
            for img in captured_images:
                combined_img.paste(img, (x_offset, 0))
                x_offset += img.width

            # Save the stitched result
                # Save the image to disk
            now = datetime.datetime.now()
            res = str(now.timestamp() * 1000)
            combined_name = outputdirectory + f"combined_monitors_{res}.png"
            combined_img.save(combined_name)
            print(f"Successfully saved combined image as {combined_name}")


if __name__ == "__main__":
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(
        description="Capture specific monitors using mss."
    )
    parser.add_argument(
        "monitors",
        metavar="N",
        type=int,
        nargs="+",
        help="One or more monitor numbers to capture (e.g., 1 2)",
    )

    args = parser.parse_args()
    capture_and_combine(args.monitors)
