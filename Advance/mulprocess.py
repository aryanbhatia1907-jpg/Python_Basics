import multiprocessing
import concurrent.futures
import requests 

def downloadfile(url, name):
    print(f"Started Downloading{name}")
    response=requests.get(url)
    open(f"file{name}.jpg","wb").write(response.content)
    print(f"Finished Downloading{name}")

if __name__ == "__main__":                      # Special in Vs Code only
    url= "https://picsum.photos/2000/3000"
#     pros=[]
#     for i in range (5):
#         # downloadfile(url,i)
#         p=multiprocessing.Process(target=downloadfile, args=[url,i])
#         p.start()
#         pros.append(p)

#     for p in pros:
#         p.join()


# Advance modules
if __name__ == "__main__":                      # Special in Vs Code only
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(6)]
        l2 = [i for i in range(6)]
        results = executor.map(downloadfile, l1, l2)
        for r in results:
            print(r)