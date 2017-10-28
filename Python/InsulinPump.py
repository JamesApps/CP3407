# CP3407 Insulin Pump Python BackEnd

# Python Imports
import os.path
import sqlite3
from sqlite3 import Error

sqlite_file = 'insulin_pump.sqlite'  # name of the sqlite database file


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


def alarm():
    # Alarm Functions
    # Battery low - The voltage of the battery has fallen to less than 0.5V
    battery_low = False

    # Sensor failure - The self-test of the sugar sensor has resulted in an error
    sensor_failure = False

    # Pump failure - The self-test of the pump has resulted in an error
    pump_failure = False

    # Delivery failure - It has not been possible to deliver the specified amount of insulin
    # (e.g. the needle may be blocked or incorrectly inserted)
    delivery_failure = False

    # Needle assembly removed - The user has removed the needle assembly
    needle_removed = False

    # Insulin reservoir removed - The user has removed the insulin reservoir
    reservoir_removed = False

    # Low insulin level - The level of insulin is low (indicating that the reservoir should be changed).
    low_insulin = False


# Pump Control - inject insulin


def clock():
    # Get clock input
    clock = float

    # At the beginning of each 24 hour period (indicated by clock =00:00:00), the
    # cumulative dose of insulin delivered is reset to 0.




# Sensors - Temp, Pressure, Blood Glucose level

# A blood sugar sensor, which measures the current blood sugar reading in
# micrograms/millilitre. This is updated every 10 minutes. The value of Reading? is normally between 1 and 35.
# r0, r1, and r2 maintain information about the last three readings from the sugar
# sensor. r2 holds the current reading, r1 the previous reading and r0 the reading
# before that. These are used to compute the rate of change of blood sugar readings

# capacity represents the capacity of the system’s insulin reservoir and
# insulin_available represents the amount of insulin in the reservoir that is currently
# available for delivery.

# A hardware test unit, which runs a self-test on the hardware every 30 seconds.
# Power Management



def insulin_pump_state():
    # switch?: (off, manual, auto)
    # ManualDeliveryButton?: N
    # Reading?: N
    # HardwareTest?: (OK, batterylow, pumpfail, sensorfail, deliveryfail)
    # InsulinReservoir?: (present, notpresent)
    # Needle?: (present, notpresent)
    # clock?: TIME
    #
    # # Output device definition
    # alarm! = (on, off)
    # display1!, P string
    # display2!: string
    # clock!: TIME
    # dose!: N
    #
    # # State variables used for dose computation
    # status: (running, warning, error)
    # r0, r1, r2: N
    # capacity, insulin_available : N
    # max_daily_dose, max_single_dose, minimum_dose: N
    # safemin, safemax: N
    # CompDose, cumulative_dose: N




# Pump configuration parameters
capacity = 100
safemin = 6
safemax = 14
max_daily_dose = 25
max_single_dose = 4
minimum_dose = 1

STATE = ""


def main():
    # Main Function

    # SQLite Database
    if os.path.isfile(sqlite_file):
        pass
    else:
        create_db()

    # Logging Loop
    while True:
        print("Logging Loop Started")

        # Check Pump State
        while STATE == "Startup":
            print("startup")

        while STATE == "Run":
            print("Run")

        while STATE == "Manual":
            print("Manual")

        while STATE == "Test":
            print("Test")

        while STATE == "Reset":
            print("Reset")





if __name__ == '__main__':
    main()
