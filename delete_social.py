import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_gmail_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def delete_social_emails(service, max_delete=30000):
    query = "label:social"
    deleted = 0
    page_token = None

    while deleted < max_delete:
        response = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=min(500, max_delete - deleted),
            pageToken=page_token
        ).execute()

        messages = response.get('messages', [])
        if not messages:
            break

        msg_ids = [msg['id'] for msg in messages]

        service.users().messages().batchDelete(
            userId='me',
            body={'ids': msg_ids}
        ).execute()

        deleted += len(msg_ids)
        print(f"Deleted {deleted} social emails...")

        page_token = response.get('nextPageToken')
        if not page_token:
            break

    print(f"\n✅ DONE. Total social emails deleted: {deleted}")

def main():
    service = get_gmail_service()
    delete_social_emails(service, max_delete=30000)

if __name__ == "__main__":
    main()
