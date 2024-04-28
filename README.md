# PyCord :snake:

`PyCord` is a client for [Discord Gateway](https://discord.com/developers/docs/topics/gateway), written in Python.

Connection to gateway is established through WebSockets.

This client is compatible with Python 3.

# Documentation
To start using `PyCord`:
* Go to [Discord Applications](https://discord.com/developers/applications).
* Copy bot token and place it in `.env` configuration file.
* Start the client by running: `python3 start.py`.
* Client will establish WebSocket connection to Discord Gateway.

# Implementation progress
> [!IMPORTANT]
> Currently `PyCord` only connects and receives events from Discord server.
> 
> Handling of disconnect is implemented. `PyCord` will automatically resume connection.
> 
> More features will be added in future.
