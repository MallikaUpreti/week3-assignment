#Write a Python program using asyncio that performs the following:
#● Define an asynchronous coroutine print_numbers() that prints numbers from 1 to 5, waiting 1 second between each print.
#● Define another asynchronous coroutine print_letters() that prints letters from 'A' to 'E', waiting 1.5 seconds between each print.
#● In the main() coroutine, run both print_numbers() and print_letters() concurrently using asyncio.gather().
#● Measure and print the total time taken to complete both tasks.

import asyncio        # Importing the asyncio module for asynchronous programming
import time           # Importing time module to measure how long the program takes 

# Coroutine to print numbers 1–5 with a1-second pause
async def print_numbers():
    for i in range(1, 6):     # Loop from 1 to 5
        print(i)              # Print the current number
        await asyncio.sleep(1)  # Pause for 1 second 

#  Coroutine to print letters A–E with a 1.5-second pause
async def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:  # Loop through the letters
        print(letter)                         # Printing letter
        await asyncio.sleep(1.5)              # Pause for 1.5 seconds

#  Main coroutine to run both tasks together and measure time
async def main():
    start_time = time.time()     # Recording the time that starts

    # asyncio.gather runs both coroutines at the same time
    await asyncio.gather(
        print_numbers(),         #  print the First task
        print_letters()          # print the Second task
    )

    end_time = time.time()       # Record the end time
    total = end_time - start_time  # Calculating  how long the program took

    print(f"Total time taken: {total:.2f} seconds")  # Display total time

# Starts the event loop and runs the main() coroutine
asyncio.run(main())
