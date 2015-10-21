import simplejson
import requests


V1_ENDPOINT = "https://api.lendingclub.com/api/investor/v1"

class LendingClubStub:
    def __init__(self, investor_id: int, api_key: str):
        self.investor_id = investor_id
        self.API_key = api_key
        self.header = {
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Authorization': api_key,
        }

    def get_portfolios_owned(self) -> list:
        """List portofolios, returns response if failed."""
        response = requests.get(
            "%s/accounts/%d/portfolios" % (V1_ENDPOINT, self.investor_id),
            headers=self.header,
        )

        response.raise_for_status()

        portfolios = response.json()['myPortfolios']

        return portfolios

    def create_portfolio(self, name: str, description: str) -> bool:
        """Create a portfolio, returns true if succeed response if failed."""
        portfolio_details = {
            'aid': self.investor_id,
            'portfolioName': name,
            'portfolioDescription': description,
        }

        response = requests.post(
            "%s/accounts/%d/portfolios" % (V1_ENDPOINT, self.investor_id),
            headers=self.header,
            data=simplejson.dumps(portfolio_details),
        )

        response.raise_for_status()

        return True

    def get_detailed_notes_owned(self) -> dict:
        """Get my detailed notes."""
        response = requests.get(
            "%s/accounts/%d/detailednotes" % (V1_ENDPOINT, self.investor_id),
            headers=self.header,
        )

        response.raise_for_status()

        notes = response.json()['myNotes']

        return notes

    def get_available_cash(self) -> int:
        """Get amount of available cash."""
        response = requests.get(
            "%s/accounts/%d/availablecash" % (V1_ENDPOINT, self.investor_id),
            headers=self.header,
        )

        response.raise_for_status()

        notes = response.json()['availableCash']

        return notes

    # TODO: Add possible filters
    def get_listed_loans(self) -> list:
        """Get loans listed for investing."""
        response = requests.get(
            "%s/loans/listing" % (V1_ENDPOINT,),
            headers=self.header,
        )

        response.raise_for_status()

        notes = response.json()['loans']

        return notes

    def submit_order(self, loan_ids: list, portfolio_id: int, requested_amount: int=25) -> bool:
        """Place order for list of loanIds."""
        orders = {
            'aid': self.investor_id,
            'orders': [
                {
                    'loanId': loan_id,
                    'requestedAmount': requested_amount,
                    'portfolioId': portfolio_id,
                } for loan_id in loan_ids
            ],
        }

        response = requests.post(
            "%s/accounts/%d/orders" % (V1_ENDPOINT, self.investor_id),
            headers=self.header,
            data=simplejson.dumps(orders),
        )

        response.raise_for_status()

        return True
