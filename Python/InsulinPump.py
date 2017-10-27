# CP3407 Insulin Pump Python BackEnd

# Python Imports
import os.path
import sqlite3
from sqlite3 import Error

sqlite_file = 'insulin_pump.sqlite'  # name of the sqlite database file


# Required Functions
# Memory - Database Need to use sql database
# Use SQLite

# Pump Control - inject insulin
# Clock Input
# Alarm
# External Device Connection
# Power Management
# Display??
# Physical Key Input - Key Pad
# Sensors - Temp, Pressure, Blood Glucose level

def create_db():
    # Create database if not already created

    # Tables
    table_name1 = 'Patient'  # name of the table to be created
    table_1_column = ['patient_id', 'first_name', 'last_name']  # name of columns
    table_1_column_field_type = ['INTEGER', 'STRING', 'STRING']  # column data types

    table_name2 = 'Insulin'  # name of the table to be created
    table_2_column = ['insulin_id', 'drip_rate', 'max_insulin_daily', 'remaining_insulin', 'min_insulin_rate',
                      'max_insulin_rate']  # name of columns
    table_2_column_field_type = ['INTEGER', 'FLOAT', 'FLOAT', 'FLOAT', 'FLOAT', 'FLOAT']  # column data types

    table_name3 = 'Battery'  # name of the table to be created
    table_3_column = ['battery_id', 'battery_power_level']  # name of columns
    table_3_column_field_type = ['INTEGER', 'INTEGER']  # column data types

    table_name4 = 'Clock'  # name of the table to be created
    table_4_column = ['clock_id', 'clock_time']  # name of columns
    table_4_column_field_type = ['INTEGER', 'FLOAT']  # column data types

    table_name5 = 'Blood_Glucose'  # name of the table to be created
    table_5_column = ['blood_glucose_id', 'blood_glucose_level']  # name of columns
    table_5_column_field_type = ['INTEGER', 'FLOAT']  # column data types

    table_name6 = 'Information_Log'  # name of the table to be created
    table_6_column = ['information_log_id', 'clock_time', 'battery_power_level', 'remaining_insulin',
                      'blood_glucose_level']  # name of columns
    table_6_column_field_type = ['INTEGER', 'FLOAT', 'FLOAT', 'FLOAT', 'FLOAT']  # column data types

    try:
        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
    except Error as e:
        print(e)
    finally:
        # Creating SQLite tables
        # Table 1
        c.execute('CREATE TABLE {tn} ({nf} {ft})'
                  .format(tn=table_name1, nf=table_1_column[0], ft=table_1_column_field_type[0]))
        for column, field in zip(table_1_column[1:], table_1_column_field_type[1:]):
            c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name1, cn=str(column), ct=field))

        # Table 2
        c.execute('CREATE TABLE {tn} ({nf} {ft})'
                  .format(tn=table_name2, nf=table_2_column[0], ft=table_2_column_field_type[0]))
        for column, field in zip(table_2_column[1:], table_2_column_field_type[1:]):
            c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name2, cn=str(column), ct=field))

        # Table 3
        c.execute('CREATE TABLE {tn} ({nf} {ft})'
                  .format(tn=table_name3, nf=table_3_column[0], ft=table_3_column_field_type[0]))
        for column, field in zip(table_3_column[1:], table_3_column_field_type[1:]):
            c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name3, cn=str(column), ct=field))

        # Table 4
        c.execute('CREATE TABLE {tn} ({nf} {ft})'
                  .format(tn=table_name4, nf=table_4_column[0], ft=table_4_column_field_type[0]))
        for column, field in zip(table_4_column[1:], table_4_column_field_type[1:]):
            c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name4, cn=str(column), ct=field))

        # Table 5
        c.execute('CREATE TABLE {tn} ({nf} {ft})'
                  .format(tn=table_name5, nf=table_5_column[0], ft=table_5_column_field_type[0]))
        for column, field in zip(table_5_column[1:], table_5_column_field_type[1:]):
            c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name5, cn=str(column), ct=field))

        # Table 6
        c.execute('CREATE TABLE {tn} ({nf} {ft})'
                  .format(tn=table_name6, nf=table_6_column[0], ft=table_6_column_field_type[0]))
        for column, field in zip(table_6_column[1:], table_6_column_field_type[1:]):
            c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name6, cn=str(column), ct=field))


def main():
    # Main Function
    print("Hello")

    if os.path.isfile(sqlite_file):
        pass
    else:
        create_db()


if __name__ == '__main__':
    main()
