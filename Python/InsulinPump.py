# CP3407 Insulin Pump Python BackEnd

import os.path
import sqlite3
from sqlite3 import Error
from Clock import Clock

# Pump configuration parameters
capacity = 100
safemin = 6
safemax = 14
max_daily_dose = 25
max_single_dose = 4
minimum_dose = 1

STATE = ""

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


def state_run(insulin_available, cumulative_dose):
    # The RUN schema defines the system state for normal operation. The software defined in
    # the RUN schema should execute every 10 minutes.

    if insulin_available < max_single_dose:
        # Raise Error
        print("Insufficient insulin")
    elif cumulative_dose > max_daily_dose:
        # Raise Error
        print('Cumulative dose exceeds max daily dose')
    else:
        print("sugar level")# SUGAR_LOW ∨ SUGAR_OK ∨ SUGAR_HIGH

        # If the computed insulin dose is zero, don’t deliver any insulin
        # CompDose = 0 ⇒ dose! = 0

        # // The maximum daily dose would be exceeded if the computed dose was delivered
        # CompDose + cumulative_dose > max_daily_dose ⇒ alarm! = on
        # ∧ status’ = warning ∧ dose! = max_daily_dose – cumulative_dose


        # // The normal situation. If maximum single dose is not exceeded then deliver computed
        # dose
        # CompDose + cumulative_dose < max_daily_dose ⇒
        # (CompDose ≤ max_single_dose ⇒ dose! = CompDose

        # // The single dose computed is too high. Restrict the dose delivered to the maximum single
        # dose
        # CompDose > max_single_dose ⇒ dose! = max_single_dose
        #  )
        # insulin_available’ = insulin_available – dose!
        # cumulative_dose’ = cumulative_dose + dose!
        # insulin_available ≤ max_single_dose * 4 ⇒ status’ = warning ∧ display1! =
        # display1! ∪ “Insulin low”
        # r1’ = r2
        # r0’ = r1

def state_manual():
    print("Manual")
    # The MANUAL schema models the system behaviour when it is in manual override mode.
    # Notice that cumulative_dose is still updated but that no safety checks are applied until the
    # system is reset to automatic mode.

    # switch? = manual
    # display1! = “Manual override”
    # dose! = ManualDeliveryButton?
    # cumulative_dose’ = cumulative_dose + dose!
    # insulin_available’ = insulin_available – dose!

def state_startup():
    print("Startup")
    # The STARTUP schema models the behaviour of the system when the user switches on the
    # device. It is assumed that the user’s blood sugar at that stage is OK. Note that
    # cumulative_dose is NOT set in the startup sequence but can only be set to zero at midnight.
    # This means that the total cumulative dose delivered can always be tracked by the system
    # and is not affected by the user switching the machine on and off.

    # switch? = off ∧ switch?’ = auto
    # dose! = 0
    # r0’ = safemin
    # r1’ = safemax
    # TEST


def state_reset():
    print("Reset")
    # The RESET schema models the system when the user changes the insulin reservoir. Notice
    # that this does not require the device to be switched off. The design of the reservoir is such
    # that it is not possible to insert reservoirs that are partially full.

    # InsulinReservoir? = notpresent and InsulinReservoir?’ = present
    # insulin_available’ = capacity
    # insulinlevel’ = OK
    # TEST

def state_test():
    # The TEST schema models the behaviour of the hardware self-test unit which runs a test on
    # the system hardware every 30 seconds.
    print("Test")

    # (HardwareTest? = OK ∧ Needle? = present ∧ InsulinReservoir? = present ⇒
    # status’ = running ∧ alarm! = off ∧ display1!= “” )
    #
    # ∨ (
    # status’ = error
    # alarm! = on
    # (
    #     Needle? = notpresent ⇒ display1! = display1! ∪ “No needle unit” ∨
    #     ( InsulinReservoir? = notpresent ∨ insulin_available < max_single_dose)
    #     ⇒ display1! = display1! ∪ “No insulin” ∨
    #
    #     HardwareTest? = batterylow ⇒ display1! = display1! ∪ ”Battery low” ∨
    #     HardwareTest? = pumpfail ⇒ display1! = display1! ∪ ”Pump failure” ∨
    #     HardwareTest? = sensorfail ⇒ display1! = display1! ∪ ”Sensor failure” ∨
    #     HardwareTest? = deliveryfail ⇒ display1! = display1! ∪ ”Needle failure” ∨
    #     )
    # )


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


def main():
    # Main Function

    Clock()
    # At the beginning of each 24 hour period (indicated by clock =00:00:00), the
    # cumulative dose of insulin delivered is reset to 0.

    # SQLite Database
    if os.path.isfile(sqlite_file):
        pass
    else:
        create_db()

    # Logging Loop
    while True:
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
