# Import requests, shutil python module.
import os
import funcs

from constants import * 

mode = input('enter the mode (r to delete images, w to download images): ').lower() 

print('e') 

if mode == 'r': 
    for path in os.listdir(directory): 
        name, *ext = path.split('.') 

        if ext and ext[0] == 'jpg': 
            os.remove(f'{directory}{path}') 

elif mode == 'w': 
    overwrite = input('enter something to allow overwrite, nothing to not overwrite: ') 

    funcs.iterate(minimum, maximum, every, directory, overwrite) 

    '''
    for i in range(maximum): 
    # This is the image url.
        image_url = ("https://imagebank.illuminateed.com/imagebank/" + str(i))
        # Open the url image, set stream to True, this will return the stream content.
        resp = requests.get(image_url, stream=True)

        # Open a local file with wb ( write binary ) permission.
        local_file = open((str(i)+'.jpg'), 'wb+')

        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        resp.raw.decode_content = True

        # Copy the response stream raw data to local image file.
        shutil.copyfileobj(resp.raw, local_file)

        # Remove the image url response object.
        del resp
        
        #if blank == open((str(i)+'.jpg'), 'rb').read():
        #   os.remove((str(i)+".jpg"))
        #print(blank != open((str(i)+'.jpg'), 'rb').read(), i)

        try:
            Image.open((str(i)+'.jpg'))
        except:
            os.remove((str(i)+".jpg")) 
    ''' 