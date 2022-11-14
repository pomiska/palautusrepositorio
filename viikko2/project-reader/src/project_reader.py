from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)
        ndict = dict(data)
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(ndict["tool"]["poetry"]["name"], ndict["tool"]["poetry"]["description"], ndict["tool"]["poetry"]["dependencies"], ndict["tool"]["poetry"]["dev-dependencies"])
