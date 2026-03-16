from wallet.models import Transaction
import os

TOKEN = os.getenv("TOKEN")

def get_dashboard_data(user):
    wallet = user.wallet
    transactions = Transaction.objects.filter(
        receiver=wallet
    ).order_by('-created_at')[:5]

    return {
        "message": f"hi, {user.first_name}",
        "wallet": wallet.wallet_number,
        "balance": wallet.balance,
        "currency": wallet.currency,
        "status": wallet.status,
        "transactions": transactions
    }



