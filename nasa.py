import os
import requests
import json

NASA = os.environ['NASA_TOKEN']

class APOD:
  def __init__(self, date, explanation, url, title):
    self.date = date
    self.desc = explanation
    self.url = url
    self.title = title
  
  def printAPOD(self):
    return "**"+self.date+" Astronomy Picture of the Day**\n**Image URL: **"+self.url+"\n**Title:** *"+self.title+"*\n**Description:** "+self.desc


def getAPOD():
  response =requests.get("https://api.nasa.gov/planetary/apod?api_key="+NASA)
  json_data = json.loads(response.text)

  apod = APOD(json_data['date'],json_data['explanation'], json_data['url'], json_data['title'])

  return apod

