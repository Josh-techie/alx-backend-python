import time
import asyncio


async def brewCoffee():
    print('Coffe is brewing....')
    await asyncio.sleep(3)
    print('Coffe brewed.')
    return 'Coffe is now ready!'

async def toastBagel():
    print('Start toastBagel...')
    await asyncio.sleep(2)
    print('End toastBagel')
    return 'Bagel toasted!'


async def main():
    start_time = time.time()
    
    # batch = asyncio.gather(brewCoffee(), toastBagel())
    # result_coffe_fct, result_bagel_time = await batch
    
    coffe_task = asyncio.create_task(brewCoffee())
    toast_task = asyncio.create_task(toastBagel())
    
    result_coffe_fct = await coffe_task
    result_bagel_time = await toast_task
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Result of brewing coffe: {result_coffe_fct}")
    print(f"Result of toast Bagel : {result_bagel_time}")
    print(f"Total execution time : {elapsed_time: .2f} seconds ")

if __name__ == "__main__":
    asyncio.run(main())
        
    