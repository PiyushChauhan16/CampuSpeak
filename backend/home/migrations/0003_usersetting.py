# Generated by Django 4.2.4 on 2023-12-08 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_comment_replyid'),
    ]

    operations = [
        migrations.CreateModel(
            name='userSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isEnable', models.TextField(default='1', max_length=1)),
                ('uid', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
    ]
