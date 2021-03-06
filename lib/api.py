import requests 
import json
import webbrowser
import datetime

# API KEY
API_KEY = '2lUw74KdgFjcPNvuiMWQ9DIBo6jZtSUkwU5x9sUW'

# API URL
url = 'https://api.nasa.gov/planetary/apod?api_key=2lUw74KdgFjcPNvuiMWQ9DIBo6jZtSUkwU5x9sUW'


#Realtime date and time
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")


#Parameters:

params={
    'date': date,
    'hd': True,
    'api_key': API_KEY

}
def file(data):
    with open(r"C:\Users\Yonna\Documents\GitHub\star-project\assets\api.json", 'w+') as api_data: 
        str(json.dump(data,api_data)) 


def main():
    response = requests.get(url, params=params) # Asking for data from APOD API
    json_data = json.loads(response.text) # Saving the ata
    file(json_data) # Adding to file
    #img_url = json_data['hdurl']
    #webbrowser.open(img_url)
    


if __name__ == "__main__":
    main()
    


if __name__ == "__main__":
    main()
