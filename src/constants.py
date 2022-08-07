from colr import color
import requests

version = "2.1"
enablePrivateLogging = False
hide_names = True
hide_levels = True


before_ascendant_seasons = [
    "0df5adb9-4dcb-6899-1306-3e9860661dd3",
    "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3",
    "0530b9c4-4980-f2ee-df5d-09864cd00542",
    "46ea6166-4573-1128-9cea-60a15640059b",
    "fcf2c8f4-4324-e50b-2e23-718e4a3ab046",
    "97b6e739-44cc-ffa7-49ad-398ba502ceb0",
    "ab57ef51-4e59-da91-cc8d-51a5a2b9b8ff",
    "52e9749a-429b-7060-99fe-4595426a0cf7",
    "71c81c67-4fae-ceb1-844c-aab2bb8710fa",
    "2a27e5d2-4d30-c9e2-b15a-93b8909a442c",
    "4cb622e1-4244-6da3-7276-8daaf1c01be2",
    "a16955a5-4ad0-f761-5e9e-389df1c892fb",
    "97b39124-46ce-8b55-8fd1-7cbf7ffe173f",
    "573f53ac-41a5-3a7d-d9ce-d6a6298e5704",
    "d929bc38-4ab6-7da4-94f0-ee84f8ac141e",
    "3e47230a-463c-a301-eb7d-67bb60357d4f",
    "808202d6-4f2b-a8ff-1feb-b3a0590ad79f",
]
sockets = {
    "skin": "bcef87d6-209b-46c6-8b19-fbe40bd95abc",
    "skin_level": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
    "skin_chroma": "3ad1b2b2-acdb-4524-852f-954a76ddae0a",
    "skin_buddy": "77258665-71d1-4623-bc72-44db9bd5b3b3",
    "skin_buddy_level": "dd3bf334-87f3-40bd-b043-682a57a8dc3a"
}



AGENTCOLORLIST = {
            "neon": (28, 69, 161),
            "none": (100, 100, 100),
            "viper": (48, 186, 135),
            "yoru": (52, 76, 207),
            "astra": (113, 42, 232),
            "breach": (217, 122, 46),
            "brimstone": (217, 122, 46),
            "cypher": (245, 240, 230),
            "jett": (154,222,255),
            "kay/o": (133, 146, 156),
            "killjoy": (255, 217, 31),
            "omen": (71, 80, 143),
            "phoenix": (254, 130, 102),
            "raze": (217, 122, 46),
            "reyna": (181, 101, 181),
            "sage": (90, 230, 213),
            "skye": (192, 230, 158),
            "sova": (37, 143, 204),
            "chamber": (200, 200, 200),
            "fade": (92, 92, 94)
        }


GAMEPODS = requests.get("https://valorant-api.com/internal/locres/en-US").json()["data"]["UI_GamePodStrings"]

symbol = "■"
PARTYICONLIST = [
            color(symbol, fore=(227, 67, 67)),
            color(symbol, fore=(216, 67, 227)),
            color(symbol, fore=(67, 70, 227)),
            color(symbol, fore=(67, 227, 208)),
            color(symbol, fore=(94, 227, 67)),
            color(symbol, fore=(226, 237, 57)),
            color(symbol, fore=(212, 82, 207)),
            symbol
        ]


NUMBERTORANKS = [
            color('Unranked', fore=(46, 46, 46)),
            color('Unranked', fore=(46, 46, 46)),
            color('Unranked', fore=(46, 46, 46)),
            color('Iron 1', fore=(72, 69, 62)),
            color('Iron 2', fore=(72, 69, 62)),
            color('Iron 3', fore=(72, 69, 62)),
            color('Bronze 1', fore=(187, 143, 90)),
            color('Bronze 2', fore=(187, 143, 90)),
            color('Bronze 3', fore=(187, 143, 90)),
            color('Silver 1', fore=(174, 178, 178)),
            color('Silver 2', fore=(174, 178, 178)),
            color('Silver 3', fore=(174, 178, 178)),
            color('Gold 1', fore=(197, 186, 63)),
            color('Gold 2', fore=(197, 186, 63)),
            color('Gold 3', fore=(197, 186, 63)),
            color('Platinum 1', fore=(24, 167, 185)),
            color('Platinum 2', fore=(24, 167, 185)),
            color('Platinum 3', fore=(24, 167, 185)),
            color('Diamond 1', fore=(216, 100, 199)),
            color('Diamond 2', fore=(216, 100, 199)),
            color('Diamond 3', fore=(216, 100, 199)),
            color('Ascendant 1', fore=(24, 148, 82)),
            color('Ascendant 2', fore=(24, 148, 82)),
            color('Ascendant 3', fore=(24, 148, 82)),
            color('Immortal 1', fore=(221, 68, 68)),
            color('Immortal 2', fore=(221, 68, 68)),
            color('Immortal 3', fore=(221, 68, 68)),
            color('Radiant', fore=(255, 253, 205)),
        ]

tierDict = {
            "0cebb8be-46d7-c12a-d306-e9907bfc5a25": (0, 149, 135),
            "e046854e-406c-37f4-6607-19a9ba8426fc": (241, 184, 45),
            "60bca009-4182-7998-dee7-b8a2558dc369": (209, 84, 141),
            "12683d76-48d7-84a3-4e09-6985794f0445": (90, 159, 226),
            "411e4a55-4e59-7757-41f0-86a53f101bb5": (239, 235, 101),
            None: None
        }

WEAPONS = [
    "Classic",
    "Shorty",
    "Frenzy",
    "Ghost",
    "Sheriff",
    "Stinger",
    "Spectre",
    "Bucky",
    "Judge",
    "Bulldog",
    "Guardian",
    "Phantom",
    "Vandal",
    "Marshal",
    "Operator",
    "Ares",
    "Odin",
    "Melee",
]

DEFAULT_CONFIG = {
        "cooldown": 10,
        "weapon": "Vandal",
        "port": 1100,
        "table": {
            "skin": True,
            "rr": True,
            "peakrank": True,
            "leaderboard": True,
        },
    }