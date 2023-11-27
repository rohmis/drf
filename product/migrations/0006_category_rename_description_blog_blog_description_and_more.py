# Generated by Django 4.2.7 on 2023-11-27 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_blog_author_remove_blogcomment_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='description',
            new_name='blog_description',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='blog_title',
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='product.category'),
        ),
    ]
