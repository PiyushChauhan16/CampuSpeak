# Generated by Django 4.2.4 on 2023-11-08 10:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('pid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('postContent', models.TextField()),
                ('image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('rollNo', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('authPin', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='saved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='home.post')),
                ('uid', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('cid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('commentContent', models.TextField()),
                ('pid', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='home.post')),
                ('replyId', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='home.comment')),
                ('uid', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
    ]
