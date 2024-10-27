import glob
import os
import zipfile
from shutil import rmtree

from jinja2 import Template

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/index.html") as index_file:
    index_template = Template(index_file.read())


def create_empty_output_folder():
    output_path = f"{script_dir}/../out"
    if os.path.exists(output_path):
        rmtree(output_path)
    os.makedirs(output_path)


def extract_images():
    zipped_file = f"{script_dir}/images.zip"
    to_directory = f"{script_dir}/../out"

    with zipfile.ZipFile(zipped_file, "r") as zip_ref:
        zip_ref.extractall(to_directory)


def generate_index():
    all_images = map(lambda f: os.path.basename(f), glob.glob("out/images/*"))
    filename = os.path.join(script_dir, "../out", "index.html")
    file = open(filename, "w")
    file.write(index_template.render(images=all_images))


if __name__ == "__main__":
    print("Start generating the files for pages")

    create_empty_output_folder()
    extract_images()
    generate_index()

    print("Finish generating the files")
