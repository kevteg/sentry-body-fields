# sentry-body-fields
This script will download a specific field or list of fields for every event body of an issue as a csv

## Usage

`python get_events_body_fields.py <issue_id> <auth_token> <field_1> <field_2>`

## What will you get?
A csv file with <field_1> and <field_2> of all events for given issue_id

## Why?
The other day I had to recover an specific field of all the body events of an issue I had at work... and this could definitely happen again (Let's hope it doesn't)
