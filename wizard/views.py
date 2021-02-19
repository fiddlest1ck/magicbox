from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.permissions import IsClient, IsSalesman, IsSuperuser
from wizard.models import Offer
from wizard.serializers import OfferSerializer, ProductTypeSerializer
from wizard.states import ProductMachine
from wizard.utils import MixedPermissionViewSet


class OfferViewSet(MixedPermissionViewSet):

    serializer_class = OfferSerializer
    queryset = Offer.objects.filter()
    permission_classes_by_action = {
        'create': (IsSuperuser | IsSalesman,),
        'list': (IsSuperuser,),
        'get': (IsSuperuser | IsClient,)
    }

    @action(detail=True, methods=('POST',), permission_classes=(IsAuthenticated, IsSuperuser | IsSalesman,))
    def product_create(self, request, pk):
        offer_state = self.get_object().state
        if offer_state == 'created':
            pt_serializer = ProductTypeSerializer(data=request.data)
            if pt_serializer.is_valid():
                p_machine = ProductMachine()
                p_machine.set_state(request.data)
                serializer = p_machine.state.get_serializer_class
                if serializer.is_valid():
                    product = serializer.save()
                    self.get_object().products.add(product.id)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(pt_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(_(f'Nie można dodawać produktów do oferty w statusie {offer_state}'), status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=('POST',), permission_classes=(IsAuthenticated, IsClient | IsSuperuser,))
    def accept(self, request, pk):
        if self.get_object().accept():
            return Response(_('Zaakceptowano ofertę'), status=status.HTTP_200_OK)
        return Response(_('Wystąpił błąd'), status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=('POST',), permission_classes=(IsAuthenticated, IsClient | IsSuperuser,))
    def reject(self, request, pk):
        if self.get_object().reject():
            return Response(_('Ofertę odrzucono'), status=status.HTTP_200_OK)
        return Response(_('Wystąpił błąd'), status=status.HTTP_400_BAD_REQUEST)
