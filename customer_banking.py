# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Helper function to validate for float string
# https://www.programiz.com/python-programming/examples/check-string-number
def isfloat(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = input("Please set the savings balance on account: $")
    savings_interest = input("Please set the interest rate percentage on the account: ")
    savings_maturity = input("Please set your savings maturity months on the account: ")

    # Validate inputs
    valid_input = True
    if isfloat(savings_balance):
        savings_balance = float(savings_balance)
    else:
        valid_input = False
    if isfloat(savings_interest):
        savings_interest = float(savings_interest)
    else:
        valid_input = False
    if savings_maturity.isnumeric():
        savings_maturity = int(savings_maturity)
    else:
        valid_input = False

    if(not valid_input):
        # Give message to user if inputs are not valid
        print("Please enter a valid data type")
        exit()

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Updated savings account balance with interest earned: ${updated_savings_balance:,.2f}")
    print(f"Updated interest earned on account during {savings_maturity} months: ${interest_earned:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = input("Please set the cd balance on account: $")
    cd_interest = input("Please set the interest rate percentage on the account: ")
    cd_maturity = input("Please set your savings maturity months on the account: ")

    # Validate inputs
    valid_input = True
    if isfloat(cd_balance):
        cd_balance = float(cd_balance)
    else:
        valid_input = False
    if isfloat(cd_interest):
        cd_interest = float(cd_interest)
    else:
        valid_input = False
    if cd_maturity.isnumeric():
        cd_maturity = int(cd_maturity)
    else:
        valid_input = False

    if(not valid_input):
        # Give message to user if inputs are not valid
        print("Please enter a valid data type")
        exit()

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Updated cd account balance with interest earned: ${updated_cd_balance:,.2f}")
    print(f"Updated interest earned on account during {cd_maturity} months: ${interest_earned:,.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()