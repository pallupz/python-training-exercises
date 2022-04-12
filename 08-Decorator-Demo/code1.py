# Exercise Name:
# 	08-Decorator-Demo
# Description:
# 	Create a decorator called 'time_this' and use it to measure time taken to run functions

# For example, running:
# 	@time_this
# 	def sleeper_func(sleeptime):
# 	    print(f'sleeping for {sleeptime}')
# 	    sleep(sleeptime)
# 	    return 'Woke up!'

# 	sleeper_func(2)

# Sould output the following in the console:
# 	--> Running sleeper_func
# 	sleeping for 2
# 	--> sleeper_func ran in 2.002105236053467 seconds


from functools import wraps
import time

def time_this(func):
    '''
    this function wraps
    '''
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''
        this function is what really wraps
        '''

        print(f'---> Running {func.__name__}')
        start = time.time()
        func(*args, **kwargs)
        print(f'---> Completed {func.__name__} in {time.time() - start}')
    
    return wrapper

@time_this
def sleeper_func(duration):
    '''
    this function simply sleeps
    '''

    print(f'sleeping for {duration}')
    time.sleep(duration)


print(sleeper_func.__doc__)
sleeper_func(2)