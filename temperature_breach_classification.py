from check_breach import infer_breach 

temperature_limits = {
    'PASSIVE_COOLING': (0,35),
    'HI_ACTIVE_COOLING': (0,45),
    'MED_ACTIVE_COOLING': (0,40)
    }

def classify_temperature_breach(coolingType, temperatureInC):
        if coolingType not in temperature_limits:
            raise ValueError(f'Invalid cooling type:{coolingType}')
        lowerLimit,upperLimit = temperature_limits[coolingType]  
        return infer_breach(temperatureInC, lowerLimit, upperLimit)

