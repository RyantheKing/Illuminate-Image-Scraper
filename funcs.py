import requests
import shutil
import threading

blank = None

class CallbackThread(threading.Thread): 
    def __init__(self, callback, *args, **kwargs): 
        super().__init__(*args, **kwargs) 

        self.callback = callback
    
    def join(self): 
        super().join() 

        self.callback() 

def search(to_search, directory): 
    global blank

    for i in to_search: 
        # This is the image url.
        image_url = ("https://imagebank.illuminateed.com/imagebank/" + str(i))
        # Open the url image, set stream to True, this will return the stream content.
        try: 
            resp = requests.get(image_url, stream=True) 
        except requests.ConnectionError: 
            print(f'error on number {i}') 
        else: 
            # Open a local file with wb ( write binary ) permission.

            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            resp.raw.decode_content = True

            # Copy the response stream raw data to local image file. 

            if blank is None: 
                blank = resp.content
            elif resp.content != blank: 
                with open((f'{directory}{i}.jpg'), 'wb+') as local_file: 
                    #print(resp.content)  

                    #shutil.copyfileobj(resp.raw, local_file) 

                    local_file.write(resp.content) 

threads = [] 

def iterate(minimum, maximum, every, directory): 
    global blank

    threads.clear() 

    blank = None

    search((0,), directory) 

    for i in range(minimum, maximum, every): 
        start = i
        end = min(i + every, maximum) 

        to_search = range(start, end) 

        t = CallbackThread(lambda: print(f'thread done, now waiting on {threading.active_count()} others'), target=search, args=(to_search, directory)) 

        threads.append(t) 

        try: 
            t.start() 
        except RuntimeError: 
            print(threading.active_count()) 

            raise

    print('all threads started') 

    [t.join() for t in threads] 

    print('all threads finished') 