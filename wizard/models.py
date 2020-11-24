from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    BLACK = 'black'
    TRANSPARENT = 'transparent'

    MATERIAL_TYPES = ((BLACK, _('czarny')),
                      (TRANSPARENT, _('przezroczysty')))

    MAILERBOX = 'mailerbox'
    POLYMAILER = 'polymailer'

    PRODUCT_TYPES = ((MAILERBOX, _('MailerBox')),
                     (POLYMAILER, _('PolyMailer')))

    quantity = models.FloatField(_('Ilość'), default=200)
    price = models.FloatField(_('Cena'), default=0)
    width = models.FloatField(_('Szerokość'), default=0)
    height = models.FloatField(_('Wysokość'), default=0)
    length = models.FloatField(_('Długość'), default=0)
    material = models.CharField(choices=MATERIAL_TYPES, max_length=128)
    product_type = models.CharField(choices=PRODUCT_TYPES, max_length=128)

    class Meta:
        verbose_name = _('Produkt')
        verbose_name_plural = _('Produkty')


class Offer(models.Model):
    CREATED = 'created'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    STATE_CHOICES = ((CREATED, _('utworzona')),
                     (ACCEPTED, _('zaackeptowana')),
                     (REJECTED, _('odrzucona')))

    state = models.CharField(choices=STATE_CHOICES, max_length=128)
    products = models.ManyToManyField('wizard.Product', blank=True)

    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Oferty'

    def reject(self):
        self.state = self.REJECTED
        self.save()
        return True

    def accept(self):
        self.state = self.ACCEPTED
        self.save()
        return True
