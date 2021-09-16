import pytest
#import soil_moisture_sensor.app

def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"1"
	assert x == y,"2"
	assert 1 == 2, "3"
def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"4" 

# Is connection string populated or modified. Need it to break if changed