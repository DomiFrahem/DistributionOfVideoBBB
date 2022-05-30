from bs4 import BeautifulSoup
from os import walk, listdir
import re

class MetadataXML:
    files_metadata = []
    list_information_metadata = []

    def __init__(self, path_directory_with_video):
        self.path_directory_with_video = path_directory_with_video
        self.create_list_files_metadata()
        self.create_list_information_metadata_file()

    def create_list_files_metadata(self):
        for root, _, files in walk(self.path_directory_with_video):
            self.files_metadata += [root + '/' + file for file in files if 'metadata' in file]

    def create_list_dir_raw(self):
        for dirs in listdir(F"{self.path_directory_with_video}recording/raw/"):
            self.list_raw.append(dirs)

    def get_list_files_metadata(self) -> list:
        return self.files_metadata

    class InformationMetaData:
        pass

    def create_list_information_metadata_file(self):
        for file in self.files_metadata:
            bs_data = BeautifulSoup(open(file), 'xml')
            server_origin = bs_data.find_all("bbb-origin-server-name")[0].get_text()

            information_metadata = self.InformationMetaData()
            information_metadata.id = bs_data.find_all("id")[0].get_text()
            information_metadata.server_name = server_origin
            information_metadata.root = "/".join(file.split("/")[0:-1]).replace(self.path_directory_with_video, "")
            self.list_information_metadata.append(information_metadata)


if __name__ == "__main__":
    metadata_xml = MetadataXML("/home/alex/bigbluebutton/")
    metadata_xml.create_list_information_metadata_file()
