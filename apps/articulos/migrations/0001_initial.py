# Generated by Django 2.2 on 2020-11-30 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=25)),
                ('marca', models.CharField(max_length=25)),
                ('modelo', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
                'db_table': 'Articulo',
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='OfertaArticulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('periodo_gracia', models.IntegerField()),
                ('descuento', models.IntegerField()),
                ('tipo_entrega', models.CharField(max_length=25)),
                ('id_articulo', models.ForeignKey(db_column='id_articulos', on_delete=django.db.models.deletion.CASCADE, to='articulos.Articulo')),
                ('id_provedora', models.ForeignKey(db_column='id_provedora', on_delete=django.db.models.deletion.CASCADE, to='personas.EmpresaProvedora')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Ofertas',
                'db_table': 'Oferta',
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existencia', models.IntegerField()),
                ('id_articulo', models.ForeignKey(db_column='id_articulos', on_delete=django.db.models.deletion.CASCADE, to='articulos.Articulo')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventario',
                'db_table': 'Inventario',
                'default_permissions': [],
            },
        ),
    ]
