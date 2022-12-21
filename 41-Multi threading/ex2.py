# %a
#
# Locale’s abbreviated weekday name.
#
# %A
#
# Locale’s full weekday name.
#
# %b
#
# Locale’s abbreviated month name.
#
# %B
#
# Locale’s full month name.
#
# %c
#
# Locale’s appropriate date and time representation.
#
# %d
#
# Day of the month as a decimal number [01,31].
#
# %H
#
# Hour (24-hour clock) as a decimal number [00,23].
#
# %I
#
# Hour (12-hour clock) as a decimal number [01,12].
#
# %j
#
# Day of the year as a decimal number [001,366].
#
# %m
#
# Month as a decimal number [01,12].
#
# %M
#
# Minute as a decimal number [00,59].
#
# %p
#
# Locale’s equivalent of either AM or PM.
#
# (1)
#
# %S
#
# Second as a decimal number [00,61].
#
# (2)
#
# %U
#
# Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.
#
# (3)
#
# %w
#
# Weekday as a decimal number [0(Sunday),6].
#
# %W
#
# Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
#
# (3)
#
# %x
#
# Locale’s appropriate date representation.
#
# %X
#
# Locale’s appropriate time representation.
#
# %y
#
# Year without century as a decimal number [00,99].
#
# %Y
#
# Year with century as a decimal number.
#
# %z
#
# Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59]. 1
#
# %Z
#
# Time zone name (no characters if no time zone exists). Deprecated. 1
#
# %%
# 
# A literal '%' character.
#
# Notes:
#
# When used with the strptime() function, the %p directive only affects the output hour field if the %I directive is used to parse the hour.
#
# The range really is 0 to 61; value 60 is valid in timestamps representing leap seconds and value 61 is supported for historical reasons.
#
# When used with the strptime() function, %U and %W are only used in calculations when the day of the week and the year are specified.