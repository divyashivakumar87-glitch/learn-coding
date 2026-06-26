testname = "Calibration Test"

# --- Positive Test Case 1: Login ---
testcase1Title = "Login into ADM to test agency"
teststep_1 = "Login into ADM to test agency"
teststep_2 = "Type in the agency name"
teststep_3 = "Click on the agency"
teststep_4 = "Type in username and password"
teststep_5 = "Click on the login button"
Expected = "Logged in successfully"
Actual = "Logged in successfully"
print("Test:", testname)
print("Test Case 1:", testcase1Title)
print("Test Step 1:", teststep_1)
print("Test Step 2:", teststep_2)
print("Test Step 3:", teststep_3)
print("Test Step 4:", teststep_4)
print("Test Step 5:", teststep_5)
print("Expected:", Expected)
print("Actual:", Actual)
print("Result: PASS" if Actual == Expected else "Result: FAIL")
print()

# --- Positive Test Case 2: Calibration ---
testcase2title = "Calibrate the sensor"
step1 = "Connect sensor to ADM"
step2 = "Sensor is connected successfully"
step3 = "Click on the calibration button"
step4 = "Calibration is started"
step5 = "Follow the instructions to calibrate the sensor"
step6 = "Sensor is calibrated successfully"
Expected = "Sensor is calibrated successfully"
Actual = "Sensor is calibrated successfully"
print("Test Case 2:", testcase2title)
print("Test Step 1:", step1)
print("Test Step 2:", step2)
print("Test Step 3:", step3)
print("Test Step 4:", step4)
print("Test Step 5:", step5)
print("Test Step 6:", step6)
print("Expected:", Expected)
print("Actual:", Actual)
print("Result: PASS" if Actual == Expected else "Result: FAIL")
print()

# ========== NEGATIVE TESTS ==========

# --- Negative Test 1: Login with invalid credentials ---
neg_test1_title = "Login with wrong username/password (negative)"
neg1_step1 = "Login into ADM to test agency"
neg1_step2 = "Type in the agency name"
neg1_step3 = "Enter invalid username and password"
neg1_expected = "Login failed - Invalid credentials"
neg1_actual = "Login failed - Invalid credentials"
print("NEGATIVE Test Case 1:", neg_test1_title)
print("Step 1:", neg1_step1)
print("Step 2:", neg1_step2)
print("Step 3:", neg1_step3)
print("Expected:", neg1_expected)
print("Actual:", neg1_actual)
print("Result: PASS (negative)" if neg1_actual == neg1_expected else "Result: FAIL")
print()

# --- Negative Test 2: Login with empty credentials ---
neg_test2_title = "Login with empty username/password (negative)"
neg2_expected = "Login failed - Required fields missing"
neg2_actual = "Login failed - Required fields missing"
print("NEGATIVE Test Case 2:", neg_test2_title)
print("Expected:", neg2_expected)
print("Actual:", neg2_actual)
print("Result: PASS (negative)" if neg2_actual == neg2_expected else "Result: FAIL")
print()

# --- Negative Test 3: Calibration with sensor not connected ---
neg_test3_title = "Calibrate when sensor is not connected (negative)"
neg3_step1 = "Do not connect sensor to ADM"
neg3_step2 = "Click on the calibration button"
neg3_expected = "Calibration failed - Sensor not connected"
neg3_actual = "Calibration failed - Sensor not connected"
print("NEGATIVE Test Case 3:", neg_test3_title)
print("Step 1:", neg3_step1)
print("Step 2:", neg3_step2)
print("Expected:", neg3_expected)
print("Actual:", neg3_actual)
print("Result: PASS (negative)" if neg3_actual == neg3_expected else "Result: FAIL")
print()

# --- Negative Test 4: Calibration interrupted / timeout ---
neg_test4_title = "Calibration interrupted or timeout (negative)"
neg4_expected = "Calibration failed - Timeout or interrupted"
neg4_actual = "Calibration failed - Timeout or interrupted"
print("NEGATIVE Test Case 4:", neg_test4_title)
print("Expected:", neg4_expected)
print("Actual:", neg4_actual)
print("Result: PASS (negative)" if neg4_actual == neg4_expected else "Result: FAIL")