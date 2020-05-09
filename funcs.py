import os
import requests
import shutil
import threading

from logging_stuff import debug

class LoggingThread(threading.Thread): 
    selves = [] 

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 

        self.selves.append(self) 
    
    def run(self):
        super().run() 

        self.selves.remove(self) 

        debug(f'thread done, {len(self.selves)} left') 

def get_blank(timeout, blank=0): 
    # This is the image url.
    image_url = f"https://imagebank.illuminateed.com/imagebank/{blank}"
    # Open the url image, set stream to True, this will return the stream content.

    resp = requests.get(image_url, timeout=timeout, stream=True) 
    # Open a local file with wb ( write binary ) permission.

    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True

    # Copy the response stream raw data to local image file. 

    return resp.content

def search(blank, to_search, timeout, directory, overwrite): 
    for i in to_search: 
        path = f'{directory}{i}.jpg'; 

        if overwrite or not os.path.exists(path): 
            #debug(path) 

            # This is the image url.
            image_url = ("https://imagebank.illuminateed.com/imagebank/" + str(i))
            # Open the url image, set stream to True, this will return the stream content.
            try: 
                resp = requests.get(image_url, timeout=timeout, stream=True) 
            except requests.ConnectionError: 
                debug(f'error on number {i}') 
            except requests.Timeout: 
                debug(f'timeout on number {i}') 
            else: 
                # Open a local file with wb ( write binary ) permission.

                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                resp.raw.decode_content = True

                # Copy the response stream raw data to local image file. 

                if resp.content != blank: 
                    with open(path, 'wb+') as local_file: 
                        #debug(resp.content)  

                        #shutil.copyfileobj(resp.raw, local_file) 

                        local_file.write(resp.content) 

def iterate(minimum, maximum, every, timeout, directory, overwrite): 
    blank = get_blank(timeout) 

    for i in range(minimum, maximum, every): 
        start = i
        end = min(i + every, maximum) 

        to_search = range(start, end) 

        t = LoggingThread(target=search, args=(blank, to_search, timeout, directory, overwrite)) 

        try: 
            t.start() 
        except RuntimeError: 
            debug(threading.active_count()) 

            raise

    debug('all threads started') 

    [t.join() for t in LoggingThread.selves] 

    debug('all threads finished') 