# Gmail Cleanup Automation

A Python tool that helps you clean up your Gmail inbox efficiently by deleting emails in bulk from **Promotions** and **Social** tabs using the Gmail API.

## Features
- Delete emails from Promotions or Social tabs
- Handles thousands of emails safely using Gmail API batch operations
- Uses OAuth 2.0 for secure authentication
- Configurable maximum number of emails to delete

## Setup

1. Create a project in Google Cloud Console
2. Enable Gmail API
3. Create OAuth 2.0 credentials (`credentials.json`)
4. Place `credentials.json` in the project folder

## Install Dependencies

```bash
pip install -r requirements.txt

