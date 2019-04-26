import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

api_key =  "api-key=BdHVq2dk5Q0xFBYZNXN0prtovoV699r3"

simfin_url = "https://simfin.com/api/v1/"
id_query = "info/find-id/ticker/"
company_query = "companies/id/"
statement_query = "statements/standardised"
avail_statements = "statements/list"


def get_url(url):
    try:
        content = requests.get(url, verify=False)
    except requests.exceptions as e:
        print(f'exception: {e}')

    return content.json()


def get_simfin_ids(ticker):
    url = f'{simfin_url}{id_query}{ticker}?{api_key}'
    simfin_ids = get_url(url)
    return simfin_ids


def get_company_info(ticker):
    simfin_ids = get_simfin_ids(ticker)
    companies_info = []
    for simfin_id in simfin_ids:
        url = f'{simfin_url}{company_query}{simfin_id["simId"]}?{api_key}'
        company_info = get_url(url)
        companies_info.append(company_info)
    return companies_info


def get_available_statements(simfin_id):
    url = f'{simfin_url}{company_query}{simfin_id}/{avail_statements}?{api_key}'
    return get_url(url)


def get_statement(simfin_id, stype, year):
    statement = {}
    url = f'{simfin_url}{company_query}{simfin_id}/{statement_query}?stype={stype}&fyear={year}&ptype=FY&{api_key}'
    statement_data = get_urt(url)
    row_num=0
    if len(statement) == 0:
        statement[row_num] = ["Description", year]
    for value in statement_data["values]"]:
        row_num += 1
        if value["valueChosen"] is None:
            value_chosen = None
        else:
            value_chosen = int(value["valueChosen"])/1000000
        statement[row_num] = [value["standardisedName"], value_chosen]
    return statement

if __name__ == "__main__":
    ticker = input("Enter the stock ticker: ")
    ticker = ticker.upper()

    simfin_ids = get_simfin_ids(ticker)
    print(f'simfin_ids: {simfin_ids}')
    company_info = get_company_info(ticker)
    print(f'company_info: {company_info}')
    for simfin_id in simfin_ids:
        print(f'available_statements: {get_available_statements(simfin_id["simId"])}')
