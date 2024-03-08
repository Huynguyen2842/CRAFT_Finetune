import os

def convert_ic13_to_ic15(ic13_data):
    ic15_lines = []

    for line in ic13_data:
        values = line.split(', ')
        x1, y1, x2, y2, text = map(str.strip, values)

        # Remove double quotes around the text if present
        text = text.replace('"', '')

        # Add "###" if the text is empty
        if not text:
            text = "###"

        ic15_line = f"{x1},{y1},{x2},{y1},{x2},{y2},{x1},{y2},{text}"
        ic15_lines.append(ic15_line)

    return ic15_lines


def save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(data))


def process_ic13_file(ic13_filename):
    with open(ic13_filename, 'r') as file:
        ic13_data = file.read().splitlines()

    ic15_data = convert_ic13_to_ic15(ic13_data)
    ic15_filename = f"gt_modified/{os.path.basename(ic13_filename)}"
    save_to_file(ic15_data, ic15_filename)
    print(f"Conversion completed. IC15 data saved to {ic15_filename}")


if __name__ == "__main__":
    ic13_folder = "dataset\ICDAR2013\gt"

    # Create a folder for the modified IC15 files
    os.makedirs("gt_modified", exist_ok=True)

    for ic13_filename in os.listdir(ic13_folder):
        if ic13_filename.endswith(".txt"):
            ic13_filepath = os.path.join(ic13_folder, ic13_filename)
            process_ic13_file(ic13_filepath)
