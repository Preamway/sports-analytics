# Import necessary data analytics libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # 1. CREATE MOCK DATA (Simulating NFL Combine Data)
    data = {
        'Player': ['Athlete A', 'Athlete B', 'Athlete C', 'Athlete D', 'Athlete E', 'Athlete F', 'Athlete G'],
        'Position': ['WR', 'RB', 'Lineman', 'WR', 'RB', 'Lineman', 'WR'],
        '40_Yard_Dash': [4.35, 4.45, 5.12, 4.40, 4.52, 5.25, 4.38],
        'Vertical_Jump_Inches': [39.5, 36.0, 28.5, 38.0, 35.5, 27.0, 40.0],
        'Bench_Press_Reps': [12, 20, 32, 14, 22, 29, 11]
    }

    # Load data into a Pandas DataFrame
    df = pd.DataFrame(data)

    print("--- Initial Dataset ---")
    print(df.to_string())
    print("\n")

    # 2. DATA ANALYSIS & AGGREGATION
    # Calculate average metrics by position
    position_stats = df.groupby('Position').mean(numeric_only=True).round(2)

    print("--- Average Performance by Position ---")
    print(position_stats.to_string())

    # 3. DATA VISUALIZATION
    # Set the style of the graphs
    sns.set_theme(style="darkgrid")

    # Create a figure with two subplots (1 row, 2 columns)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Graph 1: Speed vs. Explosive Power
    sns.scatterplot(
        data=df, 
        x='40_Yard_Dash', 
        y='Vertical_Jump_Inches', 
        hue='Position', 
        s=150, 
        ax=axes[0],
        palette='Set1'
    )
    axes[0].set_title('Explosive Power: Speed vs. Vertical Jump', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('40-Yard Dash (Seconds)')
    axes[0].set_ylabel('Vertical Jump (Inches)')
    axes[0].invert_xaxis() # Lower time is better

    # Graph 2: Bench Press Reps by Position
    sns.barplot(
        data=df, 
        x='Position', 
        y='Bench_Press_Reps', 
        errorbar=None,
        ax=axes[1],
        palette='viridis'
    )
    axes[1].set_title('Strength: Average Bench Press by Position', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Position')
    axes[1].set_ylabel('Bench Press (225 lb Reps)')

    # Show the plots
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
