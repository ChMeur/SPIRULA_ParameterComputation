#!/usr/bin/env python

import numpy as np

if __name__ == "__main__":
    # string to define what to calculate:
    #   area - approx. area given drum radius and cable length
    #   length - cable length given drum radius and approx area
    #   radius - drum radius given approx. area and cable length
    calculateWhat = "length"
    Rd = 0.1        # drum radius [m]
    Lc = 17.85       # length of cable [m]
    As_approx = 1000.0   # approximate area as a circle [m]

    if calculateWhat == "area":
        As_approx = np.around(
            np.pi * (np.power(Lc, 2) + np.power(Rd, 2)), decimals=3)
        print(f"given drum radius Rd = {Rd} m and cable length Lc = {Lc} m\
            \n approx. area  As = {As_approx} m^2")
        print(f"#######################################################")
    elif calculateWhat == "length":
        Lc = np.around(
            np.sqrt(As_approx / np.pi - np.power(Rd, 2)), decimals=3)
        print(f"drum radius Rd = {Rd} m, approx. area As = {As_approx} m^2\
            \n necessary cable lenght Lc = {Lc} m")
        print(f"#######################################################")
    elif calculateWhat == "radius":
        Rd = np.around(
            np.sqrt(As_approx / np.pi - np.power(Lc, 2)), decimals=3)
        print(f"approx. area As = {As_approx} m^2, cable length Lc = {Lc} m\
            \n necessary drum radius Rd = {Rd} m")
        print(f"#######################################################")

    # spacing between revolutions
    Sr = np.around(2.0 * np.pi * Rd, decimals=3)
    print(f"drum radius Rd = {Rd} \n spacing between revolutions Sr = {Sr}")
    print(f"#######################################################")
    # calculate vehicle related and operational parameters
    beta = np.deg2rad(35.0)     # ang. FOV of camera [rad]
    h = 2.0                     # target altitude [m]
    # camera footprint along path [m]
    b_along = np.around(2.0 * h * np.tan(beta / 2.0), decimals=3)
    ns = 5.0                    # number of equal samples per frame
    fs = 2.0                   # sampling frequency [Hz]
    Ts = 1 / fs                 # sampling period [s]
    # vehicle speed based on camera footprint and sampling (along the path)
    v_along = np.around(b_along / (ns * Ts), decimals=3)   # [m/s]
    print(f"given camera footprint along path b_along = {b_along} m,\
        sampling frequency fs = {fs} Hz, number of equal samples ns = {ns}\
        \n speed along path v_along = {v_along} m/s")
    print(f"#######################################################")
    # surve time [s]
    t_survey = np.around(np.power(Lc, 2) / (2.0 * Rd * v_along), decimals=3)
    t_survey_min = np.around(t_survey / 60.0, decimals=2)
    print(f"cable length Lc = {Lc} m, drum radius Rd = {Rd} m,\
        speed along path v_along = {v_along} m/s\
        \n overall survey time t_survey = {t_survey_min} min")
    print(f"#######################################################")
    L_path = np.around(np.power(Lc, 2) / (2.0 * Rd))
    print(f"given cable length Lc = {Lc} m, and drum radius Rd = {Rd} m\
        \n overall path length L_path = {L_path} m")

