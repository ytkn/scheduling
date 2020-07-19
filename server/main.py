import json
import encoder
import solver
import falcon
from instance_reader import read_instance_from_text
from encoder import NdArrayEncoder


class CORSMiddleware:
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header(
            'Access-Control-Allow-Headers',
            'Origin, X-Requested-With, Content-Type, Accept, x-access-token')
        resp.set_header('Access-Control-Allow-Methods',
                        'GET, PUT, POST, DELETE, OPTIONS')


class InstanceResource(object):
    def on_get(self, req, resp, file):
        instance = read_instance_from_text(f"{file}.txt")
        resp.body = json.dumps(
            instance, default=encoder.default_method, indent=2)


class SolutionResource(object):
    def on_get(self, req, resp, file):
        instance = read_instance_from_text(f"{file}.txt")
        solution = solver.solve(instance)
        resp.body = json.dumps(solution, indent=2, cls=NdArrayEncoder)


def main():
    from wsgiref import simple_server
    app = falcon.API(middleware=[CORSMiddleware()])
    app.add_route("/instances/{file}", InstanceResource())
    app.add_route("/instances/{file}/solution", SolutionResource())
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
    # instance=read_instance_from_text("Instance2.txt")
    # ans=solver.solve(instance)
    # print(json.dumps(instance, default=encoder.default_method, indent=2))
    # print(ans)


if __name__ == '__main__':
    main()
