import glob
import json
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def authenticate_google_drive():
    # Initialize GoogleAuth
    gauth = GoogleAuth()

    # Load credentials from GOOGLE_CREDENTIALS environment variable
    google_credentials = os.getenv("MY_GOOGLE_CREDENTIALS")
    if google_credentials:
        # Load the credentials from a JSON string
        creds_json = json.loads(google_credentials)
        gauth.credentials = GoogleAuth().credentials_from_dict(creds_json)
    else:
        print("The MY_GOOGLE_CREDENTIALS environment variable is not set.")
        exit(1)

    return GoogleDrive(gauth)


def upload_files(drive):
    # Fetch the Google Drive folder ID from the environment variable
    folder_id = os.getenv("MY_GOOGLE_DRIVE_FOLDER")
    if not folder_id:
        print("The MY_GOOGLE_DRIVE_FOLDER environment variable is not set.")
        exit(1)

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

        # Delete the file after successful upload
        os.remove(file_path)
        print(f"Deleted {file_path} from local filesystem after successful upload.")


def main():
    drive = authenticate_google_drive()

    upload_files(drive)


if __name__ == '__main__':
    main()
