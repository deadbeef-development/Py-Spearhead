import typing

class SplitRouter:
    __getroute = lambda _, val: val

    def __init__(self, match_case=False):
        self.__routes = dict()

        if match_case:
            self.__getroute = str.lower
    
    def split(self, cmd:str) -> typing.List[str]:
        return cmd.split(' ')

    async def __call__(self, cmd:str) -> str:
        args = self.split(cmd)

        if len(args) > 0:
            route_name = self.__getroute(args[0])

            if route_name in self.__routes:
                func = self.__routes[route_name]
                return await func(args[1:])
            else:
                return ''
        else:
            return ''
    
    def route(
        self, 
        func:typing.Callable[[typing.List[str]], typing.Awaitable[str]]
    ):
        route_name = self.__getroute(func.__name__)
        self.__routes[route_name] = func
        return func
    
