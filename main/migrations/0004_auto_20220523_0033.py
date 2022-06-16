# Generated by Django 3.2.9 on 2022-05-22 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('main', '0003_auto_20220522_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('offered', 'Offered')], default='offered', max_length=40, verbose_name='Status'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
