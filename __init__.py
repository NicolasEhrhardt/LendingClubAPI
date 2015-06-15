import requests
import json

class LendingClubAPI:
    def __init__(self, investor_id: int, API_key: str) -> object:
        self.investor_id = investor_id
        self.API_key = API_key
        self.header = {
       'Accept': 'application/json',
       'Content-type': 'application/json',
       'Authorization': API_key}
        self.endpoint = "https://api.lendingclub.com/api/invstor/v1"

    def get_portfolios_owned(self) -> list:
        """List portofolios, returns response if failed"""
        r = requests.get(
            "%s/accounts/%d/portfolios" % (self.endpoint, investor_id),
            headers=self.header)

        if not r.ok:
            print('Error %d: %s' % (r.status_code, r.reason))
            return r

        portfolios = r.json()['myPortfolios']

        return portfolios

    def create_portfolio(self, name: str, description: str) -> bool:
        """Create a portfolio, returns true if succedeed response if failed"""
        portfolio_details = {
            'aid': investor_id,
            'portfolioName': name,
            'portfolioDescription': description,
        }

        r = requests.post(
            "%s/accounts/%d/portfolios" % (self.endpoint, investor_id),
            headers=self.header,
            data=json.dumps(portfolio_details))
        
        if not r.ok:
            print('Error %d: %s (%s)' % (r.status_code, r.reason, r.url))
            return r

        return True

    def get_detailed_notes_owned(self) -> dict:
        """Get my detailed notes"""
        r = requests.get(
            "%s/accounts/%d/detailednotes" % (self.endoint, investor_id),
            headers=self.header)

        if not r.ok:
            print('Error %d: %s' % (r.status_code, r.reason))
            return r.ok

        notes = r.json()['myNotes']

        return notes

    # TODO: Add possible filters
    def get_listed_loans(self) -> list:
        """Get loans listed for investing"""
        r = requests.get(
            "https://api.lendingclub.com/api/investor/v1/loans/listing",
            headers=self.header)

        if not r.ok:
            print('Error %d: %s' % (r.status_code, r.reason))
            return r.ok

        notes = r.json()['loans']

        return notes

    # TODO: Handle different error messages
    def submit_order(self, loan_ids: list, portfolio_id: int, requested_amount: int=25) -> bool:
        """Place order for list of loanIds, investing"""
        orders = {
            'aid': investor_id,
            'orders': [{ 
                'loanId': loan_id,
                'requestedAmount': requested_amount,
                'portfolioId': portfolio_id,
            } for loanId in loanIds]
        }

        r = requests.post(
            "https://api.lendingclub.com/api/investor/v1/accounts/%d/orders" % investor_id,
            headers=self.header,
            data=json.dumps(orders))
        
        if not r.ok:
            print('Error %d: %s (%s)' % (r.status_code, r.reason, r.url))
            return r

        return True

