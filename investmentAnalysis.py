import streamlit as st
import morningstar_data as md
import os
import pandas as pd
import requests
import json
# from xbrl import XBRLParser

os.environ['MD_AUTH_TOKEN'] = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1EY3hOemRHTnpGRFJrSTRPRGswTmtaRU1FSkdOekl5TXpORFJrUTROemd6TWtOR016bEdOdyJ9.eyJodHRwczovL21vcm5pbmdzdGFyLmNvbS9lbWFpbCI6ImludmVzdEByYWRmb3JkLmVkdSIsImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL3JvbGUiOlsiUGVyc29uYS5EaXJlY3RGb3JBc3NldE1hbmFnZW1lbnQiLCJFbmFibGVkIEFuYWx5dGljcyBMYWIgRGVsaXZlcnkgTm90ZWJvb2tzIiwiRGlzYWJsZSBEZWZpbmVkIENvbnRyaWJ1dGlvbiBQbGFucyIsIlBvcnRmb2xpbyBBbmFseXNpcyBVc2VyIl0sImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL2NvbXBhbnlfaWQiOiIxMWZjMjA1MC01YmFhLTQzOTYtODI3ZS0xNzRlNzk4MDJlODkiLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS9pbnRlcm5hbF9jb21wYW55X2lkIjoiQ2xpZW50MCIsImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL2RhdGFfcm9sZSI6W10sImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL2xlZ2FjeV9jb21wYW55X2lkIjoiMTFmYzIwNTAtNWJhYS00Mzk2LTgyN2UtMTc0ZTc5ODAyZTg5IiwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vcm9sZV9pZCI6WyI3OGJhMWFlNy0xZWUzLTQ0YTAtYTAxOC0wOGM1NThmZWNmMTciLCI4MjYyOWNkMC1kZjgwLTRlNWMtYjNiYS02YmQyNWU5MzBhNDIiLCJkYzMxN2Q5OC0xMTAwLTQyM2YtOTUzZi1mZjRkYjc4MzUwMTgiXSwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vcHJvZHVjdCI6WyJESVJFQ1QiLCJQUyJdLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS9jb21wYW55IjpbeyJpZCI6IjExZmMyMDUwLTViYWEtNDM5Ni04MjdlLTE3NGU3OTgwMmU4OSIsInByb2R1Y3QiOiJESVJFQ1QifV0sImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL21zdGFyX2lkIjoiQUU1RTJFN0YtNUE1QS00RUQ5LUFEQUQtNTE4MDUzQTBDQ0NBIiwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS9wYXNzd29yZENoYW5nZVJlcXVpcmVkIjpmYWxzZSwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vdWltX3JvbGVzIjoiRUFNUyxNRF9NRU1CRVJfMV8xLERPVF9DT01fRlJFRSxESVJFQ1QiLCJpc3MiOiJodHRwczovL2xvZ2luLXByb2QubW9ybmluZ3N0YXIuY29tLyIsInN1YiI6ImF1dGgwfEFFNUUyRTdGLTVBNUEtNEVEOS1BREFELTUxODA1M0EwQ0NDQSIsImF1ZCI6WyJodHRwczovL3VpbS1wcm9kLm1vcm5pbmdzdGFyLmF1dGgwLmNvbS9hcGkvdjIvIiwiaHR0cHM6Ly91aW0tcHJvZC5tb3JuaW5nc3Rhci5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzI4OTI1NDUxLCJleHAiOjE3MjkwMTE4NTEsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJDaGVLTTR1ajhqUFQ2MGFVMkk0Y1BsSDhyREtkT3NaZCJ9.FNq38iFc_cgEZT-LTa2N4nodfpZNZcz9MyAkYiwRUGBdqV-9oA7TpUA3CUSseR4jM6S-HX5ePi5ye9ieMetpr2uRI3-0KRLjZSq-BaXP9ldzjC7x_qzGHFFSPsodHfTKYpzrICJ6shU1yGusMpCX80wEgIYnywdk46jUEWStqcggqPAM9m04Vlaltcl48f1Kp6fprghGQe0ACr4Jw52Rtcroji73fRcw8wselCSC12JF2mEQqT-8yXpfeNSPYtenUr7jdMEtbrzFKYxVOWcKM2RiRmo3ktuDSn7RE2qc-XEY7yqZ2GAM9JodnIB5XRFP_lclPGVF_y4yEy0Payvt7Q"

# Display all rows and all columns of DataFrame objects when printing
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

# md.connect()

# data = md.get_data("ANF")

# shows saved search criteria associated with our Morningstar account
data = md.direct.user_items.get_search_criteria()

# print(data)
# print("\n---------------------------------------------------------\n")
#
# results = md.direct.user_items.get_search_results('7245412')
# print(results)


# Testing finding data based on searches

# Specifies which datapoints to include in output when get_investment_data is called
datapoint_ids = [
    {"datapointId": "OS01W"},
    {"datapointId": "OS385"},
    {"datapointId": "LF035"},
    # {"datapointId": "OS01W"},
]

criteria = md.direct.user_items.get_search_criteria_conditions(search_criteria_id=data['id'][18])

data = md.direct.get_investment_data(investments=criteria, data_points=datapoint_ids)
print(data)

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

# headers = {
#     'User-Agent': 'My User Agent 1.0',
#     'From': 'taitaishi123@gmail.com'
# }

# print("\n\n\n\nKeys:")
# abercrombieJSON = requests.get("https://data.sec.gov/api/xbrl/companyfacts/CIK0001018840.json", headers=headers)
# test2 = abercrombieJSON.json()
# for key in test2.keys():
#     print(key)

# print("\n-----------------------------------------------------------\n")

# for fact in test2['facts']['us-gaap']:
#     print(fact)

