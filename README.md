# jsix-image-format
JSIX: A custom experimental image file format that stores pixel data in hexadecimal.

I saw a video of someone creating their own image file format, so I decided to do the same with Python.

# Reasons to use the JSIX image format
- Your image files will be insanely large... (a 180 KB PNG can easily get up to 230 MB in JSIX...)
- You won't be able to view your images with any image viewer other than the one provided in this repo.

### Conclusion:
Maybe don't use it... 

I might add compression and other optimizations to make it smaller in the future.

# Installation
### Step 1: Clone the GitHub Repository
1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Use the following command to clone the repository:
```bash
git clone https://github.com/johannesschiessl/jsix-image-format.git
```
### Step 2: Navigate to the Project Directory
After cloning, navigate into the project's directory:
```bash
cd jsix-image-format
```
### Step 3: Install Dependencies
To install the dependencies, run the following command:
```bash
pip install -r requirements.txt
```

# How to use it
## Convert PNG to JSIX
### Step 1: Navigate into the jsix directory:
```bash
cd jsix
```
### Step 2: Run the convert function
```bash
python convert_png_to_jsix.py <input-file-name/path>.png <output-file-name/path>.jsix
```
### 3. Be patient, this may take a while...

## View a JSIX file
### Step 1: Navigate into the jsix directory:
```bash
cd jsix
```
### Step 2: Run the convert function
```bash
python display_jsix.py <filename/path>.jsix
```
### 3. Be patient, this may take a while...
