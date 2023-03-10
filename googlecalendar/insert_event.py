#権限付与し直すにはtoken.pickleを一旦無効化する。10行目でどんな権限を付与するか変更可能。
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
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
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    event = {
    'summary': '予定1',
    'location': 'Shibuya Office',
    'description': 'サンプルの予定',
    'start': {
        'dateTime': '2023-01-20T09:00:00',
        'timeZone': 'Japan',
    },
    'end': {
        'dateTime': '2023-01-20T17:00:00',
        'timeZone': 'Japan',
    },
    }

    event = service.events().insert(calendarId='698b78fa48dd2eb17fb7178ea307132d72e901d86b19996ac58a675ea89c8f89@group.calendar.google.com',
                                    body=event).execute()
    print (event['id'])

if __name__ == '__main__':
    main()