"""
Parse simple log file and counts the number of ERROR entries.
"""

def count_errors(logfile):
    error_count = 0
    with open(logfile, 'r') as f:
        for line in f:
            if 'ERROR' in line:
                error_count += 1
    return error_count

if __name__ == "__main__":
    # Assume 'application.log' exists in the same directory
    print("Number of ERRORs:", count_errors('application.log'))
