# Generated by Django 2.2.3 on 2019-07-16 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('framework', models.CharField(choices=[('Laravel', 'Laravel'), ('Django', 'Django'), ('ASP.NET', 'ASP.NET'), ('Node.js', 'Node.js'), ('Spring', 'spring'), ('Flask', 'Flask')], max_length=50)),
                ('priority', models.CharField(choices=[('Urgent', 'Urgent'), ('Normal', 'Normal')], max_length=50, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
