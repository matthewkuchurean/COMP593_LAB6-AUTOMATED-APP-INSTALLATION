import hashlib, requests 

#URL for the HASH file 
hash_request_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.exe.sha256'
def main():

#Using Requests to Download Files 
    
   # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
#send get message to download file 

        hash_resp_msg = requests.get(hash_request_url)
    # Check if the request was successful 
        if hash_resp_msg.status_code == requests.codes.ok:

    #extract file from content 
         file_hash = hash_resp_msg.text 
         file_content = file_hash.split()
               
        return file_content[0]

def download_installer():
     # Send Get message from the download file 
    hash_resp_msg = requests.get(hash_request_url) 

    if hash_resp_msg.status_code == requests.codes.ok: 
        file_content = hash_resp_msg.content

     
        return file_content
 
def installer_ok(installer_data, expected_sha256):
    image_hash = hashlib.sha256(installer_data).hexdigest()
    print(image_hash)
   
    
    return 

def save_installer(installer_data):
    return

def run_installer(installer_path):
    return
    
def delete_installer(installer_path):
    return

if __name__ == '__main__':
    main()