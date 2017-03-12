
from .models import Payment

class JsonTemplate(object):

    render = None

    def __init__(self, instance):
        _method_name = instance.__class__.__name__.lower()
        self.instance = instance
        try:
            self.render = self.__getattribute__('_{}_template'.format(_method_name))
        except Exception as e:
            raise Exception("No supported object for render Json")

    def _payment_template(self):
        if isinstance(self.instance, Payment):
            return {
                "price" : float(self.instance.amount)
            }
        else:
            raise Exception("Not an {} instance".format(Payment.__class__))
