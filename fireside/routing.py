
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)

    # when a connection is made to the Channels development server, 
    # the ProtocolTypeRouter will first inspect the type of connection. 
    # If it is a WebSocket connection (ws:// or wss://), 
    # the connection will be given to the AuthMiddlewareStack.
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
