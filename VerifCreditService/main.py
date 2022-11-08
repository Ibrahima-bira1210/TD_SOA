from spyne import rpc, ServiceBase, Iterable, Unicode, Integer, Application,Boolean
from spyne.protocol.http import HttpRpc
from spyne.protocol.soap import Soap11

from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted


class VerifCreditService(ServiceBase):
    @rpc(Unicode, _returns=Boolean)
    def is_solvable(ctx, ssn):
        string = str(ssn)
        return string.startswith('6')


application = Application([VerifCreditService],
                          tns='spyne.examples.verifCreditService',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11()
                          )
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8084, wsgi_app)
    print("Server running on http://localhost:8084")
    server.serve_forever()

# validator='lxml' to validate xml
