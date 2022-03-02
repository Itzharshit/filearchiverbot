from pony.orm import *
from pyrogram.types import Message
from os import listdir

# ========= DB build =========
db = Database()


class User(db.Entity):
    uid = PrimaryKey(int, auto=True)
    status = Required(int)  # status-user: "INSERT"/"NOT-INSERT"


db.bind(provider='sqlite', filename='zipbot.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# ========= helping func =========
def dir_work(uid: int) -> str:
    """ static-user folder """
    return f"static/{uid}/"


def zip_work(uid: int) -> str:
    """ zip-archive file """
    return f'static/{uid}.zip'


def list_dir(uid: int) -> list:
    """ items in static-user folder """
    return listdir(dir_work(uid))


def up_progress(current, total, msg: Message):
    """ edit status-msg with progress of the uploading """
    msg.edit(f"**התקדמות ההעלאה: {current * 100 / total:.1f}%**")


# ========= MSG class =========
class Msg:

    def start(msg: Message) -> str:
        """ return start-message text """
        txt = f"Hii,/n I am file archiver bot, I can zip Your Files within telegram./nJust send me your file and wait for downloading, after that send /stopzip to starting archiving your file."
        return txt

    zip = "Send the files you want to compress, and at the end send / stopzip after all the files have been downloaded."
          "Only 20 files upto 20 mb are allowed."
    too_big = "File are too much big."
    too_much = "Only 20 files are allowed once."
    send_zip = "Use the / zip command to compress files."
    zipping = "Processing please wait {}..."
    uploading = "📤 Uploading..."
    unknow_error = "Oops! An error occurred, please report in support group. "
   
    downloading = "📥 Downloading..."
    zero_files = "❌ No Files were sent."
