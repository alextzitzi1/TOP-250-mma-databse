import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the database
engine = create_engine('sqlite:///fighter_stats.db')
Base = declarative_base()

# Define Fighter table
class Fighter(Base):
    __tablename__ = 'fighters'
    id = Column(Integer, primary_key=True, autoincrement=True)  # Auto-increment ID
    name = Column(String, nullable=False, unique=True)  # Unique to prevent duplicates
    wins = Column(Integer, nullable=False)
    losses = Column(Integer, nullable=False)
    height = Column(Float, nullable=True)
    weight = Column(Float, nullable=True)
    reach = Column(Float, nullable=True)
    stance = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    SLpM = Column(Float, nullable=True)
    sig_str_acc = Column(Float, nullable=True)
    SApM = Column(Float, nullable=True)
    str_def = Column(Float, nullable=True)
    td_avg = Column(Float, nullable=True)
    td_acc = Column(Float, nullable=True)
    td_def = Column(Float, nullable=True)
    sub_avg = Column(Float, nullable=True)
    performance_score = Column(Float, nullable=True)

# Create the table
Base.metadata.create_all(engine)

# Set up the session
Session = sessionmaker(bind=engine)
session = Session()

# Load the Excel file
file_path = 'fighter_data.xlsx'  # Ensure this file exists in the same directory
fighters_df = pd.read_excel(file_path)

# Insert fighters into the database, checking for duplicates
# Insert fighters into the database, checking for duplicates
for _, row in fighters_df.iterrows():
    # Check if the fighter already exists
    existing_fighter = session.query(Fighter).filter_by(name=row['name']).first()
    if existing_fighter is None:
        # Convert and round weight to 1 decimal place
        weight = None
        try:
            weight = round(float(row['weight']), 1)  # Convert weight to float and round to 1 decimal
        except (ValueError, TypeError):
            print(f"Invalid weight for fighter {row['name']}: {row['weight']}")  # Log any issues

        # Create and add the fighter object
        fighter = Fighter(
            name=row['name'],
            wins=row['wins'],
            losses=row['losses'],
            height=row['height'],
            weight=weight,  # Use the rounded weight
            reach=row['reach'],
            stance=row['stance'],
            age=row['age'],
            SLpM=row['SLpM'],
            sig_str_acc=row['sig_str_acc'],
            SApM=row['SApM'],
            str_def=row['str_def'],
            td_avg=row['td_avg'],
            td_acc=row['td_acc'],
            td_def=row['td_def'],
            sub_avg=row['sub_avg'],
            performance_score=row['performance_score']
        )
        session.add(fighter)

# Commit all changes
session.commit()

print("Database populated successfully!")
