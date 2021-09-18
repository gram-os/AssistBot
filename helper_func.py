import requests
import json
import string

def clean_message(msg):
  msg=msg.lower()
  msg=msg.translate(str.maketrans('', '', string.punctuation))
  msg=set(msg.split())
  return msg

def get_quote():
  response = requests.get("http://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -"+json_data[0]['a']

  return quote
  
def get_insult():
  response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
  json_data=json.loads(response.text)
  return json_data['insult']