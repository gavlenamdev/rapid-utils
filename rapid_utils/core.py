import requests
import uuid
from urllib.parse import unquote
import json
import os

def get_extension(filename):
    '''
    returns extension of filename

    Args:
        filename (str): filename
    Returns:
        extension (str): returns extension in lowercase
    '''
    return filename.rsplit('.', 1)[1]

def is_allowed_extension(filename, formats):
    '''
    checks whether filename extension is in formats

    Args:
        filename (str): filename
        formats (list): list of extensions

    Returns:
        bool: True if filename extension is in formats, False otherwise

    Examples:
        >>> is_allowed_extension('video.mp4', ['mp4', '3gp', 'mkv'])
        True
        >>> is_allowed_extension('video.mp4', ['zip', 'tar'])
        False
    '''
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in formats


def allowed_file(filename, formats):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in formats

def download_file(url, dirname=".", add_prefix=False):
    '''
    downloads files from url

    Args:
        url (str): url
        dirname (str): directory name in which file will be downloading
        add_prefix (bool): adds uuid as prefix to filename if True, nothing otherwise

    Returns:
        filename (str): returns filepath
    '''
    if add_prefix:
        filename = unquote(os.path.sep.join([dirname, uuid.uuid1().hex + url.split("/")[-1]]))
    else:
        filename = unquote(os.path.sep.join([dirname, url.split("/")[-1]]))
    file = requests.get(url, stream=True)
    with open(filename,"wb") as f:
        for chunk in file.iter_content(chunk_size=512 * 1024): 
            if chunk:
                f.write(chunk)
    return filename

def is_json(string=None, path=None):
    try:
        if string:
            json.loads(string)
            return True
        if path:
            json.load(open(path, "r"))
            return True
    except:
        return False

def get_json_from_url(url):
    return requests.get(url).json()

def get_file_size(filepath, unit='MB'):
    filesize = os.path.getsize(filepath)#v /1000/1000, ".2f"))
    return format(float({
        'byte': filesize,
        'kb': filesize/1000,
        'mb': filesize/1000/1000,
        'gb': filesize/1000/1000/1000,
        'tb': filesize/1000/1000/1000/1000
    }[unit.lower()]), ".2f")