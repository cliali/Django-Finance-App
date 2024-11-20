from django import forms

from finance_config.tracker.models import Category, Transaction


class TransactionForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), widget=forms.RadioSelect()
    )

    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        if amount <= 0:
            raise forms.ValidationError("Amount must be positive number!")

        return amount

    class Meta:
        model = Transaction
        fields = ["type", "amount", "date", "category"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}
