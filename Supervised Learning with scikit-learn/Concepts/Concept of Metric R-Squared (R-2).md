# Concept of Metric R-Squared ($R^2$)

R-squared (often written as $R^2$ and pronounced "R-squared") is the most common metric used to evaluate how well a Regression model is performing. Its technical name is the **Coefficient of Determination**.

In classification, we used "Accuracy" to see how many categories we guessed correctly. But because regression predicts continuous numbers (like dollars), we can't easily use exact matches. Instead, $R^2$ measures how much of the data's variation is explained by your model.

Here is the easiest way to understand it:

### The Baseline: Guessing the Average
Imagine you want to predict a house's price, but you have no features (no square footage, no number of bedrooms). The smartest "dumb" guess you could make is simply the average price of all houses in the neighborhood.

$R^2$ compares your machine learning model (the red line you just plotted) against that baseline "dumb" average guess.

### How to read the R-squared score
$R^2$ usually outputs a score between 0 and 1 (which can be thought of as a percentage from 0% to 100%):

* **$R^2 = 1.0$ (100%): Perfect Fit.** Your model perfectly predicts every single data point. The red line goes exactly through every blue dot on your scatter plot.
* **$R^2 = 0.0$ (0%): No better than average.** Your model is completely useless. It doesn't perform any better than if you had just guessed the average every single time.
* **$R^2 = 0.80$ (80%): Good Fit.** This means 80% of the variation in the target variable can be explained by the features you used.

> [!NOTE]
> $R^2$ can technically go below 0 into negative numbers. If you get a negative score, it means your model is actively worse than just guessing the average!

### In the context of your exercise:
In your recent code, you predicted Sales based on Radio Expenditure.

If your model scores an $R^2$ of 0.75, it means that 75% of the differences in sales can be explained purely by how much money the company spent on radio ads. The remaining 25% of the variation in sales must be caused by other factors you didn't measure (like TV ads, seasonality, or competitor pricing).

In scikit-learn, you can calculate this very easily using:
```python
model.score(X, y)
```

---

## Deeper Dive

### 1. What is "Variation in the target variable"?
Your target variable is Sales. In the real world, a company's sales are never exactly the same every single week. One week they might make $10,000, and the next week they might make $50,000.

That fluctuation—the fact that the sales numbers go up and down—is what statisticians call **"variation."** 

### 2. What does "explained by the features" mean?
As a business owner, you want to know why your sales are going up and down. What is causing that variation?

In your model, the only feature you gave it to look at was Radio Expenditure (how much money was spent on radio ads).

**Putting it together (The 80% meaning):**
If your model gets an $R^2$ score of 0.80 (80%), it is telling you this:

> *"80% of the reason your sales go up and down is directly caused by how much money you spend on radio ads."*

**What about the other 20%?**
Since the score isn't 100%, it means radio ads don't explain everything. The remaining 20% of the fluctuation in your sales is caused by "mystery" factors that your model doesn't know about because you didn't give it that data.

Those mystery factors could be things like:
* TV advertising spending
* The weather
* A competitor lowering their prices
* The time of year (holidays)

So, an $R^2$ of 80% is considered a "Good Fit" because it proves that radio advertising is a massive, highly predictable driver of your sales!

---

## Multiple Linear Regression & $R^2$

If you add more columns (like "TV Expenditure" and "Social Media Expenditure" alongside Radio), you move from Simple Linear Regression to **Multiple Linear Regression**.

Adding more features changes two major things: how we interpret $R^2$, and how we visualize the data.

### 1. How your $R^2$ Score changes
Instead of just looking at Radio, your $R^2$ score now measures the combined teamwork of all your features.

If you train a model with Radio, TV, and Social Media spending, and your new $R^2$ is 0.95 (95%), it means:

> *"Radio, TV, and Social Media spending combined explain 95% of the variation in Sales."*

Generally, giving your model more useful data columns will make your $R^2$ score go up, because you are solving the "mystery" of what causes sales to fluctuate.

### 2. How Visualization changes
Right now, your visualization file creates a standard 2D graph (X-axis for Radio, Y-axis for Sales). The model's prediction is a red line.

* **If you use 2 Features (e.g., Radio + TV):** Your graph becomes 3D! You have an X-axis, a Y-axis, and a Z-axis. Instead of drawing a red line, the model draws a flat plane (like a sheet of paper) slicing through a 3D cloud of dots.
* **If you use 3+ Features:** The math moves into 4D space and beyond. It becomes physically impossible for human eyes to visualize it in a single scatter plot!

**How do data scientists visualize 3+ features?**
Because you cannot plot 5 features and 1 target on a single graph, the visual strategy changes. Instead of plotting the features on the X-axis, data scientists will plot the **Actual Target values on the X-axis** and the **Predicted Target values on the Y-axis**.

If a model is highly accurate, all the blue dots will form a perfect diagonal straight line, no matter how many hundreds of columns/features were used to make the prediction!
