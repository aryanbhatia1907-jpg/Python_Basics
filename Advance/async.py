import time
import asyncio 
import requests


async def function1():
  URL = "https://www.bing.com/ck/a?!&&p=e11364a4c74ff371d6f21ed3993e3d52dce38d3f5153fd24014d0f485ebaa9ccJmltdHM9MTc3MjA2NDAwMA&ptn=3&ver=2&hsh=4&fclid=15d1a565-becf-63ac-0c79-b321bf3d6237&u=a1L2ltYWdlcy9zZWFyY2g_cT1waWN0dXJlcyZpZD0wRjhBMzU4NzhGMjREQjY2RDY2Rjc1RTZBMUQ1RTMxRjU0OTE3OTE3JkZPUk09SVFGUkJB"
  response = requests.get(URL)
  print("func 1") 
  open("instagram.ico", "wb").write(response.content)
   
  return "func1"
  
async def function2():
  print("func 2") 
  URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram2.jpg", "wb").write(response.content)
  
async def function3():
  print("func 3")
  URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram3.ico", "wb").write(response.content)

async def main():
  # await function1()
  # await function2()
  # await function3()
  # return 3
  L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
  print(L)
  # task = asyncio.create_task(function1())
  # # await function1()
  # await function2()
  # await function3()

asyncio.run(main())