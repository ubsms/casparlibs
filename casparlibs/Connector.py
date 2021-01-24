from amcp_pylib.core import Client
from amcp_pylib.module.query import VERSION
import logging

client = None

def init(ip="127.0.0.1", port=5250):
    logging.info("Connecting")
    logging.debug("{}:{}".format(ip, port))
    global client
    if client is None:
        client = Client()
        try:
            client.connect(ip, port)
        except ConnectionRefusedError:
            logging.error("Unable to connect to server. Connection refused")
            exit()

def getConnector():
    global client
    if client is None:
        logging.debug("Connector not initialised, init now")
        init()
    return client