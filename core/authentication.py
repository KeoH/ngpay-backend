
from rest_framework import authentication, exceptions

from credentials.models import Credential

class CredentialAuthentication(authentication.BaseAuthentication):


    def authenticate(self, request):
        
        if request.method == 'GET':
            api_key = request.GET.get('api_key', None)
        else:
            api_key = request.data.pop('api_key', None)

        if not api_key:
            raise exceptions.AuthenticationFailed('No credentials provided.')
        
        try:
            credential = Credential.objects.get(username=api_key)
        except Credential.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid API key.')
        print(credential)
        return (credential.account.merchant.user, True)