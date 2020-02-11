import json


data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)
    json_string = json.dumps(data)
    pass
json_string = json.dumps(data, indent=4)

blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)

blackjack_hand == decoded_hand
# False
type(blackjack_hand)
# <class 'tuple'>
type(decoded_hand)
# <class 'list'>
blackjack_hand == tuple(decoded_hand)
