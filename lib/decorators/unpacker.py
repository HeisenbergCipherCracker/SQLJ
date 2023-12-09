# import asyncio
# import sys
# import os

# current_directory = os.getcwd()
# sys.path.append(current_directory)

# from SQLJngUI import Argument_parser

# def unpack_coroutine_result(func):
#     def wrapper(*args, **kwargs):
#         result = asyncio.run(func(*args, **kwargs))
#         return result
#     return wrapper

# # Usage example
# @unpack_coroutine_result
# async def unpacker():
#     res = await Argument_parser()
#     return res

# result = unpacker()
# print(result)
