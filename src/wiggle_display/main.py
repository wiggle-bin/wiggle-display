#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

picdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "pic"
)
libdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "lib"
)
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
from wiggle_display.display import EPDText
import requests
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

ENDPOINT = "http://wigglebin.local:5000/sensors"


def main():
    try:
        epd_text = EPDText()

        while True:
            response = requests.get(ENDPOINT)
            data = response.json()

            wiggle_gate_time = datetime.fromisoformat(data["wiggle_gate"]["time"])

            epd_text.display_text(
                [
                    data["bme"]["temperature"],
                    f"Gate {wiggle_gate_time.strftime('%I:%M')}",
                ]
            )
            time.sleep(300)

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        # TODO: need to call epdconfig.module_exit(cleanup=True)
        exit()


if __name__ == "__main__":
    main()
