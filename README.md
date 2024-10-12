
### Instructions to Run the Python Script

1. **Install Python**: Make sure you have Python installed. You can check by opening the Terminal (found in Applications > Utilities) and typing:

   ```bash
   python3 --version
   ```

   If you don’t have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

2. **Open Terminal**: Find and open the Terminal application.

3. **Navigate to the Script Directory**: Use the `cd` command to change the directory to where your Python script and `requirements.txt` are located. For example:

   ```bash
   cd /path/to/your/script
   ```

   Replace `/path/to/your/script` with the actual path.

4. **Create a Virtual Environment (Optional but Recommended)**: This helps manage dependencies. Run the following command:

   ```bash
   python3 -m venv myenv
   ```

   Then activate the virtual environment with:

   ```bash
   source myenv/bin/activate
   ```

5. **Install Required Packages**: Now, install the required packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Script**: Finally, run your Python script by typing:

   ```bash
   python3 your_script.py
   ```

   Replace `your_script.py` with the actual name of your script.

7. **Deactivate the Virtual Environment**: Once they are done, they can deactivate the virtual environment by simply typing:

   ```bash
   deactivate
   ```
