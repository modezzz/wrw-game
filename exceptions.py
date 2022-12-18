class EnemyDown(Exception):
    """Display message if enemy have zero health points"""
    def __init__(self, msg: str):
        self.msg = msg


class GameOver(Exception):
    """Display message if player have zero health points"""
    def __init__(self, msg: str):
        self.msg = msg
