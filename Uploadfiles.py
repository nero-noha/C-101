import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)

    def upload_file(self, file_from, file_to):
        with open(file_from, "rb") as f:
            self.dbx.files_upload(f.read(), file_to, mode=WriteMode("overwrite"))

def main():
    access_token = "sl.BnHB4raV90emngE04kE2on6zE3iPn0ICiR-Y1TkeSgG-5UqaOqywnVNiat5kBQ0n-8EQ8p5IPtIgh4tOJ6jbN7H0IQBU4oRNT_m81Wg4b4Kynb6CS7FR1t3QSvi-IwMsYdCKeTzkMCct"

    file_from = input("Enter the full path of the file to upload: ")

    file_to = input("Enter the full Dropbox path to upload the file to (including the desired name): ")

    transfer_data = TransferData(access_token)

    transfer_data.upload_file(file_from, file_to)
    print(f"File '{file_from}' has been uploaded to Dropbox as '{file_to}'.")

if __name__ == "__main__":
    main()
