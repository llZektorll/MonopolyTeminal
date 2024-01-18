
def inintialize_board():
    return [
        {"name": "Go", "cost": 0, "rent": 0, "owner": None},
        {"name": "house_1", "cost": 350, "rent": 35, "owner": None},
        {"name": "house_2", "cost": 250, "rent": 25, "owner": None},
        {"name": "house_3", "cost": 150, "rent": 15, "owner": None},
        {"name": "house_4", "cost": 650, "rent": 65, "owner": None},
        {"name": "house_5", "cost": 450, "rent": 45, "owner": None},
        {"name": "house_6", "cost": 250, "rent": 25, "owner": None},
        {"name": "house_7", "cost": 350, "rent": 35, "owner": None},
        {"name": "house_8", "cost": 150, "rent": 15, "owner": None},
        {"name": "house_9", "cost": 550, "rent": 55, "owner": None},
        {"name": "house_10", "cost": 450, "rent": 45, "owner": None},
        {"name": "house_11", "cost": 350, "rent": 35, "owner": None},
    ]


def display_board(board):
    print("Current Board:")
    for property in board:
        print(
            f"{property['name']} - Owner: {property['owner'] if property['owner'] else 'None'}")
