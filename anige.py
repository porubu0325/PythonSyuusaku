import random

def generate_random_anime_name():
    anime_names = ["Naruto", "One Piece", "Dragon Ball", "Attack on Titan", "Death Note", "My Hero Academia", "Sword Art Online"]
    return random.choice(anime_names)

def generate_random_game_name():
    game_names = ["Minecraft", "Fortnite", "The Legend of Zelda", "Overwatch", "Super Mario", "Fallout", "Call of Duty"]
    return random.choice(game_names)

def randomize_anime_and_game():
    anime = generate_random_anime_name()
    game = generate_random_game_name()
    
    # ランダムにアニメ名とゲーム名を組み替える
    if random.choice([True, False]):
        return f"Anime: {anime}, Game: {game}"
    else:
        return f"Game: {game}, Anime: {anime}"

# 10回ランダムな組み替えを生成して表示
for _ in range(10):
    print(randomize_anime_and_game())
