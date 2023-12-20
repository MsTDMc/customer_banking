# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
import cd_account, savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input('What is your savings account balance? '))
    savings_interest = float(input('What is your savings account interest rate? '))
    savings_maturity = float(input('How many months is your savings account?'))

    # Call the create_savings_account function and pass the variables from the user.
    updated_balance, interest_earned = savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print()

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('What is your starting CD account balance? '))
    cd_interest = float(input('What is your CD interest rate? '))
    cd_maturity = int(input('How many months is your CD account? '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_balance, interest_earned = cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Your interest earned is:", format(interest_earned, ',.2f'),'%')
    print("Your account balance with interest earned is:", format(updated_balance,',.2f'), 'for', (cd_maturity), 'months')
    
if __name__ == "__main__":
    # Call the main function.
    main()
