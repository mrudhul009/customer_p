from rest_framework import serializers
from watchlist.models import Watchlist,Streamplatform 



class WatchlistSerializer(serializers.ModelSerializer):
    len_name=serializers.SerializerMethodField()
    class Meta:
        model=Watchlist
        fields="__all__"
        # exclude=["name"]

    def get_len_name(self,object):
        length=len(object.name) 
        return length
class Streamserializer(serializers.ModelSerializer):
    # Watchlist=WatchlistSerializer(many=True,read_only=True)
    # Watchlist=serializers.StringRelatedField(many=True,read_only=True)
    Watchlist=serializers.selct_related()
    class Meta:
        model=Streamplatform
        fields="__all__"
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     description=serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self,validated):
#         return Movie.objects.create(**validated)
#     def update(self, instance, validated_data):
#         instance.id=validated_data.get('id',instance.id)
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    # def validate_name(self,data):
    #     if len(data)<2 :
    #         raise serializers.ValidationError("not a vali name of a movie")
    #     else:
    #         return data
         
    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("name and description should not be same")
    #     else:
    #         return data


            

            































