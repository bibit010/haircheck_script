
### Instructions to Run the Python Script

**HOW TO RUN IT AGAIN**: 

Here's a simplified version of the steps you need to take to run your script again after closing the terminal:

**Open Terminal**: Press `Command + Space`, type "Terminal," and press Enter.

**Navigate to Script Directory**: Change to your script's directory with:
   ```bash
   cd ~/Documents/haircheck_script
   ```

**Activate the Virtual Environment**: Activate your virtual environment:
   ```bash
   source myenv/bin/activate
   ```

**Ensure the CSV File is Ready**: Make sure only **one** CSV file is in the directory.

**Run the Script**: Execute your script:
   ```bash
   python3 pythonscript.py
   ```

After the script runs, remember to delete the CSV file if you don't need it anymore.


### Instructions to Install the Python Script

1. **Open Terminal**: You can quickly open it by pressing:

   `Command + Space` and typing "Terminal" to find it, press Enter to open.

2. **Make sure you have Python installed**: Check for Python by typing:

   ```
   python3 --version
   ```

   If Python is installed, your Mac should return a version number, something like "Python x.xx.x." 

   If you don’t have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

3. **Navigate to your Documents in Terminal**: To do this, use the `cd` command:

   ```
   cd Documents
   ```

   And press Enter. Your terminal should return something like: 

   *"your_macbook_name":Documents "your_macbook_user"$*

4. **Clone the Repository**: 

   Once you have Git, use the following command to clone the GitHub repository where the script is located:

   ```
   git clone https://github.com/bibit010/haircheck_script.git
   ```

   This will create a folder with the same name as the repo in your Documents.

5. **Navigate to the Script Directory**: 

   Change into the directory of the cloned repository using the `cd` command:

   ```
   cd haircheck_script
   ```

6. **Create a Virtual Environment**: To keep dependencies organized, create a virtual environment by running:

   ```
   python3 -m venv myenv
   ```


7. **Activate the Virtual Environment**: Before installing packages, activate your virtual environment:

   ```
   source myenv/bin/activate
   ```

   Your terminal prompt should change to indicate that the virtual environment is active.

8. **Install Required Packages**: Now, install the required packages using the `requirements.txt` file:

   ```
   pip install -r requirements.txt
   ```

9. **Copy the .csv Report You Downloaded**: It is important to only use .csv files with this script. 

    The script is designed to only handle .csv file format and must have the report template we agreed upon. Copy or move the downloaded .csv file into your `Documents/haircheck_script` folder. Ensure you only have **one** single .csv report in the folder whenever running the script, as it cannot differentiate between multiple files. Therefore, make sure to delete the .csv file from the folder after you run the script. 

10. **Run the Script**: Finally, run your Python script by typing:

    ```
    python3 pythonscript.py
    ```

11. **You Should Now Find an .xlsx File in Your Folder**: Go ahead and open the .xlsx file!  

    This can easily be opened with Numbers or even with Preview; no need to install MS Excel. 

    **The Instagram & Facebook datapoints should be coloured in yellow.**

    **The Website datapoints should be in green.**

12. **Please BACKTEST the Script**: That is, check it against previous data.


    You should be able to do this easily by downloading .csv reports for a few past weeks and checking the .xlsx output results against your previous manual reports that you make. 
    If everything is working well, the numbers should match perfectly... *let me know :) *


___
