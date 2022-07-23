import typing
import asyncio

class NewlineException(Exception):
  def __init__(self):
    super().__init__('Command results cannot contain newline characters')

def run(
  handle_cmd:typing.Callable[[str], typing.Awaitable[str]], 
  host:str, 
  port:int,
  loop:asyncio.AbstractEventLoop=None
):
  if loop is None:
    loop = asyncio.get_event_loop()
  
  async def handle_client(reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
    while True:
      data = await reader.readline()
    
      if data:
        try:
          cmd = data.strip().decode()

          result:str = (await handle_cmd(cmd))
          
          if '\n' in result:
            raise NewlineException
        except:
          writer.close()
          raise

        writer.write(result.encode())
        writer.write(b'\n')
      else:
        break
  
  async def run():
    server = await asyncio.start_server(handle_client, host, port, loop=loop)

    await server.wait_closed()
  
  loop.run_until_complete(run())