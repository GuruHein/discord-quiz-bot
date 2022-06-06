import discord
import asyncio
import requests

client = discord.Client()

def get_question():
    question = ""
    answer = 0  
    response = requests.get('http://127.0.0.1:8000/questions/random')
    data = response.json()
    question += f"Question: {data['title']}\n"

    for i, item in enumerate(data['answers']):
        question += f"{i+1}. {item['answer']}\n" 

        if item['is_correct']:
            answer = i
    return question, answer

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!question'):
        question, answer = get_question()
        await message.channel.send(question)

        def check(m):
            return m.author == message.author and m.channel == message.channel and m.content.isdigit()

        try:
            guess = await client.wait_for('message', check=check, timeout=5.0)
            if int(guess.content) == answer:
                await message.channel.send(f"{message.author}, you are correct!")
            else:
                await message.channel.send(f"{message.author}, you are stupid. You don't know the answer.")

        except asyncio.TimeoutError:
            return await message.channel.send(f"{message.author}, you took too long. Try again.")

    

client.run('OTgzMzA5OTY3ODExNTUxMjYy.GPIhxW.-R_gvqA4pwVxyNPa2M8hJllJ1xY8t_PFVHQitU')