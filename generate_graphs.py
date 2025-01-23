import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from populate_db import Fighter

# Connect to the database
engine = create_engine('sqlite:///fighter_stats.db')
Session = sessionmaker(bind=engine)
session = Session()

# Fetch all fighters and convert to a DataFrame
fighters = session.query(Fighter).all()
data = [{
    "name": fighter.name,
    "performance_score": fighter.performance_score,
    "wins": fighter.wins,
    "losses": fighter.losses,
    "td_avg": fighter.td_avg,
    "SLpM": fighter.SLpM
} for fighter in fighters]

df = pd.DataFrame(data)

# Top 10 Performance Scores
df_performance = df.nlargest(10, 'performance_score')
plt.figure(figsize=(10, 6))
plt.bar(df_performance['name'], df_performance['performance_score'], color='blue')
plt.title('Top 10 Performance Scores')
plt.ylabel('Performance Score')
plt.xlabel('Fighter')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('static/performance_scores.png')

# Win-to-Loss Ratio
df['win_loss_ratio'] = df['wins'] / (df['losses'] + 1e-5)  # Avoid division by zero
df_ratio = df.nlargest(10, 'win_loss_ratio')
plt.figure(figsize=(10, 6))
plt.bar(df_ratio['name'], df_ratio['win_loss_ratio'], color='green')
plt.title('Top 10 Win-to-Loss Ratios')
plt.ylabel('Win/Loss Ratio')
plt.xlabel('Fighter')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('static/win_loss_ratio.png')

# Takedown Average
df_takedown = df.nlargest(10, 'td_avg')
plt.figure(figsize=(10, 6))
plt.bar(df_takedown['name'], df_takedown['td_avg'], color='orange')
plt.title('Top 10 Takedown Averages')
plt.ylabel('Takedown Average')
plt.xlabel('Fighter')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('static/takedown_avg.png')

# SLpM
df_slpm = df.nlargest(10, 'SLpM')
plt.figure(figsize=(10, 6))
plt.bar(df_slpm['name'], df_slpm['SLpM'], color='red')
plt.title('Top 10 SLpM')
plt.ylabel('Significant Strikes Landed per Minute')
plt.xlabel('Fighter')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('static/slpm.png')

print("Graphs generated and saved to the static/ folder.")
