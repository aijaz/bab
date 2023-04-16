import logging

# def add(*numbers):
#     print(numbers)
#     return sum(numbers)
#
#
# total = add(1, 2)
# print(total)
#
# total = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 1, 1, 4)
# print(total)
#
# odds = (1, 3, 5, 7, 9, 11, 13)
# total = add(*odds)
# # as if you had typed in total = add(1, 3, 5, 7, 9, 11, 13) and not add((1, 3, 5, 7, 9, 11, 13),)
#
# def agenda(**items):
#     if items.get('read') is not None:
#         print(f"I wish to read {items['read']}")
#     if items.get('eat') is not None:
#         print(f"I wish to eat {items['eat']}")
#     if items.get('play') is not None:
#         print(f"I wish to play {items['play']}")
#     if items.get('drink') is not None:
#         print(f"I wish to drink {items['drink']}")
#
# # items.get('abc') is just like items['abc'] EXCEPT if items does not contain 'abc' as a key
# # in that case it returns None, instead of throwing a KeyError and crashing your app
#
# plan = { "eat": "Bhel Puri", "read": "The Qur'an", "drink": "milk"}
# agenda(**plan)
#
import logging

logging.basicConfig(filename='app.log',
                    filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logging.debug('dd')
logging.info('ii')
logging.warning('ww')
logging.error('ee')
logging.critical('cc')



