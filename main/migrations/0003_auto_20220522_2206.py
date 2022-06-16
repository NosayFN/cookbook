# Generated by Django 3.2.9 on 2022-05-22 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220522_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('short_description', models.CharField(max_length=255, verbose_name='Short Description')),
                ('description', models.TextField(verbose_name='Description')),
                ('video', models.TextField(verbose_name='Video Link')),
                ('status', models.CharField(choices=[('published', 'Published'), ('offered', 'Offered')], default='offered', max_length=40, verbose_name='Статус')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.userprofile', verbose_name='Author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category', verbose_name='Status')),
                ('ingredients', models.ManyToManyField(to='main.Ingredient', verbose_name='Ingredient')),
            ],
            options={
                'verbose_name': 'Reciepe',
                'verbose_name_plural': 'Reciepes',
            },
        ),
        migrations.DeleteModel(
            name='Reciepe',
        ),
    ]