import websockets
import websockets.client
import ssl
import base64
import json
from colr import color

class Ws:
    def __init__(self, lockfile, Requests, cfg, colors, hide_names, chatlog):

        self.lockfile = lockfile
        self.Requests = Requests
        # websocket.enableTrace(True)
        self.ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE
        self.id_seen = []
        self.cfg = cfg
        self.player_data = {}
        self.messages = 0
        self.colors = colors
        self.hide_names = hide_names
        self.message_history = []
        self.up = "\033[A"
        self.chat_limit = 5
        self.chatlog = chatlog

    def set_player_data(self, player_data):
        self.player_data = player_data

    # async def conntect_to_websocket(self, initial_game_state):


    #     local_headers = {}
    #     local_headers['Authorization'] = 'Basic ' + base64.b64encode(('riot:' + self.lockfile['password']).encode()).decode()
    #     url = f"wss://127.0.0.1:{self.lockfile['port']}"
    #     self.websocket_client = websockets.connect(url, ssl=self.ssl_context, extra_headers=local_headers)
    #     async with self.websocket_client as websocket:
    #         await websocket.send('[5, "OnJsonApiEvent_chat_v4_presences"]')
    #         return None
    #         # while True:
    #         #     response = await websocket.recv()
    #         #     h = self.handle(response, initial_game_state)
    #         #     if h is not None:
    #         #         return h


    async def recconect_to_websocket(self, initial_game_state):
        #wont actually recconect :)
        local_headers = {}
        local_headers['Authorization'] = 'Basic ' + base64.b64encode(('riot:' + self.lockfile['password']).encode()).decode()
        url = f"wss://127.0.0.1:{self.lockfile['port']}"
        self.websocket_client = websockets.connect(url, ssl=self.ssl_context, extra_headers=local_headers)
        async with self.websocket_client as websocket:
            await websocket.send('[5, "OnJsonApiEvent_chat_v4_presences"]')
            if self.cfg.get_feature_flag("game_chat"):
                await websocket.send('[5, "OnJsonApiEvent_chat_v6_messages"]')
            while True:
                response = await websocket.recv()
                h = self.handle(response, initial_game_state)
                if h is not None:
                    await websocket.close()
                    return h

    def handle(self, m, initial_game_state):
        if len(m) > 10:
            resp_json = json.loads(m)
            if resp_json[2].get("uri") == "/chat/v4/presences":
                presence = resp_json[2]["data"]["presences"][0]
                if presence['puuid'] == self.Requests.puuid:
                    if presence.get("championId") is not None or presence.get("product") == "league_of_legends":
                        state = None
                    else:
                        state = json.loads(base64.b64decode(presence['private']))["sessionLoopState"]
                    
                    if state is not None:
                        if state != initial_game_state:
                            return state
            if resp_json[2].get("uri") == "/chat/v6/messages":
                message = resp_json[2]["data"]["messages"][0]
                #currently only game chat no pregame or menu
                if "ares-coregame" in message["cid"]:
                    if message["id"] not in self.id_seen:
                        if self.player_data[message["puuid"]]["team"] == "Red":
                            clr = (238, 77, 77)
                        else:
                            clr = (76, 151, 237)
                        agent = self.colors.get_agent_from_uuid(self.player_data[message['puuid']]['agent'].lower())
                        name = f"{message['game_name']}#{message['game_tag']}"
                        if self.player_data[message['puuid']]['streamer_mode'] and self.hide_names and message['puuid'] not in self.player_data["ignore"]:
                            self.print_message(f"{color(agent, clr)}: {message['body']}")
                        else:
                            if agent == "":
                                agent_str = ""
                            else:
                                agent_str = f" ({agent})"
                            self.print_message(f"{color(name, clr)}{agent_str}: {message['body']}")
                        self.id_seen.append(message['id'])

    def print_message(self, message):
        self.chatlog(message)
        self.messages += 1
        if self.messages > self.chat_limit:
            print(self.up * self.chat_limit, end="")
            for i in range(len(self.message_history) - self.chat_limit + 1, len(self.message_history)):
                print(self.message_history[i] + " " * max([0, len(self.message_history[i-1]) - len(self.message_history[i])]))
            print(message + " " * max([0, len(self.message_history[-1]) - len(message)]))
        else:
            print(message)

        self.message_history.append(message)


# if __name__ == "__main__":
#     try:
#         with open(os.path.join(os.getenv('LOCALAPPDATA'), R'Riot Games\Riot Client\Config\lockfile')) as lockfile:
#             data = lockfile.read().split(':')
#             keys = ['name', 'PID', 'port', 'password', 'protocol']
#             lockfile = dict(zip(keys, data))
#     except:
#         raise Exception("Lockfile not found")


#     ws = Ws(lockfile, "MENUS")
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(ws.conntect_to_websocket("MENUS"))
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop.run_forever()
