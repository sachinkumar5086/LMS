# Generated by Django 3.2.4 on 2023-09-25 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20230925_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, null=True)),
                ('category_picture', models.ImageField(null=True, upload_to='static/category')),
                ('category_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='studentbatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='submittedtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('answer_file', models.FileField(null=True, upload_to='static/submittedtask')),
                ('tid', models.CharField(max_length=20, null=True)),
                ('userid', models.CharField(max_length=200, null=True)),
                ('marks', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=30, null=True)),
                ('profile', models.ImageField(null=True, upload_to='static/profile/')),
                ('course', models.CharField(max_length=30, null=True)),
                ('pyear', models.CharField(max_length=30, null=True)),
                ('college', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('passwd', models.CharField(max_length=100, null=True)),
                ('batchid', models.IntegerField(null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.studentbatch')),
            ],
        ),
        migrations.CreateModel(
            name='mytask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('task_file', models.FileField(null=True, upload_to='static/task')),
                ('added_date', models.DateField(null=True)),
                ('taskbatch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.studentbatch')),
            ],
        ),
        migrations.CreateModel(
            name='mylectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlink', models.CharField(max_length=300, null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='static/video')),
                ('video_description', models.TextField(null=True)),
                ('added_date', models.DateField(null=True)),
                ('video_batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.studentbatch')),
                ('video_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.category')),
            ],
        ),
        migrations.CreateModel(
            name='enotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('note_pic', models.ImageField(null=True, upload_to='static/enotes')),
                ('pdf_notes', models.FileField(null=True, upload_to='static/pdf')),
                ('added_date', models.DateField(null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.studentbatch')),
            ],
        ),
        migrations.CreateModel(
            name='batchtiming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clink', models.CharField(max_length=300, null=True)),
                ('timing', models.CharField(max_length=50, null=True)),
                ('start_date', models.DateField(null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.studentbatch')),
            ],
        ),
    ]
