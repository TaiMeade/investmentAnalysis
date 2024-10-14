import streamlit as st
import morningstar_data as md
import os
import pandas as pd
import requests
import json
# from xbrl import XBRLParser

# os.environ['MD_AUTH_TOKEN'] = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1EY3hOemRHTnpGRFJrSTRPRGswTmtaRU1FSkdOekl5TXpORFJrUTROemd6TWtOR016bEdOdyJ9.eyJodHRwczovL21vcm5pbmdzdGFyLmNvbS9lbWFpbCI6ImludmVzdEByYWRmb3JkLmVkdSIsImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL3JvbGUiOlsiUGVyc29uYS5EaXJlY3RGb3JBc3NldE1hbmFnZW1lbnQiLCJFbmFibGVkIEFuYWx5dGljcyBMYWIgRGVsaXZlcnkgTm90ZWJvb2tzIiwiRGlzYWJsZSBEZWZpbmVkIENvbnRyaWJ1dGlvbiBQbGFucyIsIlBvcnRmb2xpbyBBbmFseXNpcyBVc2VyIl0sImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL2NvbXBhbnlfaWQiOiIxMWZjMjA1MC01YmFhLTQzOTYtODI3ZS0xNzRlNzk4MDJlODkiLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS9pbnRlcm5hbF9jb21wYW55X2lkIjoiQ2xpZW50MCIsImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL2RhdGFfcm9sZSI6W10sImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL2xlZ2FjeV9jb21wYW55X2lkIjoiMTFmYzIwNTAtNWJhYS00Mzk2LTgyN2UtMTc0ZTc5ODAyZTg5IiwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vcm9sZV9pZCI6WyI3OGJhMWFlNy0xZWUzLTQ0YTAtYTAxOC0wOGM1NThmZWNmMTciLCI4MjYyOWNkMC1kZjgwLTRlNWMtYjNiYS02YmQyNWU5MzBhNDIiLCJkYzMxN2Q5OC0xMTAwLTQyM2YtOTUzZi1mZjRkYjc4MzUwMTgiXSwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vcHJvZHVjdCI6WyJESVJFQ1QiLCJQUyJdLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS9jb21wYW55IjpbeyJpZCI6IjExZmMyMDUwLTViYWEtNDM5Ni04MjdlLTE3NGU3OTgwMmU4OSIsInByb2R1Y3QiOiJESVJFQ1QifV0sImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL21zdGFyX2lkIjoiQUU1RTJFN0YtNUE1QS00RUQ5LUFEQUQtNTE4MDUzQTBDQ0NBIiwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS9wYXNzd29yZENoYW5nZVJlcXVpcmVkIjpmYWxzZSwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vdWltX3JvbGVzIjoiRUFNUyxNRF9NRU1CRVJfMV8xLERPVF9DT01fRlJFRSxESVJFQ1QiLCJpc3MiOiJodHRwczovL2xvZ2luLXByb2QubW9ybmluZ3N0YXIuY29tLyIsInN1YiI6ImF1dGgwfEFFNUUyRTdGLTVBNUEtNEVEOS1BREFELTUxODA1M0EwQ0NDQSIsImF1ZCI6WyJodHRwczovL3VpbS1wcm9kLm1vcm5pbmdzdGFyLmF1dGgwLmNvbS9hcGkvdjIvIiwiaHR0cHM6Ly91aW0tcHJvZC5tb3JuaW5nc3Rhci5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzI4NTkyMDk0LCJleHAiOjE3Mjg2Nzg0OTQsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJDaGVLTTR1ajhqUFQ2MGFVMkk0Y1BsSDhyREtkT3NaZCJ9.cNTDGeIpo7dCNhhbwd6wx65ScB3RRqv1oShQjRN782ePz2q2Lfcw6NYeQreFgXgBRROPDRBJLJGBoWDrrjz3sKZrYryPdRctUbeuythbmukGoGHqFM-wAdZR8Z6tuGXffB05MupWUCqOXjDMIIQi1E8glDB8g3os1Hx7xlQnDtmshf9fRr6dRpCtz5MA8rFfKaSujwM3t4wGwrK2GnHMbP7-jooEzOUa1gsl1ujeGVVQxd8mLfkfgYGumJ9kWEdFmjot6RCPp29lL3l1ZwTMR8uc3jzj6YBZk63ci5U1OK3hnSDS1rFP0fs5KDii5ui5P3gM_Bu5tgZjTnQabtKrSg"

# md.connect()

# data = md.get_data("ANF")

# data = md.direct.get_morningstar_data_sets()
# print(data)

# abercrombie = md.direct.lookup.companies('Ford Motor')

# print(abercrombie)

# print(type(abercrombie))

# print()
# print()
# print()

# print(abercrombie['Company name'])

# test = md.direct.get_investment_data(investments=["0C000007QC"])

# print("\n\n\n\nTest:")
# print(test)

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'taitaishi123@gmail.com'
}

print("\n\n\n\nKeys:")
abercrombieJSON = requests.get("https://data.sec.gov/api/xbrl/companyfacts/CIK0001018840.json", headers=headers)
test2 = abercrombieJSON.json()
for key in test2.keys():
    print(key)

print("\n-----------------------------------------------------------\n")

for fact in test2['facts']['us-gaap']:
    print(fact)