# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_aptitudetest_eligibilitytest_hrtest_quantitativetest_reasoningtest_techtest_verbalstest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Test Name'),
        ),
    ]
