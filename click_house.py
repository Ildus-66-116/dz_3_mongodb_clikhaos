"""Зарегистрируйтесь в ClickHouse.
Загрузите данные в ClickHouse и создайте таблицу для их хранения."""

from clickhouse_driver import Client

client = Client('localhost')
client.execute('CREATE DATABASE IF NOT EXISTS town_cary')

client.execute('''
    CREATE TABLE IF NOT EXISTS town_cary.crashes (
    id UInt64,
    location_description String,
    rdfeature String,
    rdsurface String,
    rdcondition String,
    lightcond String,
    weather String,
    crash_date Int64, 
    year String,
    fatalities String,
    injuries String,
    month String
    ) ENGINE = MergeTree() ORDER BY id''')

print("Таблица создана успешно.")
