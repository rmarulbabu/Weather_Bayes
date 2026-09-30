# Unit V: Probabilistic Reasoning
# Weather Prediction using Bayesian Probability

# Dataset
total_days = 20
rain_days = 8
not_rain_days = 12

cloudy_and_rain = 7        # cloudy days among rainy days
cloudy_and_not_rain = 3    # cloudy days among non-rainy days

# Prior probabilities
p_rain = rain_days / total_days
p_not_rain = not_rain_days / total_days

# Conditional probabilities
p_cloudy_given_rain = cloudy_and_rain / rain_days
p_cloudy_given_not_rain = cloudy_and_not_rain / not_rain_days

# P(Cloudy) using total probability
p_cloudy = (p_cloudy_given_rain * p_rain) + (p_cloudy_given_not_rain * p_not_rain)

# Bayes' Theorem
p_rain_given_cloudy = (p_cloudy_given_rain * p_rain) / p_cloudy
p_not_rain_given_cloudy = (p_cloudy_given_not_rain * p_not_rain) / p_cloudy

# Display
print("Sky = Cloudy")
print("-" * 40)
print("P(Rain)              =", round(p_rain, 4))
print("P(Not Rain)          =", round(p_not_rain, 4))
print("P(Cloudy | Rain)     =", round(p_cloudy_given_rain, 4))
print("P(Cloudy | Not Rain) =", round(p_cloudy_given_not_rain, 4))
print("P(Rain | Cloudy)     =", round(p_rain_given_cloudy, 4))
print("P(Not Rain | Cloudy) =", round(p_not_rain_given_cloudy, 4))
print("-" * 40)

# Compare and predict
if p_rain_given_cloudy > p_not_rain_given_cloudy:
    print("Predicted Weather = Rain")
else:
    print("Predicted Weather = Not Rain")
