from lib.params import YUGIOH_CARD_PARAMS

class YuGiOhCard:
    def __init__(self, data: dict):
        self.name: str = data.get("name")
        self.attribute: str = data.get("attribute")
        self.stars: int = data.get("stars")
        self.atk: int = data.get("ATK")
        self.defense: int = data.get("DEF")
        self.description: str = data.get("description")
        self.card_number: str = data.get("card_number")
        self.video_game_identifier: int = data.get("video_game_identifier")
        self.edition: str = data.get("edition")

    def __repr__(self):
        return f"<YuGiOhCard {self.name} ({self.card_number})>"
    
    def format_yugioh_params(self) -> dict:
        """
        Applies .format() to every value in YUGIOH_CARD_PARAMS.
        """
        return {
            key: value.format(
                NAME=self.name,
                CARD_NUMBER=self.card_number,
                EDITION=self.edition
            )
            for key, value in YUGIOH_CARD_PARAMS.items()
        }
