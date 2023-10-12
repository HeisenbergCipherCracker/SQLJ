import re
import asyncio

auth_bypass_list_ls = []
generic_union_ls = []
generic_sql_inj_ls = []
generic_error_ls = []
time_based_sql_ls = []

async def auth_bypasses():
    with open(r"D:\SQLjj\SQLJ\payloads\authBypass.txt", "r") as file:
        contents = file.read()
        strings = re.findall(r"'([^']*)'", contents)
        auth_bypass_list_ls.extend(strings)

    return auth_bypass_list_ls

# Call the async function and print the result
# print(asyncio.run(auth_bypasses()))

async def generic_union_inj():
    with open(r"D:\SQLjj\SQLJ\payloads\Generic_union_sqlinj.txt", "r") as file:
        contents = file.read()
        strings = re.findall(r"'([^']*)'", contents)
        generic_union_ls.extend(strings)

    return generic_union_ls

async def generic_sql_inj():
    with open(r"D:\SQLjj\SQLJ\payloads\generic_sql_ijc.txt", "r") as file:
        contents = file.read()
        strings = re.findall(r"'([^']*)'", contents)
        generic_sql_inj_ls.extend(strings)

    return generic_sql_inj_ls

async def generic_error_based():
    with open(r"D:\SQLjj\SQLJ\payloads\generic_error_based.txt", "r") as file:
        contents = file.read()
        strings = re.findall(r"'([^']*)'", contents)
        generic_error_ls.extend(strings)

    return generic_error_ls

async def time_based_sql():
    with open(r"D:\SQLjj\SQLJ\payloads\time_based_sql.txt", "r") as file:
        contents = file.read()
        strings = re.findall(r"'([^']*)'", contents)
        time_based_sql_ls.extend(strings)

    return time_based_sql_ls

async def main():
    await auth_bypasses()
    await generic_union_inj()
    await generic_sql_inj()
    await generic_error_based()
    await time_based_sql()

asyncio.run(main())