from django.db import models
from django.utils.text import slugify
from django.utils.html import format_html
from django.utils import timezone
from merdeka.apps.base.models import MyUser

class Commodities(models.Model):
    """
    Description: Commodities Description
    """
    class Meta:
        db_table = 'master_commodities'
        verbose_name = 'Commodities'
        verbose_name_plural = 'Commodities'

    name = models.CharField(max_length=60, blank=False)
    unique_name = models.SlugField(blank=True, max_length=200, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(null=True, blank=True, editable=False)

    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        self.unique_name = slugify(self.name)
        super(Commodities, self).save(**kwargs)

class Goods(models.Model):
    """
    Description: Goods Description
    """
    class Meta:
        db_table = 'master_goods'
        verbose_name = 'Goods'
        verbose_name_plural = 'Goods'

    commodity = models.ForeignKey(Commodities)
    name = models.CharField(max_length=60, blank=False)
    unique_name = models.SlugField(blank=True, max_length=200, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(null=True, blank=True, editable=False)

    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        self.unique_name = slugify(self.name)
        super(Goods, self).save(**kwargs)

class GoodsChilds(models.Model):
    """
    Description: GoodsChilds Description
    """
    class Meta:
        db_table = 'master_goods_childs'
        verbose_name = 'Goods Childs'
        verbose_name_plural = 'Goods Childs'

    goods = models.ForeignKey(Goods)
    name = models.CharField(max_length=60, blank=False)
    unique_name = models.SlugField(blank=True, max_length=200, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(null=True, blank=True, editable=False)

    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        self.unique_name = slugify(self.name)
        super(GoodsChilds, self).save(**kwargs)

class BaseUnit(models.Model):
    """
    Description: Base Unit Description
    """
    class Meta:
        db_table = 'master_base_unit'
        verbose_name = 'Base Unit'
        verbose_name_plural = 'Base Unit'

    name = models.CharField(max_length=60, blank=False)
    unique_name = models.SlugField(blank=True, max_length=200, unique=True, editable=False)
    condition = models.CharField(max_length=120, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(null=True, blank=True, editable=False)

    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        self.unique_name = slugify(self.name)
        super(BaseUnit, self).save(**kwargs)

class Province(models.Model):
    """
    Description: Province Description
    """
    class Meta:
        db_table = 'master_province'
        verbose_name = 'Province'
        verbose_name_plural = 'Province'

    name = models.CharField(max_length=60, blank=False)
    unique_name = models.SlugField(blank=True, max_length=200, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(null=True, blank=True, editable=False)

    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        self.unique_name = slugify(self.name)
        super(Province, self).save(**kwargs)

class City(models.Model):
    """
    Description: City Description
    """
    class Meta:
        db_table = 'master_City'
        verbose_name = 'City'
        verbose_name_plural = 'City'

    province = models.ForeignKey(Province)
    name = models.CharField(max_length=60, blank=False)
    unique_name = models.SlugField(blank=True, max_length=200, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(null=True, blank=True, editable=False)

    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        self.unique_name = slugify(self.name)
        super(City, self).save(**kwargs)

class TypeVenue(models.Model):
    """
    Description: Type Venue Description
    """
    class Meta:
        db_table = 'master_type_venue'
        verbose_name = 'Type Venue'
        verbose_name_plural = 'Type Venue'

    name = models.CharField(max_length=60, blank=False)
    unique_name = models.SlugField(blank=True, max_length=200, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(null=True, blank=True, editable=False)

    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        self.unique_name = slugify(self.name)
        super(TypeVenue, self).save(**kwargs)

class Venues(models.Model):
    """
    Description: Venues Description
    """
    class Meta:
        db_table = 'master_venues'
        verbose_name = 'Venues'
        verbose_name_plural = 'Venues'

    type_venue = models.ForeignKey(TypeVenue)
    city = models.ForeignKey(City)
    name = models.CharField(max_length=60, blank=False)
    unique_name = models.SlugField(blank=True, max_length=200, unique=True, editable=False)
    address = models.TextField(blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(null=True, blank=True, editable=False)

    def __unicode__(self):
        return self.name

    def save(self, **kwargs):
        self.unique_name = slugify(self.name)
        super(Venues, self).save(**kwargs)
