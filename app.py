from flask import Flask, request, send_file, jsonify
import os
import subprocess
import tempfile

app = Flask(__name__)

@app.route('/compile', methods=['POST'])
def compile_tex():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    files = request.files.getlist('file')
    if not files or files[0].filename == '':
        return jsonify({'error': 'No selected file'}), 400

    tex_file = None
    temp_dir = tempfile.TemporaryDirectory()
    temp_path = temp_dir.name

    for file in files:
        file_path = os.path.join(temp_path, file.filename)
        file.save(file_path)
        if file.filename.endswith('.tex'):
            tex_file = file_path

    if not tex_file:
        return jsonify({'error': 'No .tex file provided'}), 400

    # Compile the LaTeX file using latexmk
    pdf_path = os.path.join(temp_path, 'document.pdf')
    log_path = os.path.join(temp_path, 'compile.log')

    compile_command = [
        'latexmk',
        '-pdf',
        '-output-directory=' + temp_path,
        '-interaction=nonstopmode',
        tex_file
    ]

    result = subprocess.run(compile_command, capture_output=True, text=True)
    if result.returncode != 0:
        # Log the error and return a message to the user
        with open(log_path, 'w') as log_file:
            log_file.write(result.stderr)
        return jsonify({'error': 'Error compiling LaTeX file', 'log': result.stderr}), 500

    # Send the compiled PDF file
    if not os.path.exists(pdf_path):
        return jsonify({'error': 'PDF file not found'}), 500

    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
