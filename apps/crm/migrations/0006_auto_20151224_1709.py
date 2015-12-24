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
        ('crm', '0005_auto_20151224_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('number', models.CharField(default=b'', max_length=200, null=True, verbose_name='\u5408\u540c\u7f16\u53f7', blank=True)),
                ('amount', models.FloatField(default=0.0, null=True, verbose_name='\u5408\u540c\u91d1\u989d', blank=True)),
                ('start_date', models.DateField(verbose_name='\u5f00\u59cb\u65e5\u671f')),
                ('end_date', models.DateField(verbose_name='\u7ed3\u675f\u65e5\u671f')),
                ('status', models.PositiveSmallIntegerField(default=1, verbose_name='\u6570\u636e\u72b6\u6001', choices=[(0, '\u7981\u7528'), (1, '\u542f\u7528'), (99, '\u5220\u9664')])),
                ('contract_status', models.ForeignKey(related_name='+', verbose_name='\u5408\u540c\u72b6\u6001', blank=True, to='adminlte.SystemConfig', null=True)),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('delivery_status', models.ForeignKey(related_name='+', verbose_name='\u4ea4\u4ed8\u72b6\u6001', blank=True, to='adminlte.SystemConfig', null=True)),
            ],
            options={
                'verbose_name': '\u5408\u540c',
                'verbose_name_plural': '\u5408\u540c',
            },
            bases=(models.Model, core.adminlte.constants.UsableStatus),
        ),
        migrations.AlterField(
            model_name='order',
            name='deal_amount',
            field=models.FloatField(default=0.0, verbose_name='\u6210\u4ea4\u91d1\u989d(RMB)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(related_name='+', verbose_name='\u72b6\u6001', to='adminlte.SystemConfig'),
        ),
        migrations.AlterField(
            model_name='order',
            name='plan_amount',
            field=models.FloatField(default=0.0, verbose_name='\u8ba1\u5212\u91d1\u989d(RMB)'),
        ),
        migrations.AddField(
            model_name='contract',
            name='order',
            field=models.ForeignKey(default=None, blank=True, to='crm.Order', null=True, verbose_name='\u6240\u5c5e\u8ba2\u5355'),
        ),
        migrations.AddField(
            model_name='contract',
            name='pay_status',
            field=models.ForeignKey(related_name='+', verbose_name='\u4ed8\u6b3e\u72b6\u6001', blank=True, to='adminlte.SystemConfig', null=True),
        ),
    ]
