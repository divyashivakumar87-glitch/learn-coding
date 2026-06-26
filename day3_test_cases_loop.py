test_name="Button Sequence"
test_step="Press and release button"
Expected="No LED should blink"
Actual="LED blinks RED"
print("Test:" , test_name)
print("Step:" , test_step)
print("Expected:" , Expected)
print("Actual:" , Actual)
if Actual == Expected:
    print("Final Result: Pass")
else:
    print("Final Result: Fail")

