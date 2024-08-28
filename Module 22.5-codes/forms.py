class TransferMoneyForm(TransactionForm):
    account_no = forms.IntegerField()

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        balance = self.account.balance
        if amount > balance:
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not transfer more than your account balance'
            )
        if amount <= 0:
            raise forms.ValidationError(
                f'You can not transfer less than or equal to zero'
            )
        return amount