# Pipe your output into a slack channel of your choosing

## Requirements

- Slack API key
- Python3

## Installation

  #### Clone and install dependencies
  `git clone https://github.com/sprutner/pipe-to-slack`
  `pip3 install -r requirements.txt`

  #### Set ENV Vars
  You must set the following environment variables in your bash_profile
  ```
  export SLACK_CHANNEL=server
  export SLACK_API_TOKEN=<slack_api_token>
  ```

  #### Set aliases
  I set these up for ease of use, just drop them in your bash_profile and point them to wherever this script is located

  ```
  alias slack='~/pipe-to-slack/server-slack.py'
  alias skd='slack -t Knife Diff'
  ```

## Usage

`usage: slack-diff [-h] --comment [-c] COMMENT --title [-t] TITLE`

If you followed the alias setup above, you should be able to just do:

```knife diff | slack -t knife diff -c increasing number of jellyfish instances...```

And if you alias the alias like above you can just do:

```knife diff | slack -c increasing number of jellyfish instances...```

## TODO / Issues

- You must currently escape the '#' character as it gets interpreted as a comment.
