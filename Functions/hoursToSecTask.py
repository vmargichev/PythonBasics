def hours_to_seconds(hours):
    seconds = hours * 3600
    return seconds

# Don't touch below this line


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(2.5)
test(100)
test(33)
