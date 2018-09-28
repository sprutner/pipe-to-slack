#!/usr/bin/env python3

import sys
from slackclient import SlackClient
from python_terraform import *
import os
import argparse

def parse_stdin(input):
    lines = []
    for line in input:
        # sys.stderr.write("DEBUG: got line: " + line)
        # sys.stdout.write(line)
        lines.append(line)
    return ''.join(lines)

def upload_snippet(slack_channel, snippet, comment, title):
    sc.api_call(
        "files.upload",
        channels=slack_channel,
        file=snippet,
        title=title,
        initial_comment=comment
    )

def parse_arguments(help=False):
    #argpase init
    parser = argparse.ArgumentParser('pipe-to-slack')
    parser.add_argument('--comment', '-c', required=True, nargs='+')
    parser.add_argument('--title', '-t', required=True, nargs='+')
    result, unknown = parser.parse_known_args()
    if help == True:
        return parser.print_help(sys.stderr)
    else:
        return result


if __name__ == "__main__":
    # INIT
    args = parse_arguments()
    comment = ' '.join(args.comment)
    title = ' '.join(args.title)

    slack_token = os.environ["SLACK_API_TOKEN"]
    slack_channel = os.environ["SLACK_CHANNEL"]
    sc = SlackClient(slack_token)
    snippet = parse_stdin(sys.stdin)
    upload_snippet(slack_channel, snippet, comment, title)
