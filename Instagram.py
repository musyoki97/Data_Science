import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset for September
data = {
    'Date': ['2023-09-01', '2023-09-02', '2023-09-03', '2023-09-04', '2023-09-05',
             '2023-09-06', '2023-09-07', '2023-09-08', '2023-09-09', '2023-09-10',
             '2023-09-11', '2023-09-12', '2023-09-13', '2023-09-14', '2023-09-15',
             '2023-09-16', '2023-09-17', '2023-09-18', '2023-09-19', '2023-09-20',
             '2023-09-21', '2023-09-22', '2023-09-23', '2023-09-24', '2023-09-25',
             '2023-09-26', '2023-09-27', '2023-09-28', '2023-09-29', '2023-09-30'],

    'Views': [2600, 4517, 4912, 5100, 5677,
              4815, 6235, 6644, 5789, 6543,
              7886, 7530, 10137, 9476, 7654,
              8965, 8760, 9911, 10219, 12467,
              13209, 15432, 12879, 14567, 9978,
              15789, 14523, 15670, 13675, 17890],

    'Likes': [1308, 857, 734, 1157, 990,
              3690, 3567, 934, 985, 1212,
              1324, 2086, 1234, 900, 2002,
              1012, 1190, 1387, 909, 1015,
              1500, 1823, 2895, 1320, 1689,
              2900, 3004, 2034, 1709, 1794],

    'Comments': [420, 612, 550, 713, 90,
                 100, 110, 120, 130, 140,
                 150, 160, 170, 180, 190,
                 200, 210, 220, 230, 240,
                 250, 260, 270, 280, 290,
                 300, 310, 320, 330, 340]
}

# Creating a DataFrame from the sample data
df = pd.DataFrame(data)

# Converting the 'Date' column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Calculating the total views, likes, and comments for the month
total_views = df['Views'].sum()
total_likes = df['Likes'].sum()
total_comments = df['Comments'].sum()

# Calculating the average engagement rate (likes + comments per view) for the month
average_engagement_rate = ((df['Likes'] + df['Comments']) / df['Views']).mean() * 100

# Plotting the engagement metrics over the month
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Views'], label='Views', marker='o')
plt.plot(df['Date'], df['Likes'], label='Likes', marker='o')
plt.plot(df['Date'], df['Comments'], label='Comments', marker='o')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('IGTV Video Engagement Over One Month')
plt.legend()
plt.grid(True)

# Displaying engagement summary for the month
print("Engagement Summary for One Month:")
print(f"Total Views: {total_views}")
print(f"Total Likes: {total_likes}")
print(f"Total Comments: {total_comments}")
print(f"Average Engagement Rate: {average_engagement_rate:.2f}%")

# Evaluating success based on engagement metrics
if total_likes > 1000 and total_comments > 100 and average_engagement_rate > 5.0:
    print("This IGTV product has been successful in the past month.")
else:
    print("This IGTV product may need improvement to achieve success.")

# Show the plot
plt.show()
