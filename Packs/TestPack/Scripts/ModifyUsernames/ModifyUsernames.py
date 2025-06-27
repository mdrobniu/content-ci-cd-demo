import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401
from typing import Dict, Any
import traceback
import re


def modify(args: Dict[str, Any]) -> CommandResults:
    # usernames = argToList(args.get('usernames'))
    username = args.get("value")
    client_domain = args.get("client_domain")
    pattern = r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$'
    output = []
    match_result = re.match(pattern, username)
    if match_result:
        return username
    else:
        return username + "@" + client_domain


def main():
    try:
        demisto.results(modify(demisto.args()))
        # return_results(modify(demisto.args()))
        # return_results(modify(demisto.args()))
    except Exception as ex:
        demisto.error(traceback.format_exc())  # print the traceback
        return_error(f'Failed to execute script. Error: {traceback.format_exc()}')


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()

