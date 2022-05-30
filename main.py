from MetadataXML import MetadataXML
from server_list import get_server_list
from Directories import Directories

PATH_LIST_SERVER = "server_list.json"
PATH_FROM = "/var/lib/bigbluebutton/"
PATH_TO = "*"

if __name__ == '__main__':
    ser_list = get_server_list(PATH_LIST_SERVER)
    directories = Directories(path_to=PATH_TO, server_list=ser_list)
    metadata_xml = MetadataXML(PATH_FROM)

    directories.copy_video_bbb(PATH_FROM, metadata_xml.list_information_metadata)
