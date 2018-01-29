from .dumps.apps import DumpsConfig
from .pcbs.apps import PcbsConfig

class DbprojDumpsConfig(DumpsConfig):
    name = "dbproj.dumps"

class DbprojPcbsConfig(PcbsConfig):
    name = "dbproj.pcbs"

