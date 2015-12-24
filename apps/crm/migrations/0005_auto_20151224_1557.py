# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import core.adminlte.constants


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0002_auto_20151224_1007'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
        ('crm', '0004_auto_20151224_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('plan_amount', models.FloatField(default=0.0, verbose_name='\u8ba1\u5212\u91d1\u989d')),
                ('deal_amount', models.FloatField(default=0.0, verbose_name='\u6210\u4ea4\u91d1\u989d')),
                ('last_contact_date', models.DateField(default=None, null=True, verbose_name='\u6700\u540e\u8054\u7cfb', blank=True)),
                ('next_contact_date', models.DateField(default=None, null=True, verbose_name='\u4e0b\u6b21\u8054\u7cfb', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=1, verbose_name='\u6570\u636e\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
                ('assign_to', models.ForeignKey(default=None, blank=True, to='organization.Staff', null=True, verbose_name='\u6307\u6d3e\u7ed9')),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
            bases=(models.Model, core.adminlte.constants.UsableStatus),
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_contact_time',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='next_contact_time',
        ),
        migrations.AddField(
            model_name='customer',
            name='last_contact_date',
            field=models.DateField(default=None, null=True, verbose_name='\u6700\u540e\u8054\u7cfb', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='next_contact_date',
            field=models.DateField(default=None, null=True, verbose_name='\u4e0b\u6b21\u8054\u7cfb', blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(related_name='+', default=None, blank=True, to='crm.Customer', null=True, verbose_name='\u6240\u5c5e\u5ba2\u6237'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(related_name='+', to='adminlte.SystemConfig'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(related_name='+', default=None, blank=True, to='crm.Product', null=True, verbose_name='\u4ea7\u54c1'),
        ),
    ]
