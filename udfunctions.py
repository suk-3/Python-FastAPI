from logger import putlog
import json
import os
import re

log = putlog(__file__)


def readFile(filename):
    """
    The function `readFile` reads the content of a file and returns it as a string, handling any
    exceptions that may occur during the process.
    
    :param filename: The `readFile` function is designed to read the content of a file specified by the
    `filename` parameter. The function attempts to open the file in read mode, reads its content, and
    returns the content as a string. If an exception occurs during the file reading process, the
    function logs the
    :return: The function `readFile` is returning the content of the file with the given `filename`. If
    the file is successfully read, the content of the file is returned as a string. If there is an error
    during the file reading process, an empty string will be returned.
    """
    content = ""

    try:
        with open(filename, 'r') as fileContent:
            content = fileContent.read()
    except Exception as Err:
        log.error("{}".format(Err))

    return content


def readJson(filename):
    """
    The function `readJson` reads and loads JSON content from a file, handling exceptions and logging
    errors if encountered.
    
    :param filename: The `filename` parameter in the `readJson` function is a string that represents the
    name of the file from which you want to read JSON data
    :return: The function `readJson` is returning the content of a JSON file after loading it using
    `json.loads`. If an error occurs during the process, it will log the error and return an empty
    dictionary.
    """
    content = {}

    try:
        content = json.loads(readFile(filename))
    except Exception as Err:
        log.error("{}".format(Err),exc_info=True)

    return content


def writeFile(filename, content):
    """
    The function `writeFile` writes content to a file and returns a status indicating success or
    failure.
    
    :param filename: The `filename` parameter is a string that represents the path to the file where the
    content will be written
    :param content: The `content` parameter in the `writeFile` function is the data that you want to
    write to the file specified by the `filename` parameter. This data will be written to the file in
    the function using the `write` method of the file object
    :return: The function `writeFile` returns the status of the operation, which can be either "Success"
    if the file was written successfully, or "Failed" if there was an error during the writing process.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    status = "Success"
    try:
        with open(filename, 'w') as fileSource:
            fileSource.write(content)
    except Exception as Err:
        log.error("{}".format(Err))
        status = "Failed"

    return status


def writeJson(filename, content):
    """
    The function `writeJson` writes JSON content to a file and returns a status indicating success or
    failure.
    
    :param filename: The `filename` parameter is a string that represents the name of the file where the
    JSON content will be written to
    :param content: The `content` parameter in the `writeJson` function is the data that you want to
    write to a JSON file. This data will be converted to a JSON string using the `json.dumps()` function
    before writing it to the file
    :return: The function `writeJson` returns the status of the operation, which can be either "Success"
    if the JSON content was successfully written to the file, or "Failed" if an exception occurred
    during the process.
    """
    status = "Success"

    try:
        contentDump = json.dumps(content, indent=4, sort_keys=True)
        writeFile(filename, contentDump)
    except Exception as Err:
        log.error("{}".format(Err))
        status = "Failed"

    return status


configFile = "config/app.setting.json"
configuration = readJson(configFile)