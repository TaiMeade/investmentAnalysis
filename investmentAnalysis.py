import streamlit as st
# import morningstar_data as md
# import os
import pandas as pd
# import requests
# import json
# from IPython.display import display
# from xbrl import XBRLParser
import yfinance as yf
import pprint
# import openpyxl

"""
# This is a list of searches offered by Morningstar...used this list to assist in getting ids for each datapoint since I could not find them online ANYWHERE
# 0   "0218,0020,"                                           Snapshot
# 1   "0218-1203,"  Sustainable Investing: Low Carbon Transition M...
# 2   "0218-0497,"     Sustainable Investing: Apply Exclusions (Fund)
# 3   "0218-0450,"  Sustainable Investing: Apply Exclusions (Company)
# 4   "0218-0498,"       Sustainable Investing: Limit ESG Risk (Fund)
# 5   "0218-0446,"    Sustainable Investing: Limit ESG Risk (Company)
# 6   "0218-0499,"  Sustainable Investing: Seek ESG Opportunity (F...
# 7   "0218-0981,"          Sustainable Investing: Carbon Risk (Fund)
# 8   "0218-0982,"     Sustainable Investing: Carbon Emissions (Fund)
# 9   "0218-0985,"  Sustainable Investing: Carbon Emissions Multic...
# 10  "0218-0983,"   Sustainable Investing: Carbon Involvement (Fund)
# 11  "0218-0503,"  Sustainable Investing: Seek ESG Opportunity (C...
# 12  "0218-0984,"            Sustainable Investing: Carbon (Company)
# 13  "0218-0500,"  Sustainable Investing: Target Sustainable Them...
# 14  "0218-0494,"  Sustainable Investing: Target Sustainable Them...
# 15  "0218-1201,"  Sustainable Investing: Low Carbon Transition M...
# 16  "0218-0502,"  Sustainable Investing: Practice Active Ownersh...
# 17  "0218-0526,"  Sustainable Investing: Physical Climate Risk M...
# 18  "0218-0501,"  Assess Impact: Global Operational Impact Metri...
# 19  "0218-0504,"  Assess Impact: Global Operational Impact Metri...
# 20  "0218-0490,"  Assess Impact: EU SFDR Mandatory Corporate PAI...
# 21  "0218-0491,"  Assess Impact: EU SFDR Mandatory Sovereign PAI...
# 22  "0218-0492,"  Assess Impact: EU SFDR Voluntary Corporate PAI...
# 23  "0218-0493,"  Assess Impact: EU SFDR Voluntary Sovereign PAI...
# 24  "0218-0495,"    Assess Impact: EU SFDR PAIs (Company & Country)
# 25  "0218-0511,"                          Firm Diversity: Ownership
# 26  "0218-0512,"                      Firm Diversity: Board Members
# 27  "0218-0513,"                          Firm Diversity: Employees
# 28  "0218-0472,"                                  Strategy Analysis
# 29  "0218-0480,"                          Strategy Vehicle Analysis
# 30  "0218-0034,"                                         Operations
# 31  "0218-0036,"                                    Returns (Daily)
# 32  "0218-0037,"                                Returns (Month-End)
# 33  "0218-0038,"                              Returns (Quarter-End)
# 34  "0218-0039,"                            Returns (Calendar Year)
# 35  "0218-0260,"                           Dividend (Calendar Year)
# 36  "0218-0261,"         Estimated Share Class Net Flow (Month-End)
# 37  "0218-0292,"          Estimated Fund-Level Net Flow (Month-End)
# 38  "0218-0041,"                       Post-tax Returns (Month-End)
# 39  "0218-0043,"                    Risk – Total Return (Month-End)
# 40  "0218-0044,"                  Risk – Total Return (Quarter-End)
# 41  "0218-0045,"                     Morningstar Ratings and Grades
# 42  "0593-0255,"                                   Asset Allocation
# 43  "0218-0253,"                               CAN Asset Allocation
# 44  "0218-0102,"                   Strategy Target Asset Allocation
# 45  "0218-0047,"                             Equity Sector Exposure
# 46  "0218-0353,"                           Equity Industry Exposure
# 47  "0218-0048,"                              Equity Sectors (GICS)
# 48  "0218-0049,"                             Equity Industry (GICS)
# 49  "0218-0050,"                           Equity Port Stats (Long)
# 50  "0218-0051,"                          Equity Port Stats (Short)
# 51  "0218-0035,"                              Equity Style Analysis
# 52  "0218-0052,"                           Equity Regional Exposure
# 53  "0218-0053,"                            Equity Country Exposure
# 54  "0218-0300,"                              Equity Country (MSCI)
# 55  "0218-0418,"                            Fixd-Inc Core Analytics
# 56  "0218-0420,"                           Fixd-Inc Core Attributes
# 57  "0218-0432,"                       Fixd-Inc Coupon and Interest
# 58  "0218-0422,"                            Fixd-Inc Credit Ratings
# 59  "0218-0514,"                         Fixd-Inc Currency Exposure
# 60  "0218-0485,"                       Fixd-Inc Geographic Exposure
# 61  "0218-0468,"                        Fixd-Inc Interest Rate Risk
# 62  "0218-0483,"                       Fixd-Inc Morningstar Sectors
# 63  "0218-0473,"          Fixd-Inc Option: Call, Put, Sink, Convert
# 64  "0218-0470,"                              Fixd-Inc Return/Yield
# 65  "0218-0430,"                        Fixd-Inc Sector Corp Credit
# 66  "0218-0424,"                           Fixd-Inc Sector Securtzd
# 67  "0218-0434,"                   Fixd-Inc Sector Securtzd CMO/ABS
# 68  "0218-0426,"                            Fixd-Inc Sector US Muni
# 69  "0218-0438,"                     Fixd-Inc Sector US Muni Credit
# 70  "0218-0986,"                       Fixd-Inc Surveyed Statistics
# 71  "0218-0428,"                             Fixd-Inc US Regulatory
# 72  "0218-0054,"                     Fixed-Inc Portfolio Statistics
# 73  "0218-0323,"                   Fixed-Inc Super Sector Breakdown
# 74  "0218-0324,"                 Fixed-Inc Primary Sector Breakdown
# 75  "0218-0325,"               Fixed-Inc Secondary Sector Breakdown
# 76  "0218-0326,"                 Fixed-Inc Sector Country Breakdown
# 77  "0218-0078,"                     Fixed-Inc Muni Sector Exposure
# 78  "0218-0227,"                        Fixed-Inc Regional Exposure
# 79  "0218-0056,"                         Fixed-Inc Country Exposure
# 80  "0218-0520,"                        Portfolio Currency Exposure
# 81  "0218-0057,"                         Surveyed Currency Exposure
# 82  "0218-0309,"                                      Cash Exposure
# 83  "0218-0442,"                         Revenue Exposure by Region
# 84  "0218-0444,"                        Revenue Exposure by Country
# 85  "0218-0058,"                                  Fees and Expenses
# 86  "0218-0103,"                        Fees Schedule and Breakdown
# 87  0218-0440,"                                         Risk Model
"""

# os.environ['MD_AUTH_TOKEN'] = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1EY3hOemRHTnpGRFJrSTRPRGswTmtaRU1FSkdOekl5TXpORFJrUTROemd6TWtOR016bEdOdyJ9.eyJodHRwczovL21vcm5pbmdzdGFyLmNvbS9lbWFpbCI6ImludmVzdEByYWRmb3JkLmVkdSIsImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL3JvbGUiOlsiUGVyc29uYS5EaXJlY3RGb3JBc3NldE1hbmFnZW1lbnQiLCJFbmFibGVkIEFuYWx5dGljcyBMYWIgRGVsaXZlcnkgTm90ZWJvb2tzIiwiRGlzYWJsZSBEZWZpbmVkIENvbnRyaWJ1dGlvbiBQbGFucyIsIlBvcnRmb2xpbyBBbmFseXNpcyBVc2VyIl0sImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL2NvbXBhbnlfaWQiOiIxMWZjMjA1MC01YmFhLTQzOTYtODI3ZS0xNzRlNzk4MDJlODkiLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS9pbnRlcm5hbF9jb21wYW55X2lkIjoiQ2xpZW50MCIsImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL2RhdGFfcm9sZSI6W10sImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL2xlZ2FjeV9jb21wYW55X2lkIjoiMTFmYzIwNTAtNWJhYS00Mzk2LTgyN2UtMTc0ZTc5ODAyZTg5IiwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vcm9sZV9pZCI6WyI3OGJhMWFlNy0xZWUzLTQ0YTAtYTAxOC0wOGM1NThmZWNmMTciLCI4MjYyOWNkMC1kZjgwLTRlNWMtYjNiYS02YmQyNWU5MzBhNDIiLCJkYzMxN2Q5OC0xMTAwLTQyM2YtOTUzZi1mZjRkYjc4MzUwMTgiXSwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vcHJvZHVjdCI6WyJESVJFQ1QiLCJQUyJdLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS9jb21wYW55IjpbeyJpZCI6IjExZmMyMDUwLTViYWEtNDM5Ni04MjdlLTE3NGU3OTgwMmU4OSIsInByb2R1Y3QiOiJESVJFQ1QifV0sImh0dHBzOi8vbW9ybmluZ3N0YXIuY29tL21zdGFyX2lkIjoiQUU1RTJFN0YtNUE1QS00RUQ5LUFEQUQtNTE4MDUzQTBDQ0NBIiwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJodHRwczovL21vcm5pbmdzdGFyLmNvbS9wYXNzd29yZENoYW5nZVJlcXVpcmVkIjpmYWxzZSwiaHR0cHM6Ly9tb3JuaW5nc3Rhci5jb20vdWltX3JvbGVzIjoiRUFNUyxNRF9NRU1CRVJfMV8xLERPVF9DT01fRlJFRSxESVJFQ1QiLCJpc3MiOiJodHRwczovL2xvZ2luLXByb2QubW9ybmluZ3N0YXIuY29tLyIsInN1YiI6ImF1dGgwfEFFNUUyRTdGLTVBNUEtNEVEOS1BREFELTUxODA1M0EwQ0NDQSIsImF1ZCI6WyJodHRwczovL3VpbS1wcm9kLm1vcm5pbmdzdGFyLmF1dGgwLmNvbS9hcGkvdjIvIiwiaHR0cHM6Ly91aW0tcHJvZC5tb3JuaW5nc3Rhci5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzI5MDIxMjM2LCJleHAiOjE3MjkxMDc2MzYsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJDaGVLTTR1ajhqUFQ2MGFVMkk0Y1BsSDhyREtkT3NaZCJ9.tVXP0O4b_7ezBEvVp9yIaAitUbN0w6Nz8TLWUAixeVDhfv8RSgpWwPvGTnEkTrTHrQ7yu9uOka07Y7TsQBA8FUhJdayM4h7VrlN2Vfdax7tJv1-GbRuQLg7bXqcHQJsz9RIh0uSBKX9GSdykpsczSH0_5k_G35PjqGJDDlz5YybQGJaXd8ryenWDX-bab1XGAg8jBZGlGHOPHuYBGi01_z9IT98ha1GpegQZOXmAWjGV2D20rgpOp8Nlr7QJXWX1eG-O36320C8NK-55lpjXGKgebfk7-Ce1RQsCowTguaakErELaXG7hdcpXfN4uEVzqqbMORxG8noEoMnKhW9Dkg"

# Display all rows and all columns of DataFrame objects when printing
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.precision',3)

"""
# md.connect()

# data = md.get_data("ANF")

# test = md.direct.user_items.get_data_set_details("0218-0440")
# morningstar_data_sets = md.direct.get_morningstar_data_sets() REACTIVATE

# 
# list_of_tests = ["0218-0020","0218-1203","0218-0497","0218-0450","0218-0498","0218-0499","0218-0981","0218-0982","0218-0985","0218-0983","0218-0503","0218-0984","0218-0500","0218-0494","0218-1201","0218-0502","0218-0526","0218-0501","0218-0504","0218-0490","0218-0491","0218-0492","0218-0493","0218-0495","0218-0511","0218-0512","0218-0513","0218-0472","0218-0480","0218-0034","0218-0036","0218-0037","0218-0038","0218-0039","0218-0260","0218-0261","0218-0292","0218-0041","0218-0043","0218-0044","0218-0045","0593-0255","0218-0253","0218-0102","0218-0047","0218-0353","0218-0048","0218-0049","0218-0050","0218-0051","0218-0035","0218-0052","0218-0053","0218-0300","0218-0418","0218-0420","0218-0432","0218-0422","0218-0514","0218-0485","0218-0468","0218-0483","0218-0473","0218-0470","0218-0430","0218-0424","0218-0434","0218-0426","0218-0438","0218-0986","0218-0428","0218-0054","0218-0323","0218-0324","0218-0325","0218-0326","0218-0078","0218-0227","0218-0056","0218-0520","0218-0057","0218-0309","0218-0442","0218-0444","0218-0058"]
# new_list = []
# new_dict = {}
# for string in list_of_tests:
#     current_dataset = md.direct.user_items.get_data_set_details(string)
    # new_list.append(current_dataset)
    # for i in range(0, len(current_dataset['displayName'])):
    #     new_dict[current_dataset['displayName'][i]] = current_dataset['datapointId'][i]
    # print(md.direct.user_items.get_data_set_details(string))

# for frame in new_list:
#     print(frame['datapointId'] + "    " + frame['displayName'])


# write to a file
# f = open("idList.txt", "w")
# for key in new_dict.keys():
#     # print(new_dict[key] + " :     " + key)
#     f.write(new_dict[key] + " :     " + key + "\n")

# f.close()



# shows saved search criteria associated with our Morningstar account
# ourSavedSearches = md.direct.user_items.get_search_criteria() REACTIVATE
# print(ourSavedSearches)
# print(data)
# print("\n---------------------------------------------------------\n")
#
# results = md.direct.user_items.get_search_results('7245412')
# print(results)


# Testing finding data based on searches

# Specifies which datapoints to include in output when get_investment_data is called
# datapoint_ids = [
#     {"datapointId": "OS01W"}, # Name
#     {"datapointId": "OS385"}, # Ticker
#     # {"datapointId": "LF035"}, # Group?
#     {
#         "datapointId": "HS05X",
#         "startDate": "2024-08-30",
#         "endDate": "2024-10-30"
#      }, # P/E
#     {
#         "datapointId": "HS05V",
#         "startDate": "2024-08-30",
#         "endDate": "2024-10-30"
#      }, # P/B
#     {
#         "datapointId": "HS05U",
#         "startDate": "2024-08-30",
#         "endDate": "2024-10-30"
#      }, # P/S
# ]

# 17 is my search criteria...18 is from Fall 2023
# criteriaNum = int(input('\nPlease enter the number of the saved criteria you would like to use: ')) REACTIVATE
# REACTIVATE print("Search being conducted: " + ourSavedSearches['name'][criteriaNum - 2] + "\n") # we subtract 2 because the list we retrieve contains an extra entry and starts at index 0 rather than 1 like in Direct

# criteria = md.direct.user_items.get_search_criteria_conditions(search_criteria_id=ourSavedSearches['id'][criteriaNum - 2]) # we subtract 2 because the list we retrieve contains an extra entry and starts at index 0 rather than 1 like in Direct REACTIVATE

# data = md.direct.get_investment_data(investments=criteria, data_points=datapoint_ids) REACTIVATE

# write the results to a file (hoping this will improve readability)
# f = open("searchResults.txt", "w") # using w will overwite whatever is already in the file...this is to prevent repeat information at the moment REACTIVATE

# Condition to remove the rows/companies that result in NaN (Not a Number) for value criteria...TRY to remove them in future as this is NOT IMPLEMENTED yet
# f.write(data.to_string()) REACTIVATE
# f.close() REACTIVATE

# display(data.to_string()) # this line is to print the information to the terminal in a somewhat structured form...not extremely structured because the terminal does not seem to support horizontal scrolling

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
"""

"""
    This function corresponds to the first step "Screening for Securities" in How To Research Stocks (provided by Brett Taylor).
    
    Specifications from document:
        ○ Screening with Value Criteria
        ○ Some other things to look for: 10/yr Revenue growth, Operating Profit Margin,
        and Net Debt/EBITDA
        ○ Use these factors to determine the health of the company

    Inputs: 
        tickerToCheck: str --> represents the ticker/symbol of the company the user would like to check

    Returns the Company Name, Sector, and Current Stock Price.
    Checks value criteria (and screens based on inputs) and returns current ratios, as well as 
    whether or not the criteria is met.
    Also returns revenue growth, operating margins, and EBITDA.

    NOTE: All information is provided via the yfinance module
"""
def step_1(tickerToCheck: str):

    # Get P/E, P/B, and P/S needed
    peRatio = float(input("Please enter the P/E threshold: "))
    pbRatio = float(input("Please enter the P/B threshold: "))
    psRatio = float(input("Please enter the P/S threshold: "))

    tickerInfo = yf.Ticker(tickerToCheck).info

    # this line is meant to be used for checking what information the dictionary contains
    # pprint.pprint(tickerInfo)

    # sharePrice / trailingEPS
    priceToEarnings = tickerInfo['currentPrice'] / (tickerInfo['trailingEps'])

    # Initialize conditions to false
    peRatioMet = False
    pbRatioMet = False
    psRatioMet = False
    # Check if the ratios are met and change to true if they are
    if priceToEarnings <= peRatio: 
        peRatioMet = True 
    if tickerInfo['priceToBook'] <= pbRatio:
        pbRatioMet = True 
    if tickerInfo['priceToSalesTrailing12Months'] >= psRatio:
        psRatioMet = True 

    print('\n-----------------------------------------------------\n')
    print(f"Company Name: {tickerInfo['longName']}")
    print(f"Sector: {tickerInfo['sector']}")
    print(f"Current Price: {tickerInfo['currentPrice']}\n")
    
    # Ratios and whether or not they meet the criteria
    print("P/E Ratio: " + str(priceToEarnings) + "\t \u2713    Meets" if peRatioMet else "P/E Ratio: " + str(priceToEarnings) + "\t \u274C   Does not meet")
    print("P/B Ratio: " + str(tickerInfo['priceToBook']) + "\t\t \u2713    Meets" if pbRatioMet else 'P/B Ratio: ' + str(tickerInfo['priceToBook']) + "\t\t \u274C   Does not meet")
    print("P/S Ratio: " + str(tickerInfo['priceToSalesTrailing12Months']) + "\t\t \u2713    Meets" if psRatioMet else "P/S Ratio: " + str(tickerInfo['priceToSalesTrailing12Months']) + "\t\t \u274C   Does not meet")
    
    # Revenue Growth, operatingMargins, EBITDA
    print(f"\nRevenue Growth: {tickerInfo['revenueGrowth']}") # NOTE: Check if this is proper revenue growth metric referred to in document
    print(f"Operating Margins: {tickerInfo['operatingMargins']}") # NOTE: Check if this is proper operating margins metric referred to in document
    print(f"EBITDA: {tickerInfo['ebitda']:,}")

"""
    This function corresponds to the second step "Understanding the business" in How To Research Stocks (provided by Brett Taylor).
    
    Specifications from document:
        ○ Any factors that will affect the company, what they do, how they do it, where they
          do it.
        ○ Look at the 10-K form/annual report, EDGAR in US
        ○ Gather any important information that you can find

    Inputs: 
        tickerToCheck: str --> represents the ticker/symbol of the company the user would like to check

    Returns/prints several URLs the user can view to see recent news regarding their particular stock.
    Also returns a URL meant to assist in searching for the EDGAR 10-K form.

    NOTE: EDGAR 10-K form search query likely needs to be optimized
"""
def step_2(tickerToCheck: str):
    # Separator
    print('\n-----------------------------------------------------\n')

    # return a URL in which the user can go to in order to view news associated with the ticker/symbol
    yfURL = f'https://finance.yahoo.com/quote/{tickerToCheck.upper()}/news/'
    cnbcURL = f'https://www.cnbc.com/quotes/{tickerToCheck.upper()}'
    marketWatchURL = f'https://www.marketwatch.com/investing/stock/{tickerToCheck}'
    nasdaqURL = f'https://www.nasdaq.com/market-activity/stocks/{tickerToCheck}'
    businessInsiderURL = f'https://markets.businessinsider.com/stocks/{tickerToCheck}-stock#commodity-news'
    bloombergURL = f'https://www.bloomberg.com/quote/{tickerToCheck.upper()}:US'
    cnnURL = f'https://www.cnn.com/markets/stocks/{tickerToCheck.upper()}'
    robinhoodURL = f'https://robinhood.com/us/en/stocks/{tickerToCheck.upper()}/'
    motleyFoolURL = f'https://www.fool.com/quote/nasdaq/{tickerToCheck}/'
    wsjURL = f'https://www.wsj.com/market-data/quotes/{tickerToCheck.upper()}'
    tipRanksURL = f'https://www.tipranks.com/stocks/{tickerToCheck}/stock-news'

    # Print the URLs for several websites
    print('Some recent news:')
    print(f"Yahoo Finance:                        {yfURL}")
    print(f"CNBC:                                 {cnbcURL}")
    print(f"MarketWatch:                          {marketWatchURL}")
    print(f"NASDAQ:                               {nasdaqURL}")
    print(f"Business Insider:                     {businessInsiderURL}")
    print(f"Bloomberg:                            {bloombergURL}")
    print(f"CNN:                                  {cnnURL}")
    print(f"Robinhood:                            {robinhoodURL}")
    print(f"Motley Fool:                          {motleyFoolURL}")
    print(f"Wall Street Journal:                  {wsjURL}")
    print(f"Tip Ranks:                            {tipRanksURL}\n") # \n because it is the last URL for the recent news

    # Used to give the user a quick Google search to the EDGAR 10k report NOTE: may need to be rethought/optimized
    tickerInfo = yf.Ticker(tickerToCheck).info
    searchFor10kURL = f"https://www.google.com/search?q=edgar+{tickerInfo['symbol']}+10k+recent"
    print(f'10K via EDGAR:                        {searchFor10kURL}') # not sure if this is worth doing

"""
    This function corresponds to the third step "Understanding the Finances" in How To Research Stocks (provided by Brett Taylor).
    
    Specifications from document:
        ○ Financial Position: solvency, liquidity, capital structure
        ○ Growth rates: sales, costs, assets, liabilities, cash flows, share count
        ○ Profit Margins
        ○ Areas for improvement
        ○ Look at income statements, balance sheets, and cash flow statements
        ○ Cumulative Average Growth Rate (5, 10, 15 year period)
        ○ Margins (gross, operating, net)
        ○ Ratios (ROI’s, debt, efficiency, FCF conversion)
        ○ Peer Analysis
        ○ Look for any Red Flags
        ○ Check for any adjusted accounting numbers

    Inputs: 
        tickerToCheck: str --> represents the ticker/symbol of the company the user would like to check

    Returns/prints several URLs the user can view to see recent news regarding their particular stock.
    Also returns a URL meant to assist in searching for the EDGAR 10-K form.

    NOTE: How many of these things can actually be automated?  If it cannot be automated
          our goal should be to provide links or ideas for things the user can look at/review
"""
def step_3(tickerToCheck: str):
    # Financial Position: solvency, liquidity, capital structure


    # Growth rates (sales, costs, assets, liabilities, cash flows, share count)


    # Profit margins


    # Areas for improvement (can this be calculated or is this based on personal review/analysis)


    # Income statements, balance sheets, and cash flow statements


    # Cumulative average growth rate (5, 10, 15 year period)


    # Margins (gross, operating, and net)


    # Ratios (ROI’s, debt, efficiency, FCF conversion)


    # Peer Analyis (what is this exactly?)


    # Check for red flags regarding the company (again...is this personal analysis?)


    # Check for any adjusted accounting numbers


    pass # temporary to allow running of program

def main():
    userInput = input('Enter a ticker: ')

    step_1(userInput)

    step_2(userInput)

    step_3()

if __name__ == '__main__':
    main()