from flask import Flask, render_template, request, send_file, send_from_directory, url_for
import os
from removebackground import remove_bg

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/remove-bg", methods=["POST"])
def remove_background():
    file = request.files.get("image")
    if not file:
        return "No file uploaded!", 400

    # Save uploaded image
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    # Output file path inside static folder
    output_filename = "bg_removed_" + file.filename
    output_path = os.path.join(STATIC_FOLDER, output_filename)

    # Process image
    remove_bg(input_path, output_path)

    return render_template("result.html", output_image=output_filename)


@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(STATIC_FOLDER, filename, as_attachment=True)


if __name__ == "__main__":
    app.run()
