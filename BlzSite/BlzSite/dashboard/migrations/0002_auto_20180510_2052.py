# Generated by Django 2.0 on 2018-05-10 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='Servico',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='pedido_servico', to='dashboard.Servico'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='comentario',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=2, default='', max_digits=5),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='data_atendimento',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='data_pedido',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='local_atendimento',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=models.CharField(default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='servico',
            name='preco',
            field=models.DecimalField(decimal_places=2, default='', max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='servico',
            name='tipo',
            field=models.CharField(default='', max_length=2, null=True),
        ),
    ]