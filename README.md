# ttl-test

A demo repo illustrating a potential bug in `cachetools.TTLCache`.

See the success and failure of the Github Actions, or run on your own machine.

## Installation

    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
  
## Run test

    python3 ttl_test.py
  
In Ubuntu 20.04, Python 3.7 - 3.9 sometimes the script succeeds and sometimes it fails with an AssertionError.
On Mac 10.15.7, Python 3.8.2 the script succeeds.
