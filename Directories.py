import os
from shutil import copytree
from progress.bar import Bar

class Directories:
    def __init__(self, path_to, server_list):
        self.path_to = path_to
        self.server_list = server_list
        self.create_directories_with_name_server()

    def create_directories_with_name_server(self):
        for server in self.server_list:
            os.makedirs(self.path_to + server.open, exist_ok=True)
           
    def get_correct_server(self, information_metadata_file):
        correct_server = None
        for server in self.server_list:
            if information_metadata_file.server_name in [server.open, server.bbb, server.ip]:
                correct_server = server
                break

        return correct_server

    def copy_video_bbb(self, path_from, list_information_metadata_file):
        bar = Bar('Copy directories', max=len(list_information_metadata_file))
        for information_metadata_file in list_information_metadata_file:     
            server_to = self.get_correct_server(information_metadata_file)
            try:
                if server_to is not None:
                    path_to = F"{self.path_to}{server_to.open}/{information_metadata_file.root}"
                    copytree(path_from + information_metadata_file.root, path_to)
            except FileExistsError:
                pass

            bar.next()
        bar.finish()