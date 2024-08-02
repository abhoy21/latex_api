
# Latex Compiler Api

A LaTeX compilation service using Flask and Docker. This service allows you to upload a LaTeX source file (`.tex`) and returns the compiled PDF file. The compilation is handled inside a Docker container, ensuring a consistent LaTeX environment.


## Features

- Accepts a single LaTeX source file as input.
- Compiles the LaTeX file into a PDF using `latexmk`.
- Runs the compilation in a Docker container for consistency and isolation.
- Provides an easy-to-use API with Flask.


## Prerequisites

- [Docker](https://www.docker.com/get-started) installed and running on your machine.
- [Python 3.6+](https://www.python.org/downloads/) installed.


### Basic Knowledge of LaTeX

To effectively use this service, you should have a basic understanding of LaTeX, including:

- **LaTeX Document Structure:** Understanding the basic structure of a LaTeX document, including commands such as `\documentclass`, `\begin{document}`, `\end{document}`, `\title`, `\author`, and `\date`.
- **Common Packages:** Familiarity with commonly used LaTeX packages such as `graphicx` for including images, `amsmath` for mathematical formatting, and `geometry` for page layout adjustments.
- **Basic Formatting Commands:** Knowledge of fundamental LaTeX commands for formatting text (e.g., `\section`, `\subsection`, `\textbf`, `\textit`).
- **Document Compilation:** Understanding that LaTeX files are compiled into PDFs and recognizing that LaTeX source files end with the `.tex` extension.


For example, a basic LaTeX document might look like this:

```tex
\documentclass{article}
\usepackage{graphicx}
\begin{document}
\title{Sample Document}
\author{Author Name}
\date{\today}
\maketitle
\section{Introduction}
This is a sample LaTeX document.
\end{document}
```


## Installation

### Step 1: Build the Docker Image

You need to build the Docker image for the LaTeX compiler service. Follow these steps:

1. **Navigate to the Directory:**
   Open a terminal and navigate to the directory containing the `Dockerfile`. For example:
   ```bash
   cd /path/to/your/project
   ```

Build the Docker Image:
Run the following command to build the Docker image. Replace latex_api with your desired image name:

```bash
docker build -t latexapi .
```

This command reads the Dockerfile in the current directory and creates an image named latex_api. The . signifies that the Docker build context is the current directory.

### Step 2: Run the Docker Container
Once the Docker image is built, you need to run a Docker container from it. Use the following command:

```bash
docker run -d -p 5000:5000 my_latex_compiler
```
-d: Runs the container in detached mode (in the background). 

-p 5000:5000: Maps port 5000 on your host machine to port 5000 in the Docker container.
my_latex_compiler: The name of the Docker image to run.

This command starts the Flask server inside the Docker container, making it accessible at http://localhost:5000.


## API Endpoint

### `/compile` (POST)

This endpoint accepts a LaTeX source file (`.tex`) and returns the compiled PDF file.

- **URL:** `http://localhost:5000/compile`
- **Method:** `POST`
- **Content-Type:** `multipart/form-data`
- **Parameters:**
  - `file`: The LaTeX source file (`.tex`).

### Testing the Endpoint

#### Using Postman

1. **Open Postman:**
   Launch the [Postman](https://www.postman.com/) application on your computer.

2. **Create a New Request:**
   Click on the `+` button to open a new tab for a request.

3. **Set Up the Request:**
   - Set the request method to `POST`.
   - Enter the URL `http://localhost:5000/compile` in the URL field.

4. **Configure the Request Body:**
   - Go to the `Body` tab.
   - Select `form-data`.
   - In the `Key` column, enter `file`.
   - In the `Value` column, click `Choose Files` and select your `.tex` file.

5. **Send the Request:**
   - Click the `Send` button.
   - Postman will upload the file and you should receive a PDF file as a response.

6. **Save or View the Response:**
   - You can view the PDF directly in Postman or save it by clicking the `Save Response` button.

#### Using `curl`

1. **Open a Terminal:**
   Open a command-line terminal on your computer.

2. **Run the `curl` Command:**
   Use the following command to upload a `.tex` file and receive the compiled PDF:

   ```bash
   curl -F "file=@path/to/your/document.tex" http://localhost:5000/compile --output compiled_document.pdf
________________________________________________________________________________________________________________________
