data = {
    'players': {
        'alice': {
            'level': 41, 'total_score': 2824, 'sessions_played': 13,
            'favorite_mode': 'ranked', 'achievements_count': 5,
            "region": "east"
        },
        'bob': {
            'level': 16, 'total_score': 4657, 'sessions_played': 27,
            'favorite_mode': 'ranked', 'achievements_count': 2,
            "region": "north"
        },
        'charlie': {
            'level': 44, 'total_score': 9935, 'sessions_played': 21,
            'favorite_mode': 'ranked', 'achievements_count': 7,
            "region": "north"
        },
        'diana': {
            'level': 3, 'total_score': 1488, 'sessions_played': 21,
            'favorite_mode': 'casual', 'achievements_count': 4,
            "region": "central"
        },
        'eve': {
            'level': 33, 'total_score': 1434, 'sessions_played': 81,
            'favorite_mode': 'casual', 'achievements_count': 7,
            "region": "west"
        },
        'frank': {
            'level': 15, 'total_score': 8359, 'sessions_played': 85,
            'favorite_mode': 'competitive', 'achievements_count': 1,
            "region": "north"
        }
    },
    'sessions': [
        {
            'player': 'bob', 'duration_minutes': 94, 'score': 1831, 'mode':
            'competitive', 'completed': False
        },
        {
            'player': 'bob', 'duration_minutes': 32, 'score': 1478, 'mode':
            'casual', 'completed': True
        },
        {
            'player': 'diana', 'duration_minutes': 17, 'score': 1570, 'mode':
            'competitive', 'completed': False
        },
        {
            'player': 'alice', 'duration_minutes': 98, 'score': 1981, 'mode':
            'ranked', 'completed': True
        },
        {
            'player': 'diana', 'duration_minutes': 15, 'score': 2361, 'mode':
            'competitive', 'completed': False
        },
        {
            'player': 'eve', 'duration_minutes': 29, 'score': 2985, 'mode':
            'casual', 'completed': True
        },
        {
            'player': 'frank', 'duration_minutes': 34, 'score': 1285, 'mode':
            'casual', 'completed': True
        },
        {
            'player': 'alice', 'duration_minutes': 53, 'score': 1238, 'mode':
            'competitive', 'completed': False
        },
        {
            'player': 'bob', 'duration_minutes': 52, 'score': 1555, 'mode':
            'casual', 'completed': False
        },
        {
            'player': 'frank', 'duration_minutes': 92, 'score': 2754, 'mode':
            'casual', 'completed': True
        },
        {
            'player': 'eve', 'duration_minutes': 98, 'score': 1102, 'mode':
            'casual', 'completed': False
        },
        {
            'player': 'diana', 'duration_minutes': 39, 'score': 2721, 'mode':
            'ranked', 'completed': True
        },
        {
            'player': 'frank', 'duration_minutes': 46, 'score': 329, 'mode':
            'casual', 'completed': True
        },
        {
            'player': 'charlie', 'duration_minutes': 56, 'score': 1196, 'mode':
            'casual', 'completed': True
        },
        {
            'player': 'eve', 'duration_minutes': 117, 'score': 1388, 'mode':
            'casual', 'completed': False
        },
        {
            'player': 'diana', 'duration_minutes': 118, 'score': 2733, 'mode':
            'competitive', 'completed': True
        },
        {
            'player': 'charlie', 'duration_minutes': 22, 'score': 1110, 'mode':
            'ranked', 'completed': False
        },
        {
            'player': 'frank', 'duration_minutes': 79, 'score': 1854, 'mode':
            'ranked', 'completed': False
        },
        {
            'player': 'charlie', 'duration_minutes': 33, 'score': 666, 'mode':
            'ranked', 'completed': False
        },
        {
            'player': 'alice', 'duration_minutes': 101, 'score': 292, 'mode':
            'casual', 'completed': True
        },
        {
            'player': 'frank', 'duration_minutes': 25, 'score': 2887, 'mode':
            'competitive', 'completed': True
        },
        {
            'player': 'diana', 'duration_minutes': 53, 'score': 2540, 'mode':
            'competitive', 'completed': False
        },
        {
            'player': 'eve', 'duration_minutes': 115, 'score': 147, 'mode':
            'ranked', 'completed': True
        },
        {
            'player': 'frank', 'duration_minutes': 118, 'score': 2299, 'mode':
            'competitive', 'completed': False
        },
        {
            'player': 'alice', 'duration_minutes': 42, 'score': 1880, 'mode':
            'casual', 'completed': False
        },
        {
            'player': 'alice', 'duration_minutes': 97, 'score': 1178, 'mode':
            'ranked', 'completed': True
        },
        {
            'player': 'eve', 'duration_minutes': 18, 'score': 2661, 'mode':
            'competitive', 'completed': True
        },
        {
            'player': 'bob', 'duration_minutes': 52, 'score': 761, 'mode':
            'ranked', 'completed': True
        },
        {
            'player': 'eve', 'duration_minutes': 46, 'score': 2101, 'mode':
            'casual', 'completed': True
        },
        {
            'player': 'charlie', 'duration_minutes': 117, 'score': 1359,
            'mode': 'casual', 'completed': True
        }
    ],
    'game_modes': [
        'casual', 'competitive', 'ranked'
    ],
    'achievements': [
        'first_blood', 'level_master', 'speed_runner', 'treasure_seeker',
        'boss_hunter', 'pixel_perfect', 'combo_king', 'explorer'
    ]
}

print("=== Game Analytics Dashboard ===\n")
print("=== List Comprehension Examples ===")
# high score > 2000
players = data.get("players")
sessions = data.get("sessions")
high_score = [x for x, y in players.items() if y["total_score"] > 2000]
print(f"High scorers (>2000): {high_score}")
doubled = [x["score"]*2 for x in sessions]
print(f"Scores doubled: {doubled}")
active = [x for x in players.keys()]
print(f"Active players: {active}")

print("\n=== Dict Comprehension Examples ===")
player_score = {x: y["total_score"] for x, y in players.items()}
print(f"Player scores: {player_score}")

all_modes = [s['mode'] for s in data['sessions']]
mode_counts = {m: all_modes.count(m) for m in data['game_modes']}
print(f"Score categories: {mode_counts}")

ach_count = {x: y["achievements_count"] for x, y in players.items()}
print(f"Achievement counts: {ach_count}")

print("\n=== Set Comprehension Examples ===")
unique_players = {x["player"] for x in sessions}
print(f"Unique players: {unique_players}")
unique_achievements = {x for x in data.get("achievements")}
print(f"Unique achievements: {unique_achievements}")
active_regions = {x["region"] for x in players.values()}
print(f"Active regions: {active_regions}")

print("\n=== Combined Analysis ===")
print(f"Total players: {len(unique_players)}")
print(f"Total achievement: {len(unique_achievements)}")
score_list = [x["score"] for x in sessions]
print(f"Average score: {sum(score_list) / len(score_list):.2f}")
perfomers = {
    x: [y["total_score"], y["achievements_count"]] for x, y in players.items()
}
best_perf = max(perfomers, key=perfomers.get)
stats = players.get(best_perf)
score = stats['total_score']
achs = stats['achievements_count']

print(f"Top performer: {best_perf} ({score} points, {achs} achievements)")
