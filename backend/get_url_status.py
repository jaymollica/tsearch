import requests
import sys, os

from requests.auth import HTTPBasicAuth
from tsearch.backend.models import Artwork

qs = Artwork.objects.all()

def getr(url):
    return requests.get(url, auth=HTTPBasicAuth('sfmoma01', 'art+data'), verify=False)

def get(url):
    return getr(url).json()

