import json
import encoder
import solver
from instance_reader import read_instance_from_text


def main():
    instance = read_instance_from_text("Instance2.txt")
    ans = solver.solve(instance)
    # print(json.dumps(instance, default=encoder.default_method, indent=2))
    print(ans)


if __name__ == '__main__':
    main()
