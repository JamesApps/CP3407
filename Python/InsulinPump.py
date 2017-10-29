# CP3407 Insulin Pump Python BackEnd

import os.path
import sqlite3
from sqlite3 import Error
import Clock

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
    table_5_column_field_type = ['INTEGER', 'INT']  # column data types

    table_name6 = 'Information_Log'  # name of the table to be created
    table_6_column = ['information_log_id', 'clock_time', 'battery_power_level', 'remaining_insulin',
                      'blood_glucose_level']  # name of columns
    table_6_column_field_type = ['INTEGER', 'FLOAT', 'FLOAT', 'FLOAT', 'INT']  # column data types

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


def state_run(insulin_available, cumulative_dose, r0, r1, r2):
    # The RUN schema defines the system state for normal operation. The software defined in
    # the RUN schema should execute every 10 minutes.

    if insulin_available < max_single_dose:
        # Raise Error
        print("Insufficient insulin")
    elif cumulative_dose > max_daily_dose:
        # Raise Error
        print('Cumulative dose exceeds max daily dose')
    else:
        # Get sugar level from database


        # Get Comp Dose
        compdose = get_compdose(r0, r1, r2)

        # If the computed insulin dose is zero, don’t deliver any insulin
        if compdose == 0:
            dose = 0

        # The maximum daily dose would be exceeded if the computed dose was delivered
        elif (compdose + cumulative_dose) > max_daily_dose:
            print("Max daily dose exceeded")
            # alarm

        # The normal situation. If maximum single dose is not exceeded then deliver computed dose
        elif (compdose + cumulative_dose) < max_daily_dose and compdose <= max_single_dose:
            dose = compdose

        # The single dose computed is too high. Restrict the dose delivered to the maximum single dose
        elif compdose > max_single_dose:
            dose = max_single_dose

        insulin_available -= dose
        cumulative_dose += dose

        if insulin_available <= max_single_dose * 4:
            print("Low insulin")
            # alarm

    r0 = r1
    r1 = r2
    return r0, r1


def get_compdose(r0, r1, r2):
    # r0, r1, and r2 maintain information about the last three readings from the sugar
    # sensor. r2 holds the current reading, r1 the previous reading and r0 the reading
    # before that. These are used to compute the rate of change of blood sugar readings

    # SUGAR_LOW
    if r2 < safemin:
        compdose = 0
        # alarm low sugar

    # SUGAR_OK
    elif safemin <= r2 <= safemax:
        # sugar level stable or falling
        if r2 <= r1:
            compdose = 0

        # sugar level increasing but rate of increase falling
        elif r2 > r1 and (r2-r1) < (r1-r0):
            compdose = 0

        # sugar level increasing and rate of increase increasing compute dose a minimum dose must be delivered
        # if rounded to zero
        elif r2 > r1 and (r2-r1) >= (r1-r0) and (round((r2-r1)/4) == 0):
            compdose = minimum_dose

        elif r2 > r1 and (r2-r1) >= (r1-r0) and (round((r2-r1)/4) > 0):
            compdose = round((r2-r1)/4)

    # SUGAR_HIGH
    elif r2 > safemax:
        # sugar level increasing. Round down if below 1 unit.
        if r2 > r1 and (round((r2-r1)/4) == 0):
            compdose = minimum_dose

        elif r2 > r1 and (round((r2-r1)/4) > 0):
            compdose = round((r2-r1)/4)

        # sugar level stable
        elif r2 == r1:
            compdose = minimum_dose

        # sugar level falling and rate of decrease increasing
        elif r2 < r1 and (r2-r1) <= (r1-r0):
            compdose = 0

        # sugar level falling and rate of decrease decreasing
        elif r2 < r1 and (r2-r1) > (r1-r0):
            compdose = minimum_dose
    return compdose


def state_manual(insulin_available, cumulative_dose):
    # The MANUAL schema models the system behaviour when it is in manual override mode.
    # Notice that cumulative_dose is still updated but that no safety checks are applied until the
    # system is reset to automatic mode.

    dose = ManualDeliveryButton
    insulin_available -= dose
    cumulative_dose += dose


def state_startup():
    # The STARTUP schema models the behaviour of the system when the user switches on the
    # device. It is assumed that the user’s blood sugar at that stage is OK. Note that
    # cumulative_dose is NOT set in the startup sequence but can only be set to zero at midnight.
    # This means that the total cumulative dose delivered can always be tracked by the system
    # and is not affected by the user switching the machine on and off.
    dose = 0
    r0 = safemin
    r1 = safemax
    # TEST
    return dose, r0, r1


def state_reset(reservoir):
    # The RESET schema models the system when the user changes the insulin reservoir. Notice
    # that this does not require the device to be switched off. The design of the reservoir is such
    # that it is not possible to insert reservoirs that are partially full.

    if reservoir:
        insulin_available = capacity
    else:
        alarm("reservoir_removed")

    return insulin_available
    # TEST


def state_test(needle, reservoir, insulin_available, battery, pump, sensor, delivery):
    # The TEST schema models the behaviour of the hardware self-test unit which runs a test on
    # the system hardware every 30 seconds.
    print("Test")

    if not needle:
        alarm("needle_removed")
    elif not reservoir:
        alarm("reservoir_removed")
    elif insulin_available < max_single_dose:
        alarm("low_insulin")
    elif battery < 0.5:
        alarm("battery_low")
    elif not pump:
        alarm("pump_failure")
    elif not sensor:
        alarm("sensor_failure")
    elif not delivery:
        alarm("delivery_failure")
    else:
        print('Passed Test')



def alarm(function):
    # Alarm Functions
    # Battery low - The voltage of the battery has fallen to less than 0.5V
    if function == "battery_low":
        print("battery_low")

    # Sensor failure - The self-test of the sugar sensor has resulted in an error
    if function == "sensor_failure":
        print("sensor_failure")

    # Pump failure - The self-test of the pump has resulted in an error
    if function == "pump_failure":
        print("pump_failure")

    # Delivery failure - It has not been possible to deliver the specified amount of insulin
    # (e.g. the needle may be blocked or incorrectly inserted)
    if function == "delivery_failure":
        print("delivery_failure")

    # Needle assembly removed - The user has removed the needle assembly
    if function == "needle_removed":
        print("needle_removed")

    # Insulin reservoir removed - The user has removed the insulin reservoir
    if function == "reservoir_removed":
        print("reservoir_removed")

    # Low insulin level - The level of insulin is low (indicating that the reservoir should be changed).
    if function == "low_insulin":
        print("low_insulin")


def main():
    # Main Function

    clock = Clock.Clock()
    hours = clock.hours
    print(hours)
    # At the beginning of each 24 hour period (indicated by clock =00:00:00), the
    # cumulative dose of insulin delivered is reset to 0.

    # SQLite Database
    if os.path.isfile(sqlite_file):
        pass
    else:
        create_db()

    state_startup()

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
