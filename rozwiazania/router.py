from typing import Callable, Optional

def create_router():
    
    routes: dict[str, Callable] = {}

    def route_handler(method: str, path: str, handler: Optional[Callable] = None):
        if method == "add":
            routes[path] = handler
            return f"Route {path} added"
        elif method == "get":
            if path in routes:
                return routes[path]()
            else:
                return "404: Not found" 
        else:
            return "Invalid method: Use 'add' or 'get'"
        
    return route_handler
