"""
Define the Dancer class. It should include the dance() method.
Calling this method a loop that prints out the name of the dancer
together with the 'is dancing' text should execute 20 iterations.
Create a list of 20 Dancer objects and simulate a scenario in which
at any given time there no more than 3 dancers dancing in our club.
Use the Semaphor class to ensure that.
"""
import threading
import time


def dance(text, sema):
    sema.acquire()
    i = 1
    while i < 20:
        print(threading.current_thread().getName(), text, "is dancing")
        time.sleep(1)
        i += 1
    sema.release()


semaphore = threading.Semaphore(3)
number_of_threads = 20
for dancer_name in [
    'Dancer1', 'Dancer2', 'Dancer3', 'Dancer4', 'Dancer5',
    'Dancer6', 'Dancer7', 'Dancer8', 'Dancer9', 'Dancer10',
    'Dancer11', 'Dancer12', 'Dancer13', 'Dancer14', 'Dancer15',
    'Dancer16', 'Dancer17', 'Dancer18', 'Dancer19', 'Dancer20'
]:
    thread = threading.Thread(target=dance, args=(dancer_name, semaphore))
    thread.name = ''
    thread.start()
