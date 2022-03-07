import argparse
import logging


def main():
    parser = argparse.ArgumentParser(description="run your cli")
    parser.add_argument("-n", "--name", type=str,help="Your name")
    parser.add_argument("-b", "--birth", type=str,help="Your birthday")
    parser.add_argument("-m", "--manufacturer", type=str, nargs="+",
                        help="Manufacturer", choices=["Avdor", "Simbionix", "Verint"])

    args = parser.parse_args()


    print(args)
    pass


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.exception(e)
