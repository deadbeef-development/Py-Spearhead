# Description
Spearhead is a simple protocol for inter-process communication. It is not designed to be secure, and it should only be used locally behind a firewall.

# Server Example
```python
import spearhead

async def echo(cmd:str):
    return cmd

spearhead.run(echo, '127.0.0.1', 1234)
```

# Server Example with SplitRouter
```python
import spearhead

app = spearhead.SplitRouter()

@app.route
async def foo(args):
    return 'bar'

@app.route
async def bar(args):
    return 'foo'

@app.route
async def oops(args):
    raise Exception("Oops")

spearhead.run(app, '127.0.0.1', 1234)
```