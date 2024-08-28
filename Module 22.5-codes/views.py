class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'

    def get_initial(self):
        initial = {'transaction_type' : WITHDRAWAL}
        return initial
    
    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        bank_status = BankStatus.objects.first()
        if bank_status and bank_status.is_bankrupt:
            form.add_error(None,'The bank is bankrupt. Withdrawals are not allowed.')
            return self.form_invalid(form)
            
        account.balance -= amount
        account.save(update_fields = ['balance'])
        messages.success(self.request,f'Successfully withdrawn {amount}$ from your account')
        return super().form_valid(form)


