from lib.lib import YuGiOhCard
import yugioh

def get_yugioh_card_pricing(card : YuGiOhCard) -> dict:
    card_info = yugioh.get_card(card_id=card.video_game_identifier)
    print(card_info.name)
    print(f"{card} has prices of \n\
        tcg_player: {card_info.tcgplayer_price}\n\
        amazon: {card_info.amazon_price} \n\
        cardmarket: {card_info.cardmarket_price}\n\
        ebay: {card_info.ebay_price}\n\
        coolstuffinc: {card_info.coolstuffinc_price}")
    pass

if __name__ == '__main__':
    example_card = {
        "name": "BLUE-EYES WHITE DRAGON", 
        "attribute": "LIGHT", 
        "stars": 8,
        "ATK": 3000,
        "DEF": 2500,
        "description": "This legendary dragon is a powerful engine of destruction. Virtually invincible, very few have faced this awesome creature and lived to tell the tale.", 
        "card_number": "BPT-009", 
        "video_game_identifier": 89631139,
        "edition": "1st Edition"
    }
    card = YuGiOhCard(example_card)
    get_yugioh_card_pricing(card)