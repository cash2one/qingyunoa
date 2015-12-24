# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte', '0002_auto_20151224_1007'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u521b\u5efa\u65f6\u95f4')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6570\u636e\u66f4\u65b0\u65f6\u95f4')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='\u6570\u636e\u5220\u9664\u65f6\u95f4', blank=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u540d\u79f0')),
                ('last_contact_time', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u8054\u7cfb\u65f6\u95f4', null=True)),
                ('next_contact_time', models.DateTimeField(default=None, null=True, verbose_name='\u6700\u540e\u8054\u7cfb\u65f6\u95f4', blank=True)),
                ('assign_to', models.ForeignKey(default=None, blank=True, to='organization.Staff', null=True, verbose_name='\u6307\u6d3e')),
                ('creator', models.ForeignKey(verbose_name='\u6570\u636e\u521b\u5efa\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('ctype', models.ForeignKey(related_name='+', default=None, blank=True, to='adminlte.SystemConfig', null=True, verbose_name='\u7c7b\u578b')),
                ('grade', models.ForeignKey(related_name='+', default=None, blank=True, to='adminlte.SystemConfig', null=True, verbose_name='\u7b49\u7ea7')),
                ('scale', models.ForeignKey(related_name='+', default=None, blank=True, to='adminlte.SystemConfig', null=True, verbose_name='\u89c4\u6a21')),
                ('status', models.ForeignKey(related_name='+', default=None, blank=True, to='adminlte.SystemConfig', null=True, verbose_name='\u72b6\u6001')),
            ],
            options={
                'verbose_name': '\u5ba2\u6237',
                'verbose_name_plural': '\u5ba2\u6237',
            },
        ),
    ]
