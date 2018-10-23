class ClientFile:
    def __init__(self, file_name: str, contents: str, append: bool):
        self.file_name = file_name
        self.contents  = contents
        self.append    = append