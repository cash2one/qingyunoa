# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='last_contact_time',
            field=models.DateTimeField(default=None, null=True, verbose_name='\u6700\u540e\u8054\u7cfb\u65f6\u95f4', blank=True),
        ),
    ]
