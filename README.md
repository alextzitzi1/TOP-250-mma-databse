### 1. Install Python
1. Download Python from [python.org](https://www.python.org/downloads/).
2. During installation, check the box **Add Python to PATH**.
3. Verify the installation:
   ```bash
   python --version
### 2. Install Git
Download Git from git-scm.com.
Follow the installation steps, ensuring Git is added to your system’s PATH.

Verify the installation:
  ```bash
  git --version
  ````
### 3. Clone the Repository
Open a terminal and navigate to the folder where you want to download the project:
```bash
cd path/to/your/desired/folder
```

Clone the repository:
```bash
git clone https://github.com/alextzitzi1/TOP-250-mma-database.git
```
Navigate into the project folder:
```bash
cd TOP-250-mma-database
```
### 5. Install Dependencies
Install the required Python libraries:
```bash

pip install -r requirements.txt
```

### 6. Populate the Database
Run the populate_db.py script to generate the SQLite database (fighter_stats.db):
```bash
python populate_db.py
```
### 7. Generate Graphs
Run the generate_graphs.py script to create visualizations. The graphs will be saved in the static/ folder:
```bash
python generate_graphs.py
```
### 8. Start the Flask App
Run the Flask application:
```bash
python app.py
```
Open a browser and navigate to:
```
http://127.0.0.1:5000/
```
