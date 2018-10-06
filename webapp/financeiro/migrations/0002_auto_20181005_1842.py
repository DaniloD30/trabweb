# Generated by Django 2.0.8 on 2018-10-05 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuarios',
        ),
        migrations.AlterField(
            model_name='baixapagar',
            name='idBaixasPagar',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='baixareceber',
            name='idBaixasReceber',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='idClientes',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contasbancarias',
            name='idContasBancarias',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='idEmpresas',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fornecedores',
            name='idFornecedores',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lancamentopagar',
            name='idLancamentosPagar',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lancamentoreceber',
            name='idLancamentosReceber',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='planodecontas',
            name='idPlanodeContas',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tesouraria',
            name='idTesouraria',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]