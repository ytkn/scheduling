import json
import encoder
import solver
import falcon
from instance_reader import read_instance_from_text, list_instances
from solution_reader import read_solution_from_xml, list_solutions
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


class InstanceListResource(object):
    def on_get(self, req, resp):
        instances = [i.replace(".txt", "") for i in list_instances()]
        resp.body = json.dumps(instances, indent=2)


class SolutionResource(object):
    def on_get(self, req, resp, file, solution_name):
        instance = read_instance_from_text(f"{file}.txt")
        solution = solver.solve(instance) if solution_name == 'solver' else read_solution_from_xml(
            solution_name, instance)
        resp.body = json.dumps(solution, indent=2, cls=NdArrayEncoder)


class SolutionListResource(object):
    def on_get(self, req, resp, file):
        solutions = list_solutions(file)
        resp.body = json.dumps(solutions, indent=2)


def main():
    from wsgiref import simple_server
    app = falcon.API(middleware=[CORSMiddleware()])

    app.add_route("/instances", InstanceListResource())
    app.add_route("/instances/{file}", InstanceResource())
    app.add_route(
        "/instances/{file}/solutions", SolutionListResource())
    app.add_route(
        "/instances/{file}/solutions/{solution_name}", SolutionResource())
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
