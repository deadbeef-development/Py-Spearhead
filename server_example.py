import spearhead

async def echo(cmd:str):
    return cmd

spearhead.run(echo, '127.0.0.1', 1234)