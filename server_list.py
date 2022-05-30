import json


class ServerList:
    pass


def get_server_list(path_server_list_json: str) -> list:
    server_list = []
    file = open(path_server_list_json, 'r')

    for elem in json.load(file)["server_list"]:
        ser_list = ServerList()
        ser_list.ip = elem['ip']
        ser_list.bbb = elem['bbb']
        ser_list.open = elem['open']
        server_list.append(ser_list)

    return server_list


if __name__ == "__main__":
    pass
    # get_server_list()