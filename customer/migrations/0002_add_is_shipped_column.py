from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),  # Replace with the previous migration number
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
    ]
