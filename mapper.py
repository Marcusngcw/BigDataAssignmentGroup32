import sys

def mapper():
    for line in sys.stdin:
        
        parts = line.strip().split(',')
        if len(parts) == 2:
            Location = parts[0].strip()
            try:
                Total_Sales = float(parts[1].strip())
                print(f"{Location}\t{Total_Sales}")
            except ValueError:
                continue  

if __name__ == "__main__":
    mapper()

