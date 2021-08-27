import os
import pathlib
from dataclasses import dataclass


@dataclass
class Config:
    OWM_APPID: str = os.environ['OWM_APPID']
    OWM_CALLS_PER_MIN: int = int(os.environ['OWM_CALLS_PER_MIN'])
    OWM_NODE_SIZE: int = int(os.environ['OWM_NODE_SIZE'])
    OWN_STATE_FILE: pathlib.Path = pathlib.Path(os.environ['OWM_STATE_FILE'])

    POSTGRES_HOST: str = os.environ['POSTGRES_HOST']
    POSTGRES_PORT: int = int(os.environ['POSTGRES_PORT'])
    POSTGRES_USER: str = os.environ['POSTGRES_USER']
    POSTGRES_PASS: str = os.environ['POSTGRES_PASS']
