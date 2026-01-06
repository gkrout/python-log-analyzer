def analyzer_log(file_path):
  count = {
      "INFO": 0,
      "WARNING": 0,
      "ERROR": 0,
      "TOTAL": 0
  }
  
  with open(file_path, 'r') as file:
    for line in file:
        if "INFO" in line:
            count["INFO"] += 1
        elif "WARNING" in line:
            count["WARNING"] += 1
        elif "ERROR" in line:
            count["ERROR"] += 1
        count["TOTAL"] += 1
        
  return count
# Example usage:
# log_counts = analyzer_log('path/to/logfile.log')
# print(log_counts)
if __name__ == "__main__":
    log_counts = analyzer_log('sample.log')
    for key, value in log_counts.items():
        print(f"{key}: {value}")