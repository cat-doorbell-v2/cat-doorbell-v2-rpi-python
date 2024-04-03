import glob
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def authenticate_google_drive():
    # Initialize GoogleAuth and load saved credentials
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("mycreds.txt")

    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")

    return GoogleDrive(gauth)


def upload_files(drive, folder_id):
    # List all .wav files in the /tmp directory
    for file_path in glob.glob('/tmp/*.wav'):
        # Create a file on Drive, set its parents to the given folder
        file_drive = drive.CreateFile({
            'title': os.path.basename(file_path),
            'parents': [{'id': folder_id}]
        })
        file_drive.SetContentFile(file_path)
        file_drive.Upload()
        print(f"Uploaded {file_path} to Google Drive with ID {file_drive['id']}")


def main():
    drive = authenticate_google_drive()

    # Specify your Google Drive folder ID here
    folder_id = '14nSUAluXcdfyGTU15OAoVCBLHzYdn5i3'

    upload_files(drive, folder_id)


if __name__ == '__main__':
    main()
