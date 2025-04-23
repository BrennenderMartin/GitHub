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

# Function to emulate voting
def emulate_voting():
    global votes, queue
    while "Song J" not in queue:  # Run until "Song J" is in the queue
        # Weighted random choice based on popularity
        song_names = [song["name"] for song in songs]
        weights = [song["popularity"] for song in songs]
        voted_song = random.choices(song_names, weights=weights, k=1)[0]
        
        # Increment vote for the chosen song
        votes[voted_song] += 1
        
        # Check if any song has reached 100 votes
        for song_name, vote_count in votes.items():
            if vote_count >= 100:
                queue.append(song_name)  # Add to queue
                votes[song_name] = 0  # Reset votes for that song
                print(f"Added '{song_name}' to queue. Current queue: {queue}")

# Run the emulator
emulate_voting()
print("Final queue length:", len(queue))
