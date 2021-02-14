import base64
import gspread
from twitter import *

def post_tweet(event, context):

  # API Keys etc. (omitted here)
  token = ''
  token_secret = ''
  consumer_key = ''
  consumer_secret = ''

  # Connect to Twitter
  t = Twitter(
      auth=OAuth(token, token_secret, consumer_key, consumer_secret))

  # # Google sheets (file omitted here)
  gc = gspread.service_account('credentials.json')

  # Open a sheet from a spreadsheet in one go
  wks = gc.open("mindful-mike").sheet1

  # Get next tweet from Google Sheet
  next_tweet = val = wks.acell('A2').value + "\n\n#Mindfulness #MindfulQuotes #Meditation"

  # Post tweet using Twitter API
  t.statuses.update(
      status = next_tweet)

  # Delete sheet row 
  wks.delete_rows(2)
