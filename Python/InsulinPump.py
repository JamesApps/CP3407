# CP3407 Insulin Pump Python BackEnd

import os.path
import sqlite3
from sqlite3 import Error
import Clock
import InsulinReservoir
import BloodGlucose
import Battery
import time

# Initial/default Pump configuration parameters to store in db
first_name = 'Joe'
last_name = 'Doe'

capacity_insulin = 100.0
drip_rate = 1.0
safe_min = 6.0
safe_max = 14.0
max_daily_dose = 25.0
max_single_dose = 4.0
minimum_dose = 1.0
bg_sensor = BloodGlucose.BloodGlucose()
clock = Clock.Clock()
clock_time = clock.getTime()
battery = Battery.Battery()

sqlite_file = 'insulin_pump.sqlite'  # name of the sqlite database file


def get_db(table_name, column_name):
    try:
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
    except Error as e:
        print(e)
    else:
        c.execute('SELECT ' + column_name + ' FROM ' + table_name)
        data = c.fetchone()
        return data[0]
    conn.close()


def create_db():
    # Create database if not already created

    # Tables
    table_name1 = 'Patient'  # name of the table to be created
    table_1_column = ['first_name', 'last_name']  # name of columns
    table_1_column_field_type = ['STRING', 'STRING']  # column data types

    table_name2 = 'Insulin'  # name of the table to be created
    table_2_column = ['drip_rate', 'max_daily_dose', 'capacity_insulin', 'safe_min', 'safe_max',
                      'minimum_dose', 'max_single_dose']  # name of columns
    table_2_column_field_type = ['REAL', 'REAL', 'REAL', 'REAL', 'REAL',
                                 'REAL', 'REAL']  # column data types

    table_name3 = 'Information_Log'  # name of the table to be created
    table_3_column = ['clock_time', 'battery_power_level', 'remaining_insulin',
                      'cumulative_dose', 'blood_glucose_level']  # name of columns
    table_3_column_field_type = ['STRING', 'FLOAT', 'REAL', 'REAL', 'REAL']  # column data types

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

    table_name = 'Patient'
    column_string = 'first_name, last_name'
    data_list = first_name, last_name
    command = 'INSERT INTO ' + table_name + '(' + column_string + ') VALUES (?, ?)'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute(command, data_list)
    conn.commit()

    # Insulin
    table_name = 'Insulin'
    column_string = 'drip_rate, max_daily_dose, capacity_insulin, safe_min, safe_max, minimum_dose, max_single_dose'
    data_list = drip_rate, max_daily_dose, capacity_insulin, safe_min, safe_max, minimum_dose, max_single_dose
    command = 'INSERT INTO ' + table_name + '(' + column_string + ') VALUES (?, ?, ?, ?, ?, ?, ?)'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute(command, data_list)
    conn.commit()

    # Information_Log
    # Insulin
    table_name = 'Information_Log'
    column_string = 'clock_time, battery_power_level, remaining_insulin, cumulative_dose, blood_glucose_level'
    data_list = str(clock_time), battery.batteryLevel, 100.0, 0.0, bg_sensor.bg
    command = 'INSERT INTO ' + table_name + '(' + column_string + ') VALUES (?, ?, ?, ?, ?)'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute(command, data_list)
    conn.commit()


def update_db(remaining_insulin, cumulative_dose, blood_glucose_level):
    clock_time = clock.getTime()
    battery_power_level = battery.getBattery()
    try:
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
    except Error as e:
        print(e)
    else:
        c.execute('INSERT INTO Information_Log(clock_time, battery_power_level, '
                  'remaining_insulin, cumulative_dose, blood_glucose_level) VALUES(?, ?, ?, ?, ?)',
                  (clock_time, battery_power_level, remaining_insulin, cumulative_dose, blood_glucose_level))
        print("\nInformation log entry to be added to DB:")
        print('Clock:', clock_time, '\nBattery Power:', battery_power_level, '\nRemaining Insulin', remaining_insulin,
              '\nCumulative Dose:', cumulative_dose, '\nBlood Glucose Level: ', blood_glucose_level)

        conn.commit()
        conn.close()


def state_run(reservoir, r0, r1, r2):
    # The RUN schema defines the system state for normal operation. The software defined in
    # the RUN schema should execute every 10 minutes.

    if reservoir.insulinAvailable < max_single_dose:
        # Raise Error
        print("Insufficient insulin")
    elif reservoir.cumulativeDose > max_daily_dose:
        # Raise Error
        print('Cumulative dose exceeds max daily dose')
    else:
        # Get Comp Dose
        print('Compute Dose')
        compdose = get_compdose(r0, r1, r2)

        # If the computed insulin dose is zero, don’t deliver any insulin
        if compdose == 0:
            dose = 0

        # The maximum daily dose would be exceeded if the computed dose was delivered
        elif (compdose + reservoir.cumulativeDose) > max_daily_dose:
            print("Max daily dose exceeded")
            dose = 0
            # alarm

        # The normal situation. If maximum single dose is not exceeded then deliver computed dose
        elif (compdose + reservoir.cumulativeDose) < max_daily_dose and compdose <= max_single_dose:
            dose = compdose

        # The single dose computed is too high. Restrict the dose delivered to the maximum single dose
        elif compdose > max_single_dose:
            dose = max_single_dose

        # # In case of error in system, no dose
        # else:
        #     dose = 0

        reservoir.insulinAvailable -= dose
        reservoir.cumulativeDose += dose

        if reservoir.insulinAvailable <= max_single_dose * 4:
            print("Low insulin")
            # alarm

    r0 = r1
    r1 = r2
    return reservoir.insulinAvailable, reservoir.cumulativeDose, r0, r1


def get_compdose(r0, r1, r2):
    # r0, r1, and r2 maintain information about the last three readings from the sugar
    # sensor. r2 holds the current reading, r1 the previous reading and r0 the reading
    # before that. These are used to compute the rate of change of blood sugar readings
    compdose = 0

    # SUGAR_LOW
    if r2 < safe_min:
        compdose = 0
        # alarm low sugar

    # SUGAR_OK
    elif safe_min <= r2 <= safe_max:
        # sugar level stable or falling
        if r2 <= r1:
            compdose = 0

        # sugar level increasing but rate of increase falling
        elif r2 > r1 and (r2 - r1) < (r1 - r0):
            compdose = 0

        # sugar level increasing and rate of increase increasing compute dose a minimum dose must be delivered
        # if rounded to zero
        elif r2 > r1 and (r2 - r1) >= (r1 - r0) and (round((r2 - r1) / 4) == 0):
            compdose = minimum_dose

        elif r2 > r1 and (r2 - r1) >= (r1 - r0) and (round((r2 - r1) / 4) > 0):
            compdose = round((r2 - r1) / 4)

    # SUGAR_HIGH
    elif r2 > safe_max:
        # sugar level increasing. Round down if below 1 unit.
        if r2 > r1 and (round((r2 - r1) / 4) == 0):
            compdose = minimum_dose

        elif r2 > r1 and (round((r2 - r1) / 4) > 0):
            compdose = round((r2 - r1) / 4)

        # sugar level stable
        elif r2 == r1:
            compdose = minimum_dose

        # sugar level falling and rate of decrease increasing
        elif r2 < r1 and (r2 - r1) <= (r1 - r0):
            compdose = 0

        # sugar level falling and rate of decrease decreasing
        elif r2 < r1 and (r2 - r1) > (r1 - r0):
            compdose = minimum_dose
    return compdose


def state_startup():
    # The STARTUP schema models the behaviour of the system when the user switches on the
    # device. It is assumed that the user’s blood sugar at that stage is OK. Note that
    # cumulative_dose is NOT set in the startup sequence but can only be set to zero at midnight.
    # This means that the total cumulative dose delivered can always be tracked by the system
    # and is not affected by the user switching the machine on and off.
    if os.path.isfile(sqlite_file):
        cumulative_dose = get_db('Information_Log', 'cumulative_dose')
        insulin_available = get_db('Information_Log', 'remaining_insulin')
        reservoir = InsulinReservoir.InsulinReservoir(insulin_available, cumulative_dose)
        r0 = safe_min
        r1 = get_db('Information_Log', 'blood_glucose_level')
    else:
        create_db()
        r0 = safe_min
        r1 = safe_max
        reservoir = InsulinReservoir.InsulinReservoir(capacity_insulin, 0)
    dose = 0
    state = 'Run'
    return dose, r0, r1, reservoir, state


def state_manual(reservoir):
    # The MANUAL schema models the system behaviour when it is in manual override mode.
    # Notice that cumulative_dose is still updated but that no safety checks are applied until the
    # system is reset to automatic mode.

    # One dose for each button press
    dose = 1
    reservoir.insulinAvailable -= dose
    reservoir.cumulativeDose += dose

    # At the end of the manual mode, state set to run
    state = 'Run'
    return reservoir.insulinAvailable, reservoir.cumulativeDose, state


def state_reset():
    # The RESET schema models the system when the user changes the insulin reservoir. Notice
    # that this does not require the device to be switched off. The design of the reservoir is such
    # that it is not possible to insert reservoirs that are partially full.

    insulin_available = capacity_insulin
    # At the end of the reset mode, state set to run
    state = 'Run'
    return insulin_available, state


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
    elif battery < 5:
        alarm("battery_low")
    elif not pump:
        alarm("pump_failure")
    elif not sensor:
        alarm("sensor_failure")
    elif not delivery:
        alarm("delivery_failure")
    else:
        print('Passed Test \n')


def alarm(function):
    # Alarm Functions
    # Battery low - The voltage of the battery has fallen to less than 5%
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
    # Calls Start Up function to initiate the insulin pump, then moves to the logging loop, which is 'Run' State
    # The loop State change to either manual injection, or

    # Start Up Function
    dose, r0, r1, reservoir, state = state_startup()

    # Logging Loop
    while True:
        # Check Pump State
        while state == "Run":
            print('\nClock:', str(clock.getTime()))
            print('Insulin Available:', reservoir.insulinAvailable, '\nCumulative Dose:', reservoir.cumulativeDose,
                  '\nr0:', r0, '\nr1:', r1, '\n')

            # 30 sec hardware test
            time.sleep(30)
            state_test(reservoir.needleStatus, reservoir.reservoirStatus, reservoir.insulinAvailable,
                       battery.batteryLevel, reservoir.pumpStatus, bg_sensor.sensorStatus, reservoir.deliveryStatus)
            if clock.minutes % 10 == 0:
                r2 = bg_sensor.getBG()
                print('r2:', r2)
                reservoir.insulinAvailable, reservoir.cumulativeDose, r0, r1 = state_run(reservoir, r0, r1, r2)
                update_db(reservoir.insulinAvailable, reservoir.cumulativeDose, r2)

            if clock.hours == 0 and clock.minutes == 0:
                # At the beginning of each 24 hour period (indicated by clock =00:00:00), the
                # cumulative dose of insulin delivered is reset to 0.
                print("DAILY RESET CUMULATIVE DOSE")
                reservoir.cumulativeDose = 0

            # EVENT FOR MANUAL MODE
            # if button press event:
            #     state = 'Manual'

            # EVENT FOR RESET MODE
            # if removed reservoir event:
            #     state = 'Reset'

        while state == "Manual":
            print('Entered Manual Mode')
            reservoir.insulinAvailable, reservoir.cumulativeDose, state = state_manual(reservoir)

        while state == "Reset":
            print('Entered Reset Mode')
            reservoir.insulinAvailable, state = state_reset()


if __name__ == '__main__':
    main()
