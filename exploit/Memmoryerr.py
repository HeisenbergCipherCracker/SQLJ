import psutil
import asyncio


async def Memory_handling():
    # Get the system memory information
    memory = psutil.virtual_memory()

    # Calculate the threshold for 80% memory usage
    threshold = memory.total * 0.9

    # Check if the used memory is greater than the threshold
    Err =  memory.used <= threshold
    while not Err:
        memory = psutil.virtual_memory()
        Err = memory.used <= threshold
        print("Please Release you RAM space to continue the application")
        await asyncio.sleep(5)
# asyncio.run(Memory_handling())