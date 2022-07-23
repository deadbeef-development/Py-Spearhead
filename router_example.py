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