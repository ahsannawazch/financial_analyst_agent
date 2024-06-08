import os 
from dotenv import load_dotenv
load_dotenv()

import sys
# Adding src to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from financial_analyst_crew.crew import FinancialAnalystCrew

def run():
    inputs = {"company_name": "Tesla"}
    FinancialAnalystCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()

# import sys
# import os
# from dotenv import load_dotenv

# # Add the 'src' directory to the Python path
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
# sys.path.append(parent_dir)

# load_dotenv()

# from financial_analyst_crew.crew import FinancialAnalystCrew

# def run():
#     inputs = {"company_name": "Tesla"}
#     FinancialAnalystCrew().crew().kickoff(inputs=inputs)

# if __name__ == "__main__":
#     run()
