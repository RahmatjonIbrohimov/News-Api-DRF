from rest_framework.serializers import ModelSerializer
from .models import NewsKeeperModel



class NewSerializers(ModelSerializer):

    class Meta:
        model = NewsKeeperModel
        fields = '__all__'