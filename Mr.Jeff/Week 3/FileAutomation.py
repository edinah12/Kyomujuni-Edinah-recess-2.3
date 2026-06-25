#example 4

#get the file path of the downloads folder
#file path
#approach : pathlib

from datetime import datetime
import os
from pathlib import Path

#old ways using the os.path
file_path = os.path.join(os.path.expanduser("~"), "Downloads", "report.pdf")

#new way using pathlib
file_path = Path.home() / "Downloads" / "report.pdf"

#file organisation script
#real we can automatically organize a download folder by file type

#!\usr\bin

#import libraries
from pathlib import Path
import shutil
from datetime import datetime
from dataclass import dataclass

#configuraion
@dataclass(frozen=True)
class Config:
    destination_dir: Path
    dr_run: bool = True
    
    EXTENSION_MAP = {
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'documents': ['.pdf', '.docx', '.txt'],
        'videos': ['.mp4', '.avi', '.mov'],
        'audio': ['.mp3', '.wav', '.flac'],
        'code': ['.py', '.js', '.html', '.css'],
        'Archives': ['.zip', '.tar', '.gz', '.rar'],
        
    }
    #assignmen 2: wrie a python script that perfirmswill automatically organize the files in your downloads folder based on their file type. The script should create subfolders for each file type and move the files into their respective folders. The script should also log the actions taken, including the file names and their new locations.