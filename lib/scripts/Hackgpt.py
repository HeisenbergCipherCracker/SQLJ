# import sqlite3

# def display_values():
#     conn = sqlite3.connect("Result.db")
#     cur = conn.cursor()
    
#     cur.execute("SELECT Data, attacktype FROM Datas")
#     rows = cur.fetchall()
    
#     print("Values in the table:")
#     for row in rows:
#         print("Data:", row[0])
#         print("Attack Type:", row[1])
    
#     conn.close()

# display_values()
import openai
openai.api_key = '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'
def chat(prompt,key):
    openai.api_key = key
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        break
    response = chat(user_input)
    print("ChatGPT: " + response)