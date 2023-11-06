import random

# アニメの名前のリスト
anime_names = ["鬼滅の刃", "呪術廻戦", "進撃の巨人", "名探偵コナン", "ドラゴンボール", "ONE PIECE"]
# ゲームの名前のリスト
game_names = ["Minecraft", "Fortnite", "PUBG", "Among Us", "League of Legends", "Call of Duty"]
# 海外のYouTuberの名前のリスト
youtuber_names = ["MrBeast", "PewDiePie", "Markiplier", "Jacksepticeye", "DanTDM", "Dream"]

# 1から100までの数字をループで処理
for i in range(1, 101):
  # 3の倍数の場合はアニメの名前をランダムで表示
  if i % 15 == 0:
    print(random.choice(anime_names))
  # 5の倍数の場合はゲームの名前をランダムで表示
  elif i % 5 == 0:
    print(random.choice(game_names))
  # 15の倍数の場合は海外のYouTuberの名前をランダムで表示
  elif i % 3 == 0:
    print(random.choice(youtuber_names))
  # 3でも5でも15でもない場合は、数字をそのまま表示
  else:
    print(i)
