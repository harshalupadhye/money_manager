from rest_framework import serializers
from newapp.models import wallet
class walletserializer(serializers.Serializer):
    wallet_id = serializers.IntegerField()
    user_name = serializers.CharField(max_length=20)
    money = serializers.IntegerField()
    def create(self, validate_data):
        return wallet.objects.create(**validate_data)
    def update(self, instance, validate_data):
        instance.Name=validate_data.get('username', instance.user_name)
        instance.id=validate_data.get('id',instance.wallet_id)
        instance.money=validate_data.get('money', instance.money)
        instance.save()
        return instance
