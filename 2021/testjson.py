 
 
import json 

from tqdm import tqdm 
import time 



ANIME_NAME = ["TEst",'tmep',"kik",'sfds','dddd']
for i in tqdm (range (101), desc="Loading…", ascii=False, ncols=75):         
    time.sleep(0.01)

    with open("data1.json", "w") as txt_file:
        txt_file.write(" ".join('['))
            
    # read file
    # with open('data1.json', 'r') as myfile:
    #     data1=myfile.read()
    # obj = json.loads(data1)
    # print(str(obj['Aid']))

    for x in range(5):

        # example dictionary to save as JSON
        data = {
            "Aid": x+1,
            "Anime_Name": ANIME_NAME[x],
            "last_name": "Doe",
            "email": "john@doe.com",
            "salary": 1499.9, # just to demonstrate we can use floats as well
            "age": 17,
            "is_real": False, # also booleans!
            "titles": ["The Unknown", "Anonymous"] # also lists!
        }
        
        if x!=0:
            with open("data1.json", "a") as txt_file:
                txt_file.write(" ".join(', '))

        # save JSON file
        with open("data1.json", "a") as f:
            f.write(json.dumps(data, indent=4))


    with open("data1.json", "a") as txt_file:
        txt_file.write(" ".join(']'))



fileHandle = open('data1.json', 'r')
fileHandle.close()
    
print("Complete.")


