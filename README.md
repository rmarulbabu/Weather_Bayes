# Unit V: Probabilistic Reasoning
## Weather Prediction using Bayesian Probability

A small probabilistic AI program in Python that predicts whether it will rain when the sky is cloudy, using Bayes' Theorem.

## Dataset

| Item | Days |
|------|------|
| Total days | 20 |
| Rain | 8 |
| Not Rain | 12 |
| Cloudy among rainy days | 7 |
| Cloudy among non-rainy days | 3 |

Observation: Sky = **Cloudy**

## What the Program Does

1. Calculates the prior probabilities P(Rain) and P(Not Rain)
2. Calculates P(Cloudy | Rain) and P(Cloudy | Not Rain)
3. Calculates P(Cloudy) using the total probability rule
4. Uses Bayes' Theorem to find P(Rain | Cloudy) and P(Not Rain | Cloudy)
5. Compares the two and displays the predicted weather

## How to Run

```
python weather_bayes.py
```

No extra libraries are needed.

## Output

```
Sky = Cloudy
----------------------------------------
P(Rain)              = 0.4
P(Not Rain)          = 0.6
P(Cloudy | Rain)     = 0.875
P(Cloudy | Not Rain) = 0.25
P(Rain | Cloudy)     = 0.7
P(Not Rain | Cloudy) = 0.3
----------------------------------------
Predicted Weather = Rain
```

## How Bayes' Theorem Was Used

```
P(Rain | Cloudy) = P(Cloudy | Rain) x P(Rain) / P(Cloudy)
```

1. **Prior:** P(Rain) = 8/20 = 0.4 and P(Not Rain) = 12/20 = 0.6. This is our belief before looking at the sky.
2. **Likelihood:** P(Cloudy | Rain) = 7/8 = 0.875 and P(Cloudy | Not Rain) = 3/12 = 0.25.
3. **Evidence:** P(Cloudy) = (0.875 x 0.4) + (0.25 x 0.6) = 0.5.
4. **Posterior:**
   - P(Rain | Cloudy) = (0.875 x 0.4) / 0.5 = 0.7
   - P(Not Rain | Cloudy) = (0.25 x 0.6) / 0.5 = 0.3
5. **Comparison:** 0.7 > 0.3, so the predicted weather is **Rain**.

Rain is less common overall (40%), but clouds are much more common on rainy days. So a cloudy sky raises the chance of rain from 40% to 70%.

## Concepts Used

- Prior probability
- Conditional probability (likelihood)
- Total probability rule
- Bayes' Theorem
- Posterior probability comparison
