import json
import encoder
from instance_reader import read_instance_from_text


def main():
    instance = read_instance_from_text("Instance2.txt")
    print(json.dumps(instance.staffs, default=encoder.default_method, indent=2))


if __name__ == '__main__':
    main()
