# Banker
Because my wife loves her neopets and I can't stop myself.
It collects interest from the bank.

Ideally, this is running on a cron on a daily basis, to automate
collecting interest.

## Development
`virtualenv env`

`source env/bin/activate`

`pip install -r requirements.txt`

Use latest version of chromedriver and python 3.7


## Usage
`python banker.py --username=MyName --password=Pass`

## Automation
[Here is a Gist for deploying to a cloud instance to automate this
process](https://gist.github.com/joshehlinger/ac1294e7a1a2e494a5196d043312f948)