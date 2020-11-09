import sys
import time
import inspect

from bot import Bot


if sys.stdout.encoding == 'cp1251':
    sys.stdout.reconfigure(encoding='utf-8')


bot = Bot('Вадим')

was_repeat_call = None

def response_logic(response):
    global was_repeat_call
    if response is None and was_repeat_call is None:
        response = bot.hello_null()
        was_repeat_call = response is None
    if response is None and was_repeat_call:
        bot.hangup_null()
        return

    response = response.lower().strip()
    if response == 'да':
        bot.recommend_main(confirm=True)
    elif response == 'нет':
        bot.hangup_wrong_time(confirm=False)
    elif response == 'занят':
        bot.hangup_wrong_time(wrong_time=True)
    elif response == 'еще раз':
        hello_repeat = bot.hello_repeat(repeat=True)
        response_logic(hello_repeat)
    else:   # default
        bot.recommend_main()



first_call = bot.say_hello()
response_logic(first_call)

# in: hello; out: null; control to func bot.hello_null or bot.hangup_null


# start = time.time()
# waiting = time.sleep(5)
# not_answer = time.time() - start > 5                                 # здесь делить поток

# if say_hello and was_repeat_call is None:
#     print('metka 1')
#     hello_null = bot.hello_null()
#     print('metka 3')
#     was_repeat_call = response_logic(hello_null.lower())
# if say_hello and was_repeat_call:
#     bot.hangup_null()



    # name = 'Gakik'
    # response = bot.say_hello(name)
    # if response is None:
    #     if session_with_user == 1:
    #         bot.hello_null()
    #         session_with_user += 1
    #         return

    # elif 'Yes' in response:
    #     bot.hello_repeat(repeat=False)
    #     bot.recommend_main(confirm=True)
    # elif 'No' in response:
    #     bot.hello_repeat(repeat=False)
    #     bot.hangup_wrong_time(confirm=False)
    #     return    
    # elif 'Not now' in response:
    #     bot.hello_repeat(repeat=False)
    #     bot.hangup_wrong_time(wrong_time=True)
    #     return  
    # elif 'again' in response:
    #     bot.hello_repeat(repeat=True)
    # else:
    #     bot.recommend_main()
    #     return



# from flask import Flask
# from flask import request
# from flask import jsonify

# import requests


# app = Flask(__name__)

# @app('/', methd=['POST', 'GET'])
# def main():
#     bot = Bot()
#     if not session_with_user:
#         bot.hello(name)
    
#     if request.method == 'POST':
#         r = request.get_json()
#         global u_msg
#         u_msg = r['p']['a']['r']['s']['e']

#         if u_msg is None:
#             bot.hello_repeat()
#         server.lisen()
#     return


# if __name__ == '__main__':
#     main(host, post, ...)