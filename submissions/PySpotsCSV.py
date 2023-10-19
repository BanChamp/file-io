import pandas as pd

# Your functions for counting songs with key 'E' and finding the most streamed artist
def count_songs_with_key(data):
    counts = data['key'].value_counts().get('E', 0)
    return counts

def count_occurrences_of_values(data):
    artists = data['artist(s)_name']
    dict = {}

    for artist in artists:
        names = artist.split(', ')
        for name in names:
            name = name.strip()
            if name not in dict:
                dict[name] = 1
            else:
                dict[name] += 1

    keyMax = max(zip(dict.values(), dict.keys()))[1]
    return keyMax

# Read the CSV file into a DataFrame
data = pd.read_csv('your_csv_file.csv', sep='\t')

# Solution 1: Number of songs
numOfSongs = len(data)
print("Number of songs:", numOfSongs)

# Solution 2: Number of songs with key 'E'
numOfSongsWithE = count_songs_with_key(data)
print("Number of songs with key E:", numOfSongsWithE)

# Solution 3: Most streamed artist
mostOccurences = count_occurrences_of_values(data)
print("Most streamed artist:", mostOccurences)
