from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_transaction_email(user,amount,subject,template,receiver_account):
        message = render_to_string(template,{
            'user' : user,
            'amount' : amount,
            'account' : receiver_account,
        })
        to_email = user.email
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message,'text/html')
        send_email.send()

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Your password was successfully updated!')
        send_transaction_email(self.request.user,None,"Password Updated Message",'accounts/pass_change_email.html',None)
        return super().form_valid(form)
    


class TransferMoneyView(TransactionCreateMixin):
    form_class = TransferMoneyForm
    template_name = 'transactions/transfer_amount.html'
    title = 'Transfer Money'
    success_url = reverse_lazy("transaction_report")

    def get_initial(self):
        initial = {'transaction_type' : TRANSFER_MONEY}
        return initial
    
    def form_valid(self,form):
        account_no = form.cleaned_data.get('account_no')
        amount = form.cleaned_data.get('amount')
        sender_account = self.request.user.account
        
        try:
            receiver_account = UserBankAccount.objects.get(account_no = account_no)

        except UserBankAccount.DoesNotExist:
            form.add_error(None, 'The account does not exist.')
            return self.form_invalid(form)
        
        if(sender_account == receiver_account):
            form.add_error(None,'You cant pass money in your own account')
            return self.form_invalid(form)
        
        else:
            sender_account.balance -= amount
            receiver_account.balance += amount
            sender_account.save(update_fields = ['balance'])
            receiver_account.save(update_fields = ['balance'])
            messages.success(self.request,f'Money has been transferred Successfully')
            send_transaction_email(self.request.user,amount,"Transfer Confirmation Message",'transactions/transfer_email.html',receiver_account)
            send_transaction_email(receiver_account.user,amount,"You've Received a Transfer",'transactions/receiver_email.html',receiver_account)
            return super().form_valid(form)