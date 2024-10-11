# Entity is the return type of the function

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) #dataclass is the class where you can define class variable function body without self keyword
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path 