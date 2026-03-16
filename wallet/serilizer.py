from rest_framework import serializers

from wallet.models import Wallet, Transaction


class TransferSerializer(serializers.Serializer):
    receiver_wallet = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    idempotency_key = serializers.UUIDField()
    description = serializers.CharField(allow_blank=True,max_length=100)

    def validate_amount(self, value):
        if value < 0:
            raise Exception("Invalid amount. Transaction must be greater that 0.")
        return value

    def validate_receiver_wallet(self, value):
        try:
            _receiver_wallet = Wallet.objects.get(wallet_number=value)
        except Wallet.DoesNotExist:
            raise Exception("Wallet Does Not Exist")
        return value

class DepositSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    idempotency_key = serializers.UUIDField()
    def validate_amount(self, value):
        if value < 0:
            raise Exception("Invalid amount. Funds Must be greater Than 0")
        return value


class RecentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['receiver', 'reference', 'amount', 'status', 'created_at', 'transaction_type']


class DashboardSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=55)
    wallet_number = serializers.CharField(max_length=10)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)
    currency = serializers.CharField(max_length=3)
    status = serializers.CharField(max_length=10)
    transactions = RecentTransactionSerializer(many=True)


