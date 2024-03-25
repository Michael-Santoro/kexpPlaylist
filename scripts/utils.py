from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Text, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def openfile(file_path:str):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            print("File contents:")
            print(file_contents)
            return ' '.join(file_contents.split())
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")

class Hosts(Base):
    __tablename__ = 'hosts'
    id = Column(Integer, primary_key=True)
    uri = Column(String(255))
    name = Column(String(100))
    image_uri = Column(String(255))
    thumbnail_uri = Column(String(255))
    is_active = Column(Boolean)


class Plays(Base):
    __tablename__ = 'plays'
    id = Column(Integer, primary_key=True)
    uri = Column(String(255))
    airdate = Column(TIMESTAMP)
    show_id = Column(Integer)
    song = Column(String(255))
    track_id  = Column(String(255))
    recording_id  = Column(String(255))
    artist = Column(String(255))
    album = Column(String(255))
    release_id = Column(String(255))
    release_group_id = Column(String(255))
    release_date = Column(String(255))
    is_local = Column(Boolean)
    is_request = Column(Boolean)
    is_live = Column(Boolean)
    comment = Column(Text)


class Programs(Base):
    __tablename__ = 'programs'
    id = Column(Integer, primary_key=True)
    uri = Column(String(255))
    name = Column(String(100))
    description = Column(Text)
    tags = Column(String(255))
    is_active = Column(Boolean)

class Shows(Base):
    __tablename__ = 'shows'
    id = Column(Integer, primary_key=True)
    uri = Column(String(255))
    program = Column(Integer)
    program_uri = Column(String(255))
    hosts = Column(String(255))
    program_name = Column(String(255))
    program_tags = Column(String(255))
    tagline = Column(Text)
    image_uri = Column(String(255))
    start_time = Column(TIMESTAMP)

class Timeslots(Base):
    __tablename__ = 'timeslots'
    id = Column(Integer, primary_key=True)
    uri = Column(String(255))
    program = Column(Integer)
    program_uri = Column(String(255))
    program_name = Column(String(255))
    program_tags = Column(String(255))
    weekday = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    start_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP)
    duration = Column(TIMESTAMP)
