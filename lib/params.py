TCG_BASE_URL="https://api.justtcg.com/v1"

TCG_GAMES_URL="https://api.justtcg.com/v1/games"

TCG_CARD_URL="https://api.justtcg.com/v1/cards"


YUGIOH_CARD_PARAMS={
    "q": "{NAME} {CARD_NUMBER}",
    "game": "yugioh",
    "printing": "{EDITION}"
}

TEST_PARAMS={
    "q" : "BPT-009",
    "game": "yugioh",
    "include_pricing_history": True
}

API_TCG_CARD_URL= "https://apitcg.com/api/{GAME}/cards/{CARD_NUMBER}"
