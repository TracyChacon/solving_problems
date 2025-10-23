# Favorite Songs
# Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

# Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

# Each object will have a "title" property (string), and a "plays" property (integer).

# def favorite_songs(playlist:list) -> list:
#     if len(playlist) < 2:
#         return []
    
#     sorted_songs = sorted(
#         playlist, 
#         key=lambda song_dict: song_dict['plays'], 
#         reverse=True
#     )

#     first_popular = sorted_songs[0]
#     second_popular = sorted_songs[1]

#     first = first_popular['title']
#     second = second_popular['title']

#     return [first, second]


# For large data sets the function below guarantees O(N) in contrast to the above function that uses sorted() (which uses timsort) with NlogN guaranteed
def favorite_songs(playlist:list) -> list:
    # O(1) space, O(N) time complexity
    if len(playlist) < 2:
        return []
    
    pop1_plays = -float('inf')
    pop2_plays = -float('inf')
    pop1_title = None
    pop2_title = None

    for song in playlist:
        current_plays = song['plays']
        current_title = song['title']

        if current_plays > pop1_plays:
            # Shift highest down to second highest
            pop2_plays, pop2_title = pop1_plays, pop1_title
            # Update new highest
            pop1_plays, pop1_title = current_plays, current_title
        
        elif current_plays > pop2_plays:
            # Update new second highest
            pop2_plays, pop2_title = current_plays, current_title
 
    return [pop1_title, pop2_title]

if __name__ == "__main__":
    # # should return ["Sync or Swim", "Earbud Blues"].
    # print(favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]))
    # # should return ["Clickwheel Love", "99 Downloads"].
    # print(favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ]))
    # should return ["Song B", "Song C"].
    # print(favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 42}, {"title": "Song C", "plays": 41} ]))

    playlist = [
    {"title": "Skip Track", "plays": 100}, 
    {"title": "99 Downloads", "plays": 100}, 
    {"title": "99 Downloads", "plays": 100}, 
    
    ]

    print(favorite_songs(playlist))