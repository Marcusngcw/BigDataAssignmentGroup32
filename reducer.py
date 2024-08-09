import sys
from collections import defaultdict

def reducer():
    location_sales = defaultdict(float)
    
    for line in sys.stdin:
        Location, Total_Sales = line.strip().split('\t')
        try:
            Total_Sales = float(Total_Sales)
            location_sales[Location] += Total_Sales
        except ValueError:
            continue  

    # Convert dictionary to list and sort by Total_Sales in descending order
    sorted_locations = sorted(location_sales.items(), key=lambda x: x[1], reverse=True)

    # Output the top 5 locations
    for Location, Total_Sales in sorted_locations[:5]:
        print(f"{Location}\t{Total_Sales}")

if __name__ == "__main__":
    reducer()
