from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



if __name__=='__main__':
    app.run()


#decorator function 

# import time
# current_time = time.time()
# print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

# def speed_calc_decorator(function):
#   def wrapper():
#     start_time=time.time()
#     function()
#     end_time=time.time()
#     print(f'{function.__name__} run speed: {end_time-start_time}')
#   return wrapper  
  
# @speed_calc_decorator
# def fast_function():
#   for i in range(1000000):
#     i * i
        
# @speed_calc_decorator
# def slow_function():
#   for i in range(10000000):
#     i * i


# call=speed_calc_decorator(fast_function)
# call()
# slow_function() 