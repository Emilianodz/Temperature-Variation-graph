import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'Temperature Variation graph\data\Madrid Daily Weather 1997-2015_copia.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        except ValueError:
            print("Values empty")

# Plot the high of the day.
plt.style.use('fast')
fig, ax = plt.subplots()
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates, highs, c='red', alpha=0.5)
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)

# Format plot.

plt.title("Daily high and low temperatures", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='minor', labelsize=16)



plt.show()