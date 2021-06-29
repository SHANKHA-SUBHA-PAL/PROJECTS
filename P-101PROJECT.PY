import dropbox
import os

from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx =dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)


        with open(local_path, 'rb') as f :
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'vm-etNZDT8EAAAAAAAAAAaX8y5UX8nMlVUPTrYTg8522BC_ehqxPTUTe3sAsaIDM'
    transferData = TransferData(access_token)

    file_from = '/Projects/SampleText1.txt'
    file_to = '/Projects For P-101/SampleText1.txt'

    transferData.upload_file(file_from, file_to)

main()