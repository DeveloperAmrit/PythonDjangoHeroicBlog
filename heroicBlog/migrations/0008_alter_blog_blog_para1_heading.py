# Generated by Django 4.0 on 2022-09-11 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroicBlog', '0007_blog_blog_para1_heading_blog_blog_para2_heading_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_para1_heading',
            field=models.CharField(default='headingPara1OK', max_length=10000),
        ),
    ]
