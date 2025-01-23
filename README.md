Setup Instructions
1. Clone the Repository
If you haven’t cloned the repository yet, run:

In the terminal(windows button + r and then type cmd):
  
  git clone https://github.com/alextzitzi1/TOP-250-mma-database.git     
  cd TOP-250-mma-database
2. Install Dependencies
Install the necessary Python libraries using pip:

bash
Copy
Edit
pip install -r requirements.txt
The dependencies include:


Flask: For creating the web application.

SQLAlchemy: For interacting with the SQLite database.

Pandas: For handling and processing data.

Matplotlib: For generating graphs.

3. Populate the Database

Run the populate_db.py script to populate the SQLite database (fighter_stats.db) with data from the fighter_data.xlsx file:

python populate_db.py

4. Generate Graphs

Run the generate_graphs.py script to create visualizations. The graphs will be saved as PNG files in the static/ folder:

python generate_graphs.py

5. Start the Flask App
 
Run the app.py script to start the web server:

python app.py

6. Access the Web Application
7. 
Open your browser and navigate the given link.
