from __future__ import print_function
import pickle
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from email.mime.text import MIMEText
from email import errors
import base64

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
global msg
"""Shows basic usage of the Gmail API.
Lists the user's Gmail labels.
"""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle','rb') as token:
        creds=pickle.load(token)
    
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds,token)

try:
    # Call the Gmail API
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    print('Labels:')
    for label in labels:
        print(label['name'])

except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f'An error occurred: {error}')


# if __name__ == '__main__':
#     main()
def sent_message():
    gmail_from={
        'mail_from':'alpeshpatilalpesh91@gmail.com'
    }
    gmail_to={
        'mail_to':'alpeshpatilalpesh91@gmail.com'
    }
    gmail_subject='Sending mail using api'
    gmail_content='please let me know how it looks in your email when you get an email using api'

    message=MIMEText(gmail_content)
    message['to']=gmail_to
    message['from']=gmail_from
    message['subject']='gmail_subject'
    raw=base64.urlsafe_b64encode(message.as_bytes())
    raw=raw.decode
    body={'raw':raw}

    try:
        message=(service.users().messages().send(userId='me',body=body).execute())
        print("your message has been sent")
    except errors.MessageError as error:
        print('An error occurred: %s'% error)
        
sent_message()