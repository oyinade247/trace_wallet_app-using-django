from django.contrib import admin

from wallet.models import Wallet, Transaction, Ledger


# Register your models here.
@admin.register(Wallet)
class walletAdmin(admin.ModelAdmin):
    list_display = ["wallet_number", "account_number", "balance", "status"]
    list_per_page = 10
    list_editable = ["status"]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["reference", "amount", "transaction_type", "sender", "receiver", "transaction_status"]
    list_per_page = 10
    list_editable = ["transaction_status"]


@admin.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
    list_display = ["transaction", "amount", "balance_after", "wallet", "transaction_type"]
    list_per_page = 10
    list_editable = ["transaction_type"]

