#get curr directore


def get_curr_dir():
    from os import path
    return path.dirname(path.abspath(__file__))


def get_date_brazil(date_to_format:str):
    from datetime import datetime
    return datetime.strftime(date_to_format, '%d/%m/%Y')