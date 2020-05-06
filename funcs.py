import requests
import shutil

def iterate(maximum): 
    blank = None

    for i in range(maximum): 
        # This is the image url.
        image_url = ("https://imagebank.illuminateed.com/imagebank/" + str(i))
        # Open the url image, set stream to True, this will return the stream content.
        resp = requests.get(image_url, stream=True)

        # Open a local file with wb ( write binary ) permission.

        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        resp.raw.decode_content = True

        # Copy the response stream raw data to local image file. 

        if blank is None: 
            blank = resp.content
        elif resp.content != blank: 
            with open((f'{i}.jpg'), 'wb+') as local_file: 
                #print(resp.content)  

                #shutil.copyfileobj(resp.raw, local_file) 

                local_file.write(resp.content) 