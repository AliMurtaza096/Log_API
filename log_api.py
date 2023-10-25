import requests
import uuid

def get_mac_address():
    # Get the MAC address of the machine
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    return mac
def send_file_to_server(file_path, api_url,mac_address):
    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Create a dictionary of files to send
        files = {'file': file}
         # Send the POST request with the file and MAC address as data
        data = {'macAddress': mac_address,
                'botName': "<Replace Bot Name here>",
                'version':"<Replace Version number here>"}
        # Send the POST request with the file
        response = requests.post(api_url,data=data, files=files)

        # Check if the request was successful
        if response.status_code == 200:
            print("File uploaded successfully.")
        else:
            print(f"Failed to upload the file. Status code: {response.status_code}")
            print(response.text)

if __name__ == "__main__":
    # Replace the below Path with your file path
    FILE_PATH = "/home/ali/Desktop/ML-Bot/requirements.txt"
    # Replace the Backend API below with actual API
    API_URL = "http://localhost:3000/upload"
    MAC_ADDRESS = get_mac_address()

    send_file_to_server(FILE_PATH, API_URL, MAC_ADDRESS)