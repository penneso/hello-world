import csv
from collections import Counter

def find_balance(bin, tot_no_companies, bin_count):
    # Finds balance for a single list
    return abs(100*len(bin) - (100*tot_no_companies / bin_count))

def find_tot_balance(bins, tot_no_companies):
    # Takes list of lists which is the bins and bin count, returns total balance
    total_balance = 0.0
    for bin in bins:
        total_balance += find_balance(bin, tot_no_companies, len(bins))
    return total_balance / len(bins)

def fill_bins(scores, bin_count):
    # Populates the bins with scores
    bins = []
    counts = Counter(scores)
    entries = set(scores)

    for entry in entries:
        bin = []
        for count in range(counts[entry]):
            bin.append(entry)
        bins.append(bin)
    #Right now we have as many bins as there were different scores
    #now we need to reduce them until we have the required number of bins
    reduce_bins(bins, bin_count)
    
    return bins

def reduce_bins(bins, bin_count):
    #This combines entries in bins list to reduce the number of bins
    #until we reach the required bin_count
    while len(bins) > bin_count:

        location_to_combine = find_small_bin_combos(bins)
        bins[location_to_combine] = bins[location_to_combine] + bins[location_to_combine + 1]
        del bins[location_to_combine + 1]

    return bins

def find_small_bin_combos(bins):
    #Here we find the 2 bins we can combine (i.e. next to each other)
    #with the smallest sum, these are the best as the next step to combine
    min_length = len(bins[0]) + len(bins[1])
    location = 0
    for i in range(len(bins) - 1):
        if len(bins[i]) + len(bins[i + 1]) < min_length:
            min_length = len(bins[i]) + len(bins[i+1])
            location = i
    return location

def import_csv(filename):
    # Turn a csv of scores into a list of integers
    with open(filename, 'rb') as f:
        return [int(item) for sublist in csv.reader(f) for item in sublist]

def main():
    bin_count = 100#input("Number of bins:")#5
    filename = 'input_scores.csv'#'input_scores.csv'#input("Name of csv with scores:")#test.csv
    scores = import_csv(filename)
    bins = fill_bins(scores, bin_count)

    print(bins)
    print(len(bins),find_tot_balance(bins, len(scores))/100)
    
    return bins
        

if __name__ == '__main__':
    main()
