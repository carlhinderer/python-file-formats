import sys
sys.path.append('gen-py')

from hello import HelloSvc

from thrift.transport import TSocket           # Endpoint for clients to connect to
from thrift.transport import TTransport        # Provides a buffering layer
from thrift.protocol import TBinaryProtocol    # Handles data serialization
from thrift.server import TServer              # Gives us access to prebuilt server classes


class HelloHandler:
    def hello_func(self):
        print("[Server] Handling client request...")
        return "Hello from the Python server"


handler = HelloHandler()
proc = HelloSvc.Processor(handler)

trans_svr = TSocker.TServerSocket(port=9090)
trans_fac = TTransport.TBufferedTransportFactory()
proto_fac = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(proc, trans_svr, trans_fac, proto_fac)
server.serve()
