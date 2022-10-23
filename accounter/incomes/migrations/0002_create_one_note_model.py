# Generated by Django 4.1.2 on 2022-10-21 19:31

import accounter.mixins
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('incomes', '0001_create_photo_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_in_check', models.DateTimeField()),
                ('score', models.FloatField(validators=[django.core.validators.MinValueValidator(0, 'Min number value!')])),
                ('where_from', models.CharField(max_length=30, null=True)),
                ('photo', models.ManyToManyField(to='incomes.photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'income_note',
                'verbose_name_plural': 'income_notes',
                'ordering': ['-date_in_check'],
            },
            bases=(models.Model, accounter.mixins.DateTimeMixin),
        ),
    ]
