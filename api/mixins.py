
from .models import APICall

class APICallsRegisterMixin(object):

    def list(self, request, *args, **kwargs):
        APICall.objects.create(method="GET", merchant=request.user.merchant, view=self.__class__.__name__+'::list')
        return super(APICallsRegisterMixin, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        APICall.objects.create(method="GET", merchant=request.user.merchant, view=self.__class__.__name__+'::retrieve')
        return super(APICallsRegisterMixin, self).retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        APICall.objects.create(method="POST", merchant=request.user.merchant, view=self.__class__.__name__+'::create')
        return super(APICallsRegisterMixin, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        APICall.objects.create(method="PUT", merchant=request.user.merchant, view=self.__class__.__name__+'::update')
        return super(APICallsRegisterMixin, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        APICall.objects.create(method="PATCH", merchant=request.user.merchant, view=self.__class__.__name__+'::partial_update')
        return super(APICallsRegisterMixin, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        APICall.objects.create(method="DELETE", merchant=request.user.merchant, view=self.__class__.__name__+'::destroy')
        return super(APICallsRegisterMixin, self).destroy(request, *args, **kwargs)