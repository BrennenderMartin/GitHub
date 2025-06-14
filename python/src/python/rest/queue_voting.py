import random

# List of songs with their popularity ratings
songs = [
    {"name": "Song A", "popularity": 90},
    {"name": "Song B", "popularity": 80},
    {"name": "Song C", "popularity": 70},
    {"name": "Song D", "popularity": 60},
    {"name": "Song E", "popularity": 50},
    {"name": "Song F", "popularity": 40},
    {"name": "Song G", "popularity": 30},
    {"name": "Song H", "popularity": 20},
    {"name": "Song I", "popularity": 10},
    {"name": "Song J", "popularity": 5},
]

# Initialize votes and queue
votes = {song["name"]: 0 for song in songs}
queue = []
i = 0
# Function to emulate voting
def emulate_voting():
    global votes, queue, i
    while "Song J" not in queue:  # Run until "Song J" is in the queue
        # Weighted random choice based on popularity
        song_names = [song["name"] for song in songs]
        weights = [song["popularity"] for song in songs]
        voted_song = random.choices(song_names, weights=weights, k=1)[0]
        """
        # Increment vote for the chosen song
        votes[voted_song] += 1
        i += 1
        while i % 100 == 0:
            queue.append(voted_song)  # Add the most popular song to the queue
            #print(f"Voted for '{voted_song}'. Current votes: {votes}")
            votes[voted_song] = 0  # Reset votes for that song
        
        """
        # Check if any song has reached 100 votes
        for song_name, vote_count in votes.items():
            if vote_count >= 100:
                queue.append(song_name)  # Add to queue
                votes[song_name] = 0  # Reset votes for that song
                print(f"Added '{song_name}' to queue. Current queue: {queue}")
        

def sort(list): return sorted(list, key=lambda x: x["popularity"], reverse=True)[0]

# Run the emulator
emulate_voting()
print("Final queue length:", len(queue))
