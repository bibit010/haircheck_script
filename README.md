

### Instructions to Run the Python Script

1. **Open Terminal**: You can quickly open it by pressing `Command + Space` and typing "Terminal" to find and open it.

2. **Make sure you have Git installed**: You can check by typing:

   ```
   git --version
   ```

   If Git is installed, you should see a version number. If not, you can install it by downloading it from [git-scm.com](https://git-scm.com/downloads).

3. **Make sure you have Python installed**: Check for Python by typing:

   ```
   python3 --version
   ```
   
   If Python is installed, your Mac should returnt you a version number, something like "Python x.xx.x" if it is installed. 

   If you don’t have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

4. **Navigate to your Documents in Terminal**: To do this, use the `cd` command:

   ```
   cd Documents
   ```
   
   And press Enter. Your terminal should return something like: *"your_macbook_name":Documents "your_macbook_user"$*

5. **Clone the Repository**: 
   Once you have Git, use the following command to clone the GitHub repository where the script is located:

   ```
   git clone https://github.com/bibit010/natalia_script.git
   ```

   This will create a folder with the same name as the repo in your Documents.

6. **Navigate to the Script Directory**: 
   Change into the directory of the cloned repository using the `cd` command:

   ```
   cd natalia_script
   ```

7. **Install Required Packages**: Now, install the required packages using the `requirements.txt` file:

   ```
   pip install -r requirements.txt
   ```

8. **Copy the .csv report you downloaded**: It is important to only use .csv files with this script. 

   The script is designed to only handle .csv file format, and must have the report template we agreed upon. Cope or move the downloaded .csv file into your mac/Documents/natalia_script folder. It is important to do this before running the script. Make sure you only have 1 single .csv report in the folder whenever running the script as it cannot differentiate between multiple files, therefore, make sure to delete .csv file from the folder after you run the script. 

9. **Run the Script**: Finally, run your Python script by typing:

   ```
   python3 pythonscript.py
   ```

10. **You should now find .xlsx file in your folder**: Go ahead and open the .xlsx file!  
   This can easily be opened with Numbers or even with Preview, no need to install MS Excel. 
   **The Instagram&Facebook datapoints should be coloured in yellow.**
   **The Website datapoints should be in Blue.**


11. **Please BACKTEST the script**: ie. check it against previous data
   You should be able to do this easily by downloading .csv reports for a few past weeks and checking the .xlsx output results against your previous manual reports that you make. 
   If everything is working well, the numbers should match perfectly.... *let me know :) *

---

